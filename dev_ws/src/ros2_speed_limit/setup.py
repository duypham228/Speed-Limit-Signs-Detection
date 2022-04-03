from setuptools import setup

package_name = 'ros2_speed_limit'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bao Vo',
    maintainer_email='vo789@tamu.edu',
    description='Speedlimit Sign Classification Package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_file = ros2_speed_limit.image_file_pub:main',
            'classifier = ros2_speed_limit.classifier:main',
            'listener = ros2_speed_limit.image_input_sub:main',
        ],
    },
)
