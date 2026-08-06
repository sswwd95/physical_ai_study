# ============================================================================
# 노션 원문 학습 설명: 예제 86. 이미지 Subscriber 구조
# ============================================================================
#
# [핵심 주제]
# 카메라 Topic을 구독하고 OpenCV로 변환한 뒤, 처리 함수로 넘기는 기본 구조를 생성
#
# 이번 예제는 아직 복잡한 검출을 하지 않고, 구조를 안정적으로 잡는 데 집중함
#
# [실습 목표]
# 1. ROS2 Image Subscriber 작성
# 2. cv_bridge 변환
# 3. process_frame() 함수 분리
# 4. OpenCV 결과 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. 예외 처리를 하지 않음
#
# 카메라 메시지 변환 중 오류가 나면 노드가 종료될 수 있음
#
# 실무 노드에서는 최소한 콜백 내부에 예외 처리를 넣는 것이 좋습니다.
#
# 실수 2. 흑백 이미지를 그대로 컬러 그리기 함수에 사용
#
# 흑백 이미지에 컬러 텍스트나 박스를 그리면 기대와 다를 수 있음
#
# 결과 시각화가 필요하면 다시 BGR로 변환하는 것이 좋습니다.
#
# [ROS2와 연결되는 포인트]
# 이 구조를 기반으로 이후 Edge Publisher, 객체 중심 Publisher를 만들 수 있음
# ============================================================================
# Python으로 ROS2 노드를 만들고 실행하기 위해 rclpy를 불러오기
import rclpy
# ROS2 노드 클래스를 만들 때 상속할 Node를 불러오기
from rclpy.node import Node
# ROS2에서 카메라 영상을 주고받는 Image 메시지 형식을 불러오기
from sensor_msgs.msg import Image
# ROS2 Image 메시지와 OpenCV 이미지 배열을 서로 변환하는 CvBridge를 불러오기
from cv_bridge import CvBridge
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 관련 기능과 데이터를 하나로 묶는 클래스를 정의함
class BasicVisionSubscriber(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드임
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정함
        super().__init__("basic_vision_subscriber")

        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 생성
        self.bridge = CvBridge()

        # 다른 ROS2 노드가 보낸 메시지를 받을 Subscriber를 생성
        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
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

            # processed frame 변수에 이후 처리에 사용할 값을 저장
            processed_frame = self.process_frame(frame)

            # 처리 결과 확인용 OpenCV 창 표시
            cv2.imshow("Processed Frame", processed_frame)
            # 키 입력 대기 및 실시간 영상 갱신
            cv2.waitKey(1)

        # 위의 처리 과정에서 오류가 발생했을 때 실행할 코드를 작성함
        except Exception as e:
            # 오류 내용을 ROS2 로그에 출력
            self.get_logger().error(f"이미지 처리 오류: {e}")

    # process_frame 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def process_frame(self, frame):
        # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 이미지를 필요한 색상 공간으로 변환
        processed_frame = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )

        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
        return processed_frame

# 프로그램 실행 순서를 담당하는 main 함수를 정의함
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장
    node = BasicVisionSubscriber()

    # 노드가 종료될 때까지 콜백을 계속 처리하도록 실행 상태를 유지
    rclpy.spin(node)

    # 사용이 끝난 ROS2 노드 자원을 정리함
    node.destroy_node()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
    # ROS2 사용을 종료하고 관련 자원을 정리함
    rclpy.shutdown()

# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인
if __name__ == "__main__":
    main()
