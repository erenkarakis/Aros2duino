import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Test_Writing(Node):
    def __init__(self):
        super().__init__("test_writing")
        self.counter = 0
        self.data_publisher_ = self.create_publisher(String, "test_writing", 1)
        self.timer_ = self.create_timer(0.10, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = "A" + str(self.counter) + "\n"
        self.get_logger().info(msg.data+ str(self.counter))
        self.counter += 1
        self.data_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = Test_Writing()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()