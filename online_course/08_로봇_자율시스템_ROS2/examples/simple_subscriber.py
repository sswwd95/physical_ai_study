"""ROS2 std_msgs/String subscriber example."""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        self.subscription = self.create_subscription(
            String, "study_topic", self.on_message, 10
        )

    def on_message(self, msg: String):
        self.get_logger().info(f"received: {msg.data}")


def main():
    rclpy.init()
    node = SimpleSubscriber()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
