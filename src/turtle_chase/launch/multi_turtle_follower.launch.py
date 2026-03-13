from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('turtle_chase'),
        'config',
        'pid_params.yaml'
    )
    return LaunchDescription([

        #khởi động turtlesim
        Node(
            package = 'turtlesim',
            executable = 'turtlesim_node',
            output = 'screen'
        ),
        #thêm 1 turtle
        ExecuteProcess(
            cmd = [
                'ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn',
                '{x: 3.0, y: 3.0, theta: 0.0, name: "turtle2"}',

            ],
            output = 'screen'
        ),
        ExecuteProcess(
            cmd = [
                'ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn', 
                '{x: 4.0, y: 4.0, theta: 0.0, name: "turtle3"}',
            ],
            output = 'screen'
        ),

        ExecuteProcess(
            cmd = [
                'ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn',
                '{x: 6.0, y: 6.0, theta: 0.0, name: "turtle4"}',
            ],
        ),
        # chạy node turtle_leader_follower với parameter từ yaml
        Node(
            package = 'turtle_chase',
            executable = 'multi_turtle_follower',
            name = 'turtle1',
            output = 'screen',
            parameters = [config,{"leader": "turtle1", "follower": "turtle2"}]
        ),
        Node(
            package = 'turtle_chase',
            executable = 'multi_turtle_follower',
            output = 'screen',
            name = 'turtle2',
            parameters = [config, {"leader": "turtle2", "follower": "turtle3"}]
        ),
        Node(
            package = 'turtle_chase',
            executable = 'multi_turtle_follower',
            output = 'screen',
            name = 'turtle3',
            parameters = [config, {"leader": "turtle3", "follower": "turtle4"}]
        )

    ])


