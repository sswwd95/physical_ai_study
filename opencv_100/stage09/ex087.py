"""예제 87. 실시간 Edge Publisher

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class EdgePublisher(Node):
    def __init__(self):
        super().__init__("edge_publisher")

        self.bridge = CvBridge()

        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        self.edge_pub = self.create_publisher(
            Image,
            "/vision/edge_image",
            10
        )

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            edge_image = self.process_frame(frame)

            edge_msg = self.bridge.cv2_to_imgmsg(
                edge_image,
                encoding="mono8"
            )

            edge_msg.header = msg.header

            self.edge_pub.publish(edge_msg)

        except Exception as e:
            self.get_logger().error(f"Edge 처리 오류: {e}")

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blurred, 50, 150)

        return edges

def main(args=None):
    rclpy.init(args=args)

    node = EdgePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
