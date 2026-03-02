import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenSubscribers(Node):

    def __init__(self):
        super().__init__('even_subscribers')

        self.subscription = self.create_subscription(
            Int32,
            'random_number',
            self.callback,
            10
        )

    def callback(self, msg):
        if msg.data %2 == 0:
            self.get_logger().info(f'Even number: {msg.data}')

def main(args = None):
    rclpy.init(args = args)
    node = EvenSubscribers()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

        