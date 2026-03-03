import rclpy
from rclpy.node import Node

class MyParamNode(Node):
    def __init__(self):
        super().__init__('my_param_node')

        self.declare_parameter('robot_name', 'my_robot')
        self.declare_parameter('speed', 1.0)

        #lấy giá trị
        robot_name = self.get_parameter('robot_name').value
        speed = self.get_parameter('speed').value 

        self.get_logger().info(f'Robot name: {robot_name}')
        self.get_logger().info(f'Speed: {speed}')

def main(args=None):
    rclpy.init(args = args)
    node = MyParamNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



