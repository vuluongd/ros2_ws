import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class AvgNumbers(Node):

    def __init__(self):
        super.__init__('Average Numbers')
