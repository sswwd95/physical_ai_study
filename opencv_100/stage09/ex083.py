# ============================================================================
# 노션 원문 학습 설명: 예제 83. OpenCV 이미지를 ROS2 메시지로 변환
# ============================================================================
#
# [핵심 주제]
# OpenCV에서 처리한 이미지를 ROS2 Image Topic으로 발행할 수 있도록 메시지로 변환
#
# 예를 들어 다음 이미지를 ROS2로 보낼 수 있음
#
# 원본 카메라 이미지
# Edge 결과 이미지
# 색상 마스크 이미지
# 객체 박스가 그려진 이미지
#
# [실습 목표]
# 1. cv2_to_imgmsg() 사용법 이해
# 2. OpenCV 이미지 encoding 설정
# 3. ROS2 Image Publisher 구조 이해
# 4. 처리 결과 이미지를 Topic으로 발행하는 개념 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. encoding을 잘못 설정
#
# 흑백 이미지를 발행하면서 `bgr8`로 설정하면 문제가 생길 수 있음
#
# 흑백 이미지는 보통 다음처럼 발행
#
# msg = bridge.cv2_to_imgmsg(gray_image, encoding="mono8")
#
# 컬러 이미지는 보통 다음임
#
# msg = bridge.cv2_to_imgmsg(color_image, encoding="bgr8")
#
# 실수 2. 이미지 경로를 ROS2 실행 위치 기준으로 잘못 작성
#
# ROS2 패키지에서 실행할 때 현재 작업 디렉토리가 예상과 다를 수 있음
#
# 실무에서는 패키지 경로를 기준으로 이미지 파일을 찾는 구조를 쓰는 것이 좋습니다.
#
# [ROS2와 연결되는 포인트]
# 이 예제는 OpenCV 처리 결과를 RViz2나 `rqt_image_view`에서 확인할 때 필요
#
# OpenCV 처리 결과
# → cv2_to_imgmsg()
# → /processed_image Publish
# → rqt_image_view에서 확인
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
class OpenCVImagePublisher(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드임
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정함
        super().__init__("opencv_image_publisher")

        # 처리 결과를 다른 ROS2 노드에 보낼 Publisher를 생성
        self.publisher = self.create_publisher(
            Image,
            "/opencv/image",
            10
        )

        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 생성
        self.bridge = CvBridge()

        # 정해진 시간 간격마다 콜백 함수를 실행하는 타이머를 생성
        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        # 지정 경로의 이미지 읽기 및 NumPy 배열 저장
        self.image = cv2.imread("practice_images/sample.jpg")

    # timer_callback 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def timer_callback(self):
        # 이미지 또는 검출 결과 생성 여부 확인
        if self.image is None:
            # 오류 내용을 ROS2 로그에 출력
            self.get_logger().error("이미지를 읽을 수 없습니다.")
            # 현재 함수를 여기서 종료
            return

        # OpenCV 이미지 배열을 ROS2 Image 메시지로 변환
        msg = self.bridge.cv2_to_imgmsg(
            self.image,
            encoding="bgr8"
        )

        # 완성한 ROS2 메시지를 지정한 Topic으로 발행
        self.publisher.publish(msg)

        # 정상 진행 상태를 ROS2 로그에 출력
        self.get_logger().info("OpenCV 이미지를 ROS2 Image로 발행했습니다.")

# 프로그램 실행 순서를 담당하는 main 함수를 정의함
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장
    node = OpenCVImagePublisher()

    # 노드가 종료될 때까지 콜백을 계속 처리하도록 실행 상태를 유지
    rclpy.spin(node)

    # 사용이 끝난 ROS2 노드 자원을 정리함
    node.destroy_node()
    # ROS2 사용을 종료하고 관련 자원을 정리함
    rclpy.shutdown()

# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인
if __name__ == "__main__":
    main()
