from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='multi_subscriber_demo',
            executable='publisher',
            name='publisher',
            output='screen'
        ),
        Node(
            package='multi_subscriber_demo',
            executable='sub_big',
            name='big_subscriber',
            output='screen'
        ),
        Node(
            package='multi_subscriber_demo',
            executable='sub_even',
            name='even_subscriber',
            output='screen'
        ),
        Node(
            package = 'multi_subscriber_demo',
            executable = 'sub_avg',
            name='avg_subscriber',
            output='screen'
        )

    ])
