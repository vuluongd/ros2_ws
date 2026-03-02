from setuptools import find_packages, setup

package_name = 'multi_subscriber_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/multi_demo.launch.py']),
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
            'publisher = multi_subscriber_demo.random_publisher_1:main',
            'sub_big = multi_subscriber_demo.subscriber_1:main',
            'sub_even = multi_subscriber_demo.subscriber_2:main',
            'sub_avg = multi_subscriber_demo.subscriber_3:main',
        ],
    },
)
