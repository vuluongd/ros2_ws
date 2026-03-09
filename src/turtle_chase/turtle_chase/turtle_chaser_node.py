import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class TurtleFollower(Node):

    def __init__(self):
        super().__init__('turtle_follower')
        #các biến của bộ điều khiển pid
        self.prev_distance_error = 0.0
        self.integral_distance = 0.0

        self.prev_angle_error = 0.0
        self.integral_angle = 0.0
        
        self.prev_time = self.get_clock().now()

        #ROS 2 parameter
        self.declare_parameter("desired_distance", 1.0)
        self.declare_parameter("max_linear_speed", 2.0)
        self.declare_parameter("kp_linear", 1.5)
        self.declare_parameter("ki_linear", 0.1)
        self.declare_parameter("kd_linear", 0.2)
        self.declare_parameter("kp_angular", 4.0)
        self.declare_parameter("ki_angular", 0.05)
        self.declare_parameter("kd_angular", 0.3)
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
        current_time = self.get_clock().now()
        dt = (current_time - self.prev_time).nanoseconds/1e9
        self.prev_time = current_time

        if dt == 0:
            return
        
        if self.leader_pose is None:
            return
        
        desired_distance = self.get_parameter("desired_distance").value
        max_linear_speed = self.get_parameter("max_linear_speed").value
        kp_linear = self.get_parameter("kp_linear").value
        ki_linear = self.get_parameter("ki_linear").value
        kd_linear = self.get_parameter("kd_linear").value
        kp_angular = self.get_parameter("kp_angular").value
        ki_angular = self.get_parameter("ki_angular").value
        kd_angular = self.get_parameter("kd_angular").value
        angle_threshold = self.get_parameter("angle_threshold").value


        dx = self.leader_pose.x - msg.x
        dy = self.leader_pose.y - msg.y

        distance = math.sqrt(dx*dx + dy*dy)
        
        distance_error = distance - desired_distance

        angle = math.atan2(dy, dx)
        angle_error = angle - msg.theta
        angle_error = math.atan2(math.sin(angle_error),math.cos(angle_error))

        cmd = Twist()
        #PID cho distance
        self.integral_distance += distance_error * dt
        derivative_distance = (distance_error - self.prev_distance_error) / dt

        linear_output = (
            kp_linear*distance_error +
            ki_linear*self.integral_distance +
            kd_linear*derivative_distance
        )

        self.prev_distance_error = distance_error

        #PID cho angle
        self.integral_angle += angle_error * dt
        derivative_angle = (angle_error -self.prev_angle_error)/dt

        angular_output = (
            kp_angular*angle_error +
            ki_angular*self.integral_angle +
            kd_angular*derivative_angle
        )
        self.prev_angle_error = angle_error

        
        if abs(angle_error) > angle_threshold:
            cmd.linear.x = 0.0
            cmd.angular.z = angular_output
        else:
            cmd.linear.x = max(0.0, min(max_linear_speed, linear_output))
            cmd.angular.z = angular_output

        self.publisher_.publish(cmd)

def main():
    rclpy.init()
    node = TurtleFollower()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()