import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class RandomSubscriber(Node):
    def __init__(self):
        super().__init__('random_subcribers')
        self.subscription = self.create_subscription(
            Int32,
            'random_number',
            self.listener_callback,
            10
        )
    def listener_callback(self, msg):
        if msg.data > 50:
            self.get_logger().info(f'Big number: {msg.data}')
        if msg.data < 50:
            self.get_logger().info(f'Small number: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = RandomSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ =='__main__':
    main()


