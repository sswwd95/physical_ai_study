# ============================================================================
# 노션 원문 학습 설명: 예제 84. ROS2 Image 메시지를 OpenCV로 변환
# ============================================================================
#
# [핵심 주제]
# ROS2 카메라 Topic을 구독하고, 수신한 Image 메시지를 OpenCV 이미지로 변환
#
# 이 구조가 ROS2 비전 노드의 기본임
#
# [실습 목표]
# 1. ROS2 Image Subscriber 생성
# 2. imgmsg_to_cv2() 사용법 이해
# 3. OpenCV 화면 출력
# 4. 카메라 Topic 처리 구조 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. Topic 이름이 다름
#
# 카메라 Topic 이름은 환경에 따라 다를 수 있음
#
# 먼저 다음 명령으로 확인
#
# ros2 topic list
#
# 그리고 Image Topic 정보를 확인
#
# ros2 topic info /camera/image_raw
#
# 실수 2. cv2.waitKey(1)을 빼먹음
#
# `cv2.imshow()`를 사용하면 `cv2.waitKey(1)`이 필요합니다.
#
# 없으면 창이 갱신되지 않거나 멈춘 것처럼 보일 수 있음
#
# [ROS2와 연결되는 포인트]
# 이 예제는 앞으로 만들 모든 ROS2 OpenCV 노드의 출발점임
#
# Image Subscribe
# → cv_bridge 변환
# → OpenCV 처리
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
class ImageSubscriber(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드임
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정함
        super().__init__("image_subscriber")

        # 다른 ROS2 노드가 보낸 메시지를 받을 Subscriber를 생성
        self.subscription = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 생성
        self.bridge = CvBridge()

    # image_callback 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def image_callback(self, msg):
        # 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환
        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding="bgr8"
        )

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("ROS2 Camera Image", frame)
        # 키 입력 대기 및 실시간 영상 갱신
        cv2.waitKey(1)

# 프로그램 실행 순서를 담당하는 main 함수를 정의함
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장
    node = ImageSubscriber()

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
