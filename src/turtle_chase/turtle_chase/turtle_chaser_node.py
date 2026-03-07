import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class TurtleFollower(Node):

    def __init__(self):
        super().__init__('turtle_follower')
        #ROS 2 parameter
        self.declare_parameter("desired_distance", 1.0)
        self.declare_parameter("max_linear_speed", 2.0)
        self.declare_parameter("kp_linear", 1.5)
        self.declare_parameter("kp_angular", 4.0)
        self.declare_parameter("angle_threshold", 0.3)

        self.leader_pose = None

        self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.leader_callback,
            10
        )

        self.create_subscription(
             Pose,
             '/turtle2/pose',
             self.follower_callback,
             10
         )
        

        self.publisher_= self.create_publisher(
            Twist,
            '/turtle2/cmd_vel',
            10
        )

    def leader_callback(self, msg):
        self.leader_pose = msg
    def follower_callback(self, msg):
        
        if self.leader_pose is None:
            return
        
        desired_distance = self.get_parameter("desired_distance").value
        max_linear_speed = self.get_parameter("max_linear_speed").value
        kp_linear = self.get_parameter("kp_linear").value
        kp_angular = self.get_parameter("kp_angular").value
        angle_threshold = self.get_parameter("angle_threshold").value


        dx = self.leader_pose.x - msg.x
        dy = self.leader_pose.y - msg.y

        distance = math.sqrt(dx*dx + dy*dy)
        
        error_distance = distance - desired_distance

        angle = math.atan2(dy, dx)
        angle_error = angle - msg.theta
        angle_error = math.atan2(math.sin(angle_error),math.cos(angle_error))

        cmd = Twist()
        if abs(angle_error) > angle_threshold:
            cmd.linear.x = 0.0
            cmd.angular.z = kp_angular*angle_error
        else:
            cmd.linear.x = min(max_linear_speed, kp_linear*error_distance)
            cmd.angular.z = kp_angular*angle_error

        self.publisher_.publish(cmd)

def main():
    rclpy.init()
    node = TurtleFollower()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()




    

    