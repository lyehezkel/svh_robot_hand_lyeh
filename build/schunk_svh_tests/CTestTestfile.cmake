# CMake generated Testfile for 
# Source directory: /home/lab-pc/robot_hand_ws/src/schunk_svh_ros_driver/schunk_svh_tests
# Build directory: /home/lab-pc/robot_hand_ws/build/schunk_svh_tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(integration_tests_test_startup.py "/usr/bin/python3" "-u" "/opt/ros/foxy/share/ament_cmake_test/cmake/run_test.py" "/home/lab-pc/robot_hand_ws/build/schunk_svh_tests/test_results/schunk_svh_tests/integration_tests_test_startup.py.xunit.xml" "--package-name" "schunk_svh_tests" "--output-file" "/home/lab-pc/robot_hand_ws/build/schunk_svh_tests/launch_test/CHANGEME.txt" "--command" "/usr/bin/python3" "-m" "launch_testing.launch_test" "/home/lab-pc/robot_hand_ws/src/schunk_svh_ros_driver/schunk_svh_tests/integration_tests/test_startup.py" "--junit-xml=/home/lab-pc/robot_hand_ws/build/schunk_svh_tests/test_results/schunk_svh_tests/integration_tests_test_startup.py.xunit.xml" "--package-name=schunk_svh_tests")
set_tests_properties(integration_tests_test_startup.py PROPERTIES  TIMEOUT "60" WORKING_DIRECTORY "/home/lab-pc/robot_hand_ws/build/schunk_svh_tests" _BACKTRACE_TRIPLES "/opt/ros/foxy/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/opt/ros/foxy/share/launch_testing_ament_cmake/cmake/add_launch_test.cmake;125;ament_add_test;/home/lab-pc/robot_hand_ws/src/schunk_svh_ros_driver/schunk_svh_tests/CMakeLists.txt;11;add_launch_test;/home/lab-pc/robot_hand_ws/src/schunk_svh_ros_driver/schunk_svh_tests/CMakeLists.txt;0;")
