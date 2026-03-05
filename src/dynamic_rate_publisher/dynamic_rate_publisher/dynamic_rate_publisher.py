import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from rcl_interfaces.msg import SetParametersResult

class CounterNode(Node):
    def __init__(self):
        super().__init__('my_counter')

        #declare parameter
        self.declare_parameter('publish_rate', 1.0)

        self.publisher_ = self.create_publisher(Int32, 'counter', 10)

        self.count = 0

        #lấy rate ban đầu
        self.publish_rate = self.get_parameter('publish_rate').value

        #tạo timer
        self.timer = self.create_timer(1.0 /self.publish_rate, self.timer_callback)

        #nghe thay đổi của callback
        self.add_on_set_parameters_callback(self.parameter_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.count
        self.publisher._publish(msg)

        self.get_logger().info(f'Publishing: {self.count}')
        self.count += 1

    def parameter_callback(self, params):
        for param in params:
            if param.name == 'publish_rate':
                self.publish_rate = param.value

                self.timer.cancel()

                self.timer = self.create_timer(
                    1.0 / self.publish_rate,
                    self.timer_callback
                )

                self.get_logger().info(
                    f'Updated publish_rate: {self.publish_rate} Hz'
                )
        return SetParametersResult(successful=True)
def main(args=None):
    rclpy.init(args=args)
    node =CounterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
