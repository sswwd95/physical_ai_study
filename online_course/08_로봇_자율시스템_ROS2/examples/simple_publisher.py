"""ROS2 std_msgs/String publisher example.

Run in a ROS2 environment after creating a package that depends on rclpy and std_msgs.
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.publisher = self.create_publisher(String, "study_topic", 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f"hello {self.count}"
        self.publisher.publish(msg)
        self.get_logger().info(msg.data)
        self.count += 1


def main():
    rclpy.init()
    node = SimplePublisher()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
