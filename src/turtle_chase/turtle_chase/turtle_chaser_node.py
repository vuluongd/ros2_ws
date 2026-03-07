import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class TurtleFollower(Node):

    def __init__(self):
        super().__init__('turtle_follower')

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
        
        dx = self.leader_pose.x - msg.x
        dy = self.leader_pose.y - msg.y

        distance = math.sqrt(dx*dx + dy*dy)
        angle = math.atan2(dy, dx)

        angle_error = angle - msg.theta
        angle_error = math.atan2(math.sin(angle_error),math.cos(angle_error))

        cmd = Twist()
        if abs(angle_error) > 0.3:
            cmd.linear.x = 0.0
            cmd.angular.z = 4*angle_error
        else:
            cmd.linear.x = 1.5*distance
            cmd.angular.z = 4*angle_error

        self.publisher_.publish(cmd)

def main():
    rclpy.init()
    node = TurtleFollower()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()




    

    