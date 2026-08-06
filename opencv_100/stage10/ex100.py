"""예제 100. ROS2 비전 프로젝트 통합 구조

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from std_msgs.msg import Bool
from cv_bridge import CvBridge
import cv2
import numpy as np

class IntegratedVisionNode(Node):
    def __init__(self):
        super().__init__("integrated_vision_node")

        self.bridge = CvBridge()

        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        self.debug_image_pub = self.create_publisher(
            Image,
            "/vision/debug_image",
            10
        )

        self.target_pub = self.create_publisher(
            Point,
            "/vision/target_center",
            10
        )

        self.detected_pub = self.create_publisher(
            Bool,
            "/vision/target_detected",
            10
        )

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            debug_frame, detection = self.detect_blue_target(frame)

            detected_msg = Bool()
            detected_msg.data = detection is not None
            self.detected_pub.publish(detected_msg)

            if detection is not None:
                point_msg = Point()
                point_msg.x = float(detection["center_x"])
                point_msg.y = float(detection["center_y"])
                point_msg.z = float(detection["area"])

                self.target_pub.publish(point_msg)

            debug_msg = self.bridge.cv2_to_imgmsg(
                debug_frame,
                encoding="bgr8"
            )
            debug_msg.header = msg.header

            self.debug_image_pub.publish(debug_msg)

        except Exception as e:
            self.get_logger().error(f"통합 비전 처리 오류: {e}")

    def detect_blue_target(self, frame):
        debug_frame = frame.copy()

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

        height, width = frame.shape[:2]
        image_center_x = width // 2

        cv2.line(
            debug_frame,
            (image_center_x, 0),
            (image_center_x, height),
            (255, 0, 0),
            2
        )

        if len(contours) == 0:
            cv2.putText(
                debug_frame,
                "Target Not Found",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )
            return debug_frame, None

        largest_contour = max(contours, key=cv2.contourArea)

        area = cv2.contourArea(largest_contour)

        if area < 500:
            return debug_frame, None

        moments = cv2.moments(largest_contour)

        if moments["m00"] == 0:
            return debug_frame, None

        center_x = int(moments["m10"] / moments["m00"])
        center_y = int(moments["m01"] / moments["m00"])

        error_x = center_x - image_center_x

        cv2.drawContours(
            debug_frame,
            [largest_contour],
            -1,
            (0, 255, 0),
            2
        )

        cv2.circle(
            debug_frame,
            (center_x, center_y),
            8,
            (0, 0, 255),
            -1
        )

        cv2.putText(
            debug_frame,
            f"center=({center_x},{center_y}) area={int(area)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        cv2.putText(
            debug_frame,
            f"error_x={error_x}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        detection = {
            "center_x": center_x,
            "center_y": center_y,
            "area": area,
            "error_x": error_x
        }

        return debug_frame, detection

def main(args=None):
    rclpy.init(args=args)

    node = IntegratedVisionNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
