# svh_robot_hand_lyeh
this is a repository to operate the 5 fingers SVH-hand robot in a ros2 rviz simulation. it is an extention that completes the schunck_svh_ros_driver.

## installation
first, install the [Schunk SVH ros driver](https://github.com/fzi-forschungszentrum-informatik/schunk_svh_ros_driver/tree/ros2-foxy). follow the instructions in the link to install the package.

then, in the same `src` folder of your Ros2 workspace that you installed the Schunk SVH package use the next lines in terminal 
```
git clone https://github.com/lyehezkel/svh_robot_hand_lyeh.git
rosdep install --ignore-src --from-paths ./ -y -r
```
navigate back to the root of you workspace then use the command
```
colcon build
```
source the terminal and then use the command
```
ros2 launch hand_robot_bringup hand_robot.launch.py

```
