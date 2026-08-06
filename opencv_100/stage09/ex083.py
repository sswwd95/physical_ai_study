"""예제 83. OpenCV 이미지를 ROS2 메시지로 변환

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class OpenCVImagePublisher(Node):
    def __init__(self):
        super().__init__("opencv_image_publisher")

        self.publisher = self.create_publisher(
            Image,
            "/opencv/image",
            10
        )

        self.bridge = CvBridge()

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        self.image = cv2.imread("practice_images/sample.jpg")

    def timer_callback(self):
        if self.image is None:
            self.get_logger().error("이미지를 읽을 수 없습니다.")
            return

        msg = self.bridge.cv2_to_imgmsg(
            self.image,
            encoding="bgr8"
        )

        self.publisher.publish(msg)

        self.get_logger().info("OpenCV 이미지를 ROS2 Image로 발행했습니다.")

def main(args=None):
    rclpy.init(args=args)

    node = OpenCVImagePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
