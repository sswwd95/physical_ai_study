# ============================================================================
# 노션 원문 학습 설명: 예제 88. 객체 중심 좌표 Publisher
# ============================================================================
#
# [핵심 주제]
# 카메라 영상에서 색상 객체를 검출하고, 객체 중심 좌표를 ROS2 Topic으로 발행
#
# 간단한 실습에서는 `geometry_msgs/Point`를 사용 가능
#
# x = center_x
# y = center_y
# z = area 또는 검출 여부 보조값
#
# 정식 프로젝트에서는 커스텀 메시지를 권장하지만, 입문 실습에서는 `Point`가 이해하기 쉽습니다.
#
# [실습 목표]
# 1. 색상 객체 중심점 계산
# 2. geometry_msgs/Point 발행
# 3. 중심 좌표와 면적을 Topic으로 전달
# 4. 로봇 제어 노드와 연결할 준비
#
# [실무에서 자주 하는 실수]
# 실수 1. 검출 실패 시 이전 좌표를 계속 사용
#
# 객체가 사라졌는데 이전 좌표를 계속 쓰면 로봇이 잘못 움직일 수 있음
#
# 검출 실패 상태를 따로 발행하는 것이 좋습니다.
#
# 실수 2. Point.z에 면적을 넣고 의미를 문서화하지 않음
#
# 실습에서는 편하지만 협업에서는 혼란을 줍니다.
#
# 정식 메시지는 다음처럼 만드는 것이 좋습니다.
#
# bool detected
# float64 center_x
# float64 center_y
# float64 area
#
# [ROS2와 연결되는 포인트]
# 이 Topic은 다음 제어 노드가 구독할 수 있음
#
# /vision/target_center
# → 로봇 주행 제어 노드
# → 화면 중앙과 target x 비교
# → /cmd_vel 발행
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
class TargetCenterPublisher(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드임
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정함
        super().__init__("target_center_publisher")

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
        self.center_pub = self.create_publisher(
            Point,
            "/vision/target_center",
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

            # target 변수에 이후 처리에 사용할 값을 저장
            target = self.detect_blue_target(frame)

            # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
            if target is not None:
                center_x, center_y, area = target

                # point msg 변수에 이후 처리에 사용할 값을 저장
                point_msg = Point()
                point_msg.x = float(center_x)
                point_msg.y = float(center_y)
                point_msg.z = float(area)

                # 완성한 ROS2 메시지를 지정한 Topic으로 발행
                self.center_pub.publish(point_msg)

                # 정상 진행 상태를 ROS2 로그에 출력
                self.get_logger().info(
                    f"target center: x={center_x}, y={center_y}, area={area}"
                )

        # 위의 처리 과정에서 오류가 발생했을 때 실행할 코드를 작성함
        except Exception as e:
            # 오류 내용을 ROS2 로그에 출력
            self.get_logger().error(f"객체 중심 처리 오류: {e}")

    # detect_blue_target 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def detect_blue_target(self, frame):
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

        # 검출되거나 매칭된 항목의 개수를 확인
        if len(contours) == 0:
            # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
            return None

        # 윤곽선이 차지하는 픽셀 면적을 계산
        largest_contour = max(contours, key=cv2.contourArea)

        # 윤곽선이 차지하는 픽셀 면적을 계산
        area = cv2.contourArea(largest_contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if area < 500:
            # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
            return None

        # 윤곽선의 면적과 중심점을 계산하는 데 필요한 모멘트 값을 구함
        moments = cv2.moments(largest_contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if moments["m00"] == 0:
            # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
            return None

        # center x 값을 계산하거나 저장해 이후 처리에서 사용
        center_x = int(moments["m10"] / moments["m00"])
        # center y 값을 계산하거나 저장해 이후 처리에서 사용
        center_y = int(moments["m01"] / moments["m00"])

        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
        return center_x, center_y, area

# 프로그램 실행 순서를 담당하는 main 함수를 정의함
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장
    node = TargetCenterPublisher()

    # 노드가 종료될 때까지 콜백을 계속 처리하도록 실행 상태를 유지
    rclpy.spin(node)

    # 사용이 끝난 ROS2 노드 자원을 정리함
    node.destroy_node()
    # ROS2 사용을 종료하고 관련 자원을 정리함
    rclpy.shutdown()

# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인
if __name__ == "__main__":
    main()
