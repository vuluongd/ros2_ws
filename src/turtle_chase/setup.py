from setuptools import find_packages, setup

package_name = 'turtle_chase'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/turtle_leader_follower.launch.py']),
        ('share/' + package_name + '/launch', ['launch/multi_turtle_follower.launch.py']),
        ('share/' + package_name + '/config', ['config/pid_params.yaml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lunog',
    maintainer_email='vul45845@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'turtle_leader_follower = turtle_chase.turtle_chaser_node:main',
            'multi_turtle_follower = turtle_chase.multi_turtle_follower:main',
        ],
    },
)