"""예제 86. 이미지 Subscriber 구조

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class BasicVisionSubscriber(Node):
    def __init__(self):
        super().__init__("basic_vision_subscriber")

        self.bridge = CvBridge()

        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            processed_frame = self.process_frame(frame)

            cv2.imshow("Processed Frame", processed_frame)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"이미지 처리 오류: {e}")

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        processed_frame = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )

        return processed_frame

def main(args=None):
    rclpy.init(args=args)

    node = BasicVisionSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
