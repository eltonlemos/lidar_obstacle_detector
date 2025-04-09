from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    pkg_dir = get_package_share_directory('lidar_obstacle_detector')
    rviz_config_path = os.path.join(pkg_dir, 'rviz', 'lidar_obstacle_detector.rviz')

    return LaunchDescription([
        # Declare optional argument for loading parameters
        DeclareLaunchArgument(
            'params_file',
            default_value=os.path.join(pkg_dir, 'config', 'params.yaml'),
            description='Path to the parameter file.'
        ),

        # Main lidar obstacle detector node
        Node(
            package='lidar_obstacle_detector',
            executable='obstacle_detector_node',
            name='obstacle_detector',
            output='screen',
            parameters=[LaunchConfiguration('params_file')],
            remappings=[
                # Add your remaps here
                # ('/input_scan', '/scan_filtered')
            ]
        ),

        # RViz2 visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]  # fallback to default if not present
        ),

    ])

