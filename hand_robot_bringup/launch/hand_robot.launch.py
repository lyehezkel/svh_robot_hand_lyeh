import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import xacro


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'schunk_svh_description'
    file_subpath = 'urdf/svh-standalone.urdf.xacro'
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'urdf/svh-standalone.urdf.xacro'

    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # Configure the nodes
    node_rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', os.path.join(get_package_share_directory(pkg_name), 'rviz', 'hand_robot_default.rviz')] # replace 'hand_robot_defualt.rviz' with next RViz2 config file name
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description',
                    '-entity', 'svh_gazebo',
                    '-file' , os.path.join(get_package_share_directory(pkg_name), 'urdf', 'svh.gazebo.xacro')],
        output='screen'
    )

    joint_state_publisher = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw,
        'use_sim_time': True}] # add other parameters here if required
    )

    requested_gestures_publisher = Node(
        package='my_py_pkg',
        executable='requested_gestures',
        output='screen'
    )
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
        )

    # Run the nodes in the desired order
    return LaunchDescription([
        node_rviz2,
        spawn_entity,
        joint_state_publisher,
        node_robot_state_publisher,
        requested_gestures_publisher,
        gazebo
    ])