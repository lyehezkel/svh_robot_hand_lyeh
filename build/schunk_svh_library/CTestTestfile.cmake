# CMake generated Testfile for 
# Source directory: /home/lab-pc/robot_hand_ws/src/schunk_svh_library
# Build directory: /home/lab-pc/robot_hand_ws/build/schunk_svh_library
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_driver_svh "/home/lab-pc/robot_hand_ws/build/schunk_svh_library/test_driver_svh")
set_tests_properties(test_driver_svh PROPERTIES  _BACKTRACE_TRIPLES "/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;112;add_test;/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;0;")
add_test(test_svh_send_packet "/home/lab-pc/robot_hand_ws/build/schunk_svh_library/test_svh_send_packet")
set_tests_properties(test_svh_send_packet PROPERTIES  _BACKTRACE_TRIPLES "/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;126;add_test;/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;0;")
add_test(test_svh_send_feedback_packet "/home/lab-pc/robot_hand_ws/build/schunk_svh_library/test_svh_send_feedback_packet")
set_tests_properties(test_svh_send_feedback_packet PROPERTIES  _BACKTRACE_TRIPLES "/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;155;add_test;/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;0;")
add_test(test_svh_controller_init_send "/home/lab-pc/robot_hand_ws/build/schunk_svh_library/test_svh_controller_init_send")
set_tests_properties(test_svh_controller_init_send PROPERTIES  _BACKTRACE_TRIPLES "/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;169;add_test;/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;0;")
add_test(test_svh_finger_manager "/home/lab-pc/robot_hand_ws/build/schunk_svh_library/test_svh_finger_manager")
set_tests_properties(test_svh_finger_manager PROPERTIES  _BACKTRACE_TRIPLES "/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;183;add_test;/home/lab-pc/robot_hand_ws/src/schunk_svh_library/CMakeLists.txt;0;")
