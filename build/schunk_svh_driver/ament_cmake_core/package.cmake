set(_AMENT_PACKAGE_NAME "schunk_svh_driver")
set(schunk_svh_driver_VERSION "2.0.1")
set(schunk_svh_driver_MAINTAINER "Stefan Scherzinger <scherzin@fzi.de>")
set(schunk_svh_driver_BUILD_DEPENDS "hardware_interface" "pluginlib" "rclcpp" "schunk_svh_library")
set(schunk_svh_driver_BUILDTOOL_DEPENDS "ament_cmake")
set(schunk_svh_driver_BUILD_EXPORT_DEPENDS "hardware_interface" "pluginlib" "rclcpp" "schunk_svh_library")
set(schunk_svh_driver_BUILDTOOL_EXPORT_DEPENDS )
set(schunk_svh_driver_EXEC_DEPENDS "schunk_svh_description" "controller_manager" "joint_state_controller" "joint_trajectory_controller" "launch" "launch_ros" "ros2launch" "xacro" "hardware_interface" "pluginlib" "rclcpp" "schunk_svh_library")
set(schunk_svh_driver_TEST_DEPENDS "ament_lint_auto")
set(schunk_svh_driver_GROUP_DEPENDS )
set(schunk_svh_driver_MEMBER_OF_GROUPS )
set(schunk_svh_driver_DEPRECATED "")
set(schunk_svh_driver_EXPORT_TAGS)
list(APPEND schunk_svh_driver_EXPORT_TAGS "<build_type>ament_cmake</build_type>")
