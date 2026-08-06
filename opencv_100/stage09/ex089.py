# ============================================================================
# 노션 원문 학습 설명: 예제 89. 로봇 추종용 비전 노드
# ============================================================================
#
# [핵심 주제]
# 색상 객체 중심 좌표를 계산하고, 화면 중앙 대비 오차를 발행
#
# 로봇 추종 제어에서 핵심은 객체 좌표 자체보다 화면 중앙에서 얼마나 벗어났는지임
#
# error_x = center_x - image_center_x
#
# 이 값으로 로봇의 회전 방향을 결정함
#
# [실습 목표]
# 1. 객체 중심 좌표 계산
# 2. 화면 중앙 기준선 계산
# 3. error_x 계산
# 4. error_x를 ROS2 Topic으로 발행
#
# [실무에서 자주 하는 실수]
# 실수 1. error_x 부호를 반대로 사용
#
# 카메라 좌표계와 로봇 회전 방향을 반드시 확인필요
#
# 로봇이 반대로 돌면 `angular_z` 부호를 바꿔야 함
#
# 실수 2. 검출 실패 시 제어 노드가 계속 움직임
#
# 비전 노드가 target_error를 발행하지 않는 경우 제어 노드에서 정지하도록 설계필요
#
# [ROS2와 연결되는 포인트]
# 이 예제는 실제 객체 추종 로봇의 비전 노드에 가깝습니다.
#
# 비전 노드:
# /camera/image_raw Subscribe
# /vision/target_error Publish
#
# 제어 노드:
# /vision/target_error Subscribe
# /cmd_vel Publish
# ============================================================================
# Python으로 ROS2 노드를 만들고 실행하기 위해 rclpy를 불러오기
import rclpy
# ROS2 노드 클래스를 만들 때 상속할 Node를 불러오기
from rclpy.node import Node
# ROS2에서 카메라 영상을 주고받는 Image 메시지 형식을 불러오기
from sensor_msgs.msg import Image
# x, y, z 좌표를 전달할 수 있는 ROS2 Point 메시지를 불러오기
from geometry_msgs.msg import Point
# ROS2 Image 메시지와 OpenCV 이미지 배열을 서로 변환하는 CvBridge를 불러오기
from cv_bridge import CvBridge
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 관련 기능과 데이터를 하나로 묶는 클래스를 정의함
class FollowVisionNode(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드임
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정함
        super().__init__("follow_vision_node")

        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 생성
        self.bridge = CvBridge()

        # 다른 ROS2 노드가 보낸 메시지를 받을 Subscriber를 생성
        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        # 처리 결과를 다른 ROS2 노드에 보낼 Publisher를 생성
        self.error_pub = self.create_publisher(
            Point,
            "/vision/target_error",
            10
        )

        # 처리 결과를 다른 ROS2 노드에 보낼 Publisher를 생성
        self.debug_image_pub = self.create_publisher(
            Image,
            "/vision/debug_image",
            10
        )

    # image_callback 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def image_callback(self, msg):
        # 영상 변환이나 처리 중 오류가 나더라도 노드 전체가 갑자기 종료되지 않도록 예외 처리를 시작함
        try:
            # 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            debug_frame, result = self.process_frame(frame)

            # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
            if result is not None:
                # center x 값을 계산하거나 저장해 이후 처리에서 사용
                center_x = result["center_x"]
                # center y 값을 계산하거나 저장해 이후 처리에서 사용
                center_y = result["center_y"]
                # area 값을 계산하거나 저장해 이후 처리에서 사용
                area = result["area"]
                # error x 값을 계산하거나 저장해 이후 처리에서 사용
                error_x = result["error_x"]

                # error msg 값을 계산하거나 저장해 이후 처리에서 사용
                error_msg = Point()
                error_msg.x = float(error_x)
                error_msg.y = float(center_y)
                error_msg.z = float(area)

                # 완성한 ROS2 메시지를 지정한 Topic으로 발행
                self.error_pub.publish(error_msg)

            # OpenCV 이미지 배열을 ROS2 Image 메시지로 변환
            debug_msg = self.bridge.cv2_to_imgmsg(
                debug_frame,
                encoding="bgr8"
            )
            debug_msg.header = msg.header

            # 완성한 ROS2 메시지를 지정한 Topic으로 발행
            self.debug_image_pub.publish(debug_msg)

        # 위의 처리 과정에서 오류가 발생했을 때 실행할 코드를 작성함
        except Exception as e:
            # 오류 내용을 ROS2 로그에 출력
            self.get_logger().error(f"추종 비전 처리 오류: {e}")

    # process_frame 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def process_frame(self, frame):
        # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
        height, width = frame.shape[:2]
        # image center x 값을 계산하거나 저장해 이후 처리에서 사용
        image_center_x = width // 2

        # 색상 검출이 쉬운 HSV 색상 공간으로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
        lower_blue = np.array([100, 100, 100])
        upper_blue = np.array([130, 255, 255])

        # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # 형태학적 연산이나 필터에 사용할 값이 1인 커널 배열을 생성
        kernel = np.ones((5, 5), np.uint8)
        # 작은 흰색 노이즈를 제거하기 위해 열기 연산을 적용
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # 객체 내부의 작은 검은 구멍을 메우기 위해 닫기 연산을 적용
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 생성
        debug_frame = frame.copy()

        # 기준선이나 검출 결과를 표시하기 위해 선을 그리기
        cv2.line(
            debug_frame,
            (image_center_x, 0),
            (image_center_x, height),
            (255, 0, 0),
            2
        )

        # 검출되거나 매칭된 항목의 개수를 확인
        if len(contours) == 0:
            # 이미지 위에 상태나 좌표 정보를 글자로 표시
            cv2.putText(
                debug_frame,
                "Target Not Found",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )
            # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
            return debug_frame, None

        # 윤곽선이 차지하는 픽셀 면적을 계산
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if area < 500:
            # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
            return debug_frame, None

        # 윤곽선의 면적과 중심점을 계산하는 데 필요한 모멘트 값을 구함
        moments = cv2.moments(largest_contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if moments["m00"] == 0:
            # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
            return debug_frame, None

        # center x 값을 계산하거나 저장해 이후 처리에서 사용
        center_x = int(moments["m10"] / moments["m00"])
        # center y 값을 계산하거나 저장해 이후 처리에서 사용
        center_y = int(moments["m01"] / moments["m00"])

        # error x 값을 계산하거나 저장해 이후 처리에서 사용
        error_x = center_x - image_center_x

        # 검출한 윤곽선을 결과 이미지 위에 그리기
        cv2.drawContours(
            debug_frame,
            [largest_contour],
            -1,
            (0, 255, 0),
            2
        )

        # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
        cv2.circle(
            debug_frame,
            (center_x, center_y),
            8,
            (0, 0, 255),
            -1
        )

        # 이미지 위에 상태나 좌표 정보를 글자로 표시
        cv2.putText(
            debug_frame,
            f"error_x: {error_x}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        # result 변수에 이후 처리에 사용할 값을 저장
        result = {
            "center_x": center_x,
            "center_y": center_y,
            "area": area,
            "error_x": error_x
        }

        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
        return debug_frame, result

# 프로그램 실행 순서를 담당하는 main 함수를 정의함
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장
    node = FollowVisionNode()

    # 노드가 종료될 때까지 콜백을 계속 처리하도록 실행 상태를 유지
    rclpy.spin(node)

    # 사용이 끝난 ROS2 노드 자원을 정리함
    node.destroy_node()
    # ROS2 사용을 종료하고 관련 자원을 정리함
    rclpy.shutdown()

# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인
if __name__ == "__main__":
    main()
