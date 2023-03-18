# Change the hand gestures
In order to change the hand gestures, go to the file 'requsted_gestures.py'. then look for the arrays that look like this:
```
def fist():
    #return the value numbers that make a fist
    return [0.44,0.63,1.33,0.8,0.8,1.33,0.98,0.98,0.0]
```
These array sending the vaule for each joint of the hand its value, so if you change the values to your needs you need to source the termianal and start the launch file again.

You can also move the joints by using the 'joint_state_publisher_gui'. You can start the node by using this line in terminal:
```
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```
Make sure that you kill the 'requsted_gestures.py' node before you use the 'joint_state_publisher_gui' because both of them will send information to the '/robot_description' topic and it will result jitter in the visual of the robot hand
