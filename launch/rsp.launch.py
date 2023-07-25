import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro


def generate_launch_description():

    # Check if we're told to use sim time
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Process the URDF file one (1st ugv)
    pkg_path = os.path.join(get_package_share_directory('articubot_one'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config = Command(['xacro ', xacro_file, ' sim_mode:=', use_sim_time])
    
    # Process the URDF file two (2nd ugv)
    xacro_file_one = os.path.join(pkg_path,'description','robot_one.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config_one = Command(['xacro ', xacro_file_one, ' sim_mode:=', use_sim_time])
    
    # Process the URDF file three (3rd ugv)
    xacro_file_two = os.path.join(pkg_path,'description','robot_two.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config_two = Command(['xacro ', xacro_file_two, ' sim_mode:=', use_sim_time])
    
    # Process the URDF file four (4th ugv)
    xacro_file_three = os.path.join(pkg_path,'description','robot_three.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config_three = Command(['xacro ', xacro_file_three, ' sim_mode:=', use_sim_time])
    
    # Process the URDF file five (5th ugv)
    xacro_file_four = os.path.join(pkg_path,'description','robot_four.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config_four = Command(['xacro ', xacro_file_four, ' sim_mode:=', use_sim_time])
    
    # Process the URDF file for uav_station
    xacro_file_uav_station = os.path.join(pkg_path,'description','uav_station.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config_uav_station = Command(['xacro ', xacro_file_uav_station, ' sim_mode:=', use_sim_time])
    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )
    
    # Creating a robot_state_publisher node for UGV2
    params_one = {'robot_description': robot_description_config_one, 'use_sim_time': use_sim_time}
    node_robot_state_publisher_one = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params_one],
        remappings=[
        	("robot_description", "robot_description_one")
        ]
     )
     
    # Creating a robot_state_publisher node for UGV3
    params_two = {'robot_description': robot_description_config_two, 'use_sim_time': use_sim_time}
    node_robot_state_publisher_two = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params_two],
        remappings=[
        	("robot_description", "robot_description_two")
        ]
     )
     
    # Creating a robot_state_publisher node for UGV4
    params_three = {'robot_description': robot_description_config_three, 'use_sim_time': use_sim_time}
    node_robot_state_publisher_three = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params_three],
        remappings=[
        	("robot_description", "robot_description_three")
        ]
     )
    
    # Creating a robot_state_publisher node for UGV5
    params_four = {'robot_description': robot_description_config_four, 'use_sim_time': use_sim_time}
    node_robot_state_publisher_four = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params_four],
        remappings=[
        	("robot_description", "robot_description_four")
        ]
     )
    
    # Creating a robot_state_publisher node for the uav_station
    params_uav_station = {'robot_description': robot_description_config_uav_station, 'use_sim_time': use_sim_time}
    node_uav_station_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params_uav_station],
        remappings=[
        	("robot_description", "uav_station_description")
        ]
     )
     
    


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        node_robot_state_publisher,
        node_robot_state_publisher_one,
        node_robot_state_publisher_two,
        node_robot_state_publisher_three,
        node_robot_state_publisher_four,
        node_uav_station_state_publisher
    ])
