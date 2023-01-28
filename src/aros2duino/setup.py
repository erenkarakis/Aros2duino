from setuptools import setup

package_name = 'aros2duino'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Taha Eren Karakis',
    maintainer_email='tekkarakis@gmail.com',
    description='Package for read and publish serial communication data to ROS2 system.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "serial_comm = aros2duino.serial_comm:main",
            "find_ports = aros2duino.find_ports:main",
            "test_writing = aros2duino.test_writing:main"
        ],
    },
)
