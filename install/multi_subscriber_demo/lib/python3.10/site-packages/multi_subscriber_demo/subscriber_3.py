import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class AvgSubscribers(Node):

    def __init__(self):
        super().__init__('average_numbers')

        self.subscription = self.create_subscription(
            Int32,
            'random_number',
            self.callback,
            10
        )

        self.values = []

    def callback(self, msg):
        self.values.append(msg.data)

        if len(self.values) > 10:
            self.values.pop(0)

        average = sum(self.values)/len(self.values)
        self.get_logger().info(f'Average (last {len(self.values)}): {average:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = AvgSubscribers()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

