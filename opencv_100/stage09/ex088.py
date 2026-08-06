"""예제 88. 객체 중심 좌표 Publisher

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
import cv2
import numpy as np

class TargetCenterPublisher(Node):
    def __init__(self):
        super().__init__("target_center_publisher")

        self.bridge = CvBridge()

        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        self.center_pub = self.create_publisher(
            Point,
            "/vision/target_center",
            10
        )

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            target = self.detect_blue_target(frame)

            if target is not None:
                center_x, center_y, area = target

                point_msg = Point()
                point_msg.x = float(center_x)
                point_msg.y = float(center_y)
                point_msg.z = float(area)

                self.center_pub.publish(point_msg)

                self.get_logger().info(
                    f"target center: x={center_x}, y={center_y}, area={area}"
                )

        except Exception as e:
            self.get_logger().error(f"객체 중심 처리 오류: {e}")

    def detect_blue_target(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100, 100, 100])
        upper_blue = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        kernel = np.ones((5, 5), np.uint8)

        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if len(contours) == 0:
            return None

        largest_contour = max(contours, key=cv2.contourArea)

        area = cv2.contourArea(largest_contour)

        if area < 500:
            return None

        moments = cv2.moments(largest_contour)

        if moments["m00"] == 0:
            return None

        center_x = int(moments["m10"] / moments["m00"])
        center_y = int(moments["m01"] / moments["m00"])

        return center_x, center_y, area

def main(args=None):
    rclpy.init(args=args)

    node = TargetCenterPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
