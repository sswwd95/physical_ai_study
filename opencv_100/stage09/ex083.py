"""예제 83. OpenCV 이미지를 ROS2 메시지로 변환

초보자용 상세 주석판입니다.

읽는 순서:
1. 위에서 아래로 주석을 먼저 읽습니다.
2. 바로 아래 코드가 어떤 작업을 하는지 확인합니다.
3. 실행 후 나타나는 창이나 터미널 결과를 비교합니다.

실행 위치: 이 프로젝트의 opencv_100 폴더
주의: cv2.imshow()가 있는 예제는 화면 창에서 아무 키나 눌러야 종료됩니다.
"""

# Python으로 ROS2 노드를 만들고 실행하기 위해 rclpy를 불러옵니다.
import rclpy
# ROS2 노드 클래스를 만들 때 상속할 Node를 불러옵니다.
from rclpy.node import Node
# ROS2에서 카메라 영상을 주고받는 Image 메시지 형식을 불러옵니다.
from sensor_msgs.msg import Image
# ROS2 Image 메시지와 OpenCV 이미지 배열을 서로 변환하는 CvBridge를 불러옵니다.
from cv_bridge import CvBridge
# OpenCV 기능을 사용하기 위해 cv2 모듈을 불러옵니다.
import cv2

# 관련 기능과 데이터를 하나로 묶는 클래스를 정의합니다.
class OpenCVImagePublisher(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드입니다.
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정합니다.
        super().__init__("opencv_image_publisher")

        # 처리 결과를 다른 ROS2 노드에 보낼 Publisher를 만듭니다.
        self.publisher = self.create_publisher(
            Image,
            "/opencv/image",
            10
        )

        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 만듭니다.
        self.bridge = CvBridge()

        # 정해진 시간 간격마다 콜백 함수를 실행하는 타이머를 만듭니다.
        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        # 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
        self.image = cv2.imread("practice_images/sample.jpg")

    # timer_callback 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
    def timer_callback(self):
        # 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
        if self.image is None:
            # 오류 내용을 ROS2 로그에 출력합니다.
            self.get_logger().error("이미지를 읽을 수 없습니다.")
            # 현재 함수를 여기서 종료합니다.
            return

        # OpenCV 이미지 배열을 ROS2 Image 메시지로 변환합니다.
        msg = self.bridge.cv2_to_imgmsg(
            self.image,
            encoding="bgr8"
        )

        # 완성한 ROS2 메시지를 지정한 Topic으로 발행합니다.
        self.publisher.publish(msg)

        # 정상 진행 상태를 ROS2 로그에 출력합니다.
        self.get_logger().info("OpenCV 이미지를 ROS2 Image로 발행했습니다.")

# 프로그램 실행 순서를 담당하는 main 함수를 정의합니다.
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화합니다.
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장합니다.
    node = OpenCVImagePublisher()

    # 노드가 종료될 때까지 콜백을 계속 처리하도록 실행 상태를 유지합니다.
    rclpy.spin(node)

    # 사용이 끝난 ROS2 노드 자원을 정리합니다.
    node.destroy_node()
    # ROS2 사용을 종료하고 관련 자원을 정리합니다.
    rclpy.shutdown()

# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인합니다.
if __name__ == "__main__":
    main()
