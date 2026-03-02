import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class publisher(Node):

    def __init__(self):
        super.__init__('publisher')

        self.publisher_ = self.create_publisher(
            Int32, 
            'random number',
            10
        )

        self.timer = self.create_timer (
            1.0,
            self.publish_number
        )
    def publish_number(self):
        msg = Int32()
        msg.data = random.randint(0, 100)
        self.publisher_publish(msg)
        self.get_logger().info('Published {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = publisher()
    rclpy.spin(Node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



