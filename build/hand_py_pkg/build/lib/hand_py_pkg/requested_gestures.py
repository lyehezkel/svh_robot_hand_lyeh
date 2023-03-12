import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import time
import random

def fist():
    #return the value numbers that make a fist
    return [0.44,0.63,1.33,0.8,0.8,1.33,0.98,0.98,0.0]
def bet():
    #return the value numbers that make a rock sign
    return [0.89,0.17,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
def two_fingers():
    #return the value numbers that make the number two with fingers
    return [0.74,0.34,0.0,0.0,0.0,0.0,0.98,0.98,0.4]
def three_fingers():
    #return the value numbers that make  the number three with fingers
    return [0.0,0.0,0.0,0.0,0.0,0.0,0.98,0.98,0.48]
def five_fingers():
    #return the value numbers that make  the number four with fingers
    return [0.15,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.58]
def gimel():
    #return the value numbers that make  the number four with fingers
    return [0.0,0.0,0.0,0.0,0.8,1.33,0.98,0.98,0.0]
def het():
    #return the value numbers that make  the number four with fingers
    return [0.53,0.28,0.0,0.0,0.8,1.33,0.98,0.0,0.1]
def tet():
    #return the value numbers that make  the number four with fingers
    return [0.37,0.97,1.0,0.8,0.0,0.0,0.0,0.0,0.1]
def kaf():
    #return the value numbers that make  the number four with fingers
    return [0.33,0.99,0.35,0.52,0.44,0.4,0.36,0.27,0.1]
def nun():
    #return the value numbers that make  the number four with fingers
    return [0.89,0.99,1.33,0.8,0.8,1.33,0.98,0.98,0.49]

class RequestedNode(Node):

    def __init__(self):
        super().__init__('requested_nodes')
        self.subscription = self.create_subscription(JointState, 'joint_states', self.joint_state_callback, 10)
        self.subscription  # prevent unused variable warning
        self.current_joint_positions = [0.0] * 9
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        timer_period = 20  # seconds
        self.timer = self.create_timer(timer_period, self.publish_number)


        

    def joint_state_callback(self, msg):
        desired_joints = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
        for i in range(len(msg.name)):
            if msg.name[i] in desired_joints:
                self.current_joint_positions[desired_joints.index(msg.name[i])] = msg.position[i]

    def publish_number(self):
        new_state = two_fingers()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = three_fingers()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = five_fingers()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = fist()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = bet()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = gimel()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = het()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = tet()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = kaf()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)
        new_state = nun()
        for i in range(0, 97):
            for j in range(len(self.current_joint_positions)):
                if new_state[j] - self.current_joint_positions[j] > 0:
                    self.current_joint_positions[j] += 0.01
                if new_state[j] - self.current_joint_positions[j] < 0:
                    self.current_joint_positions[j] -= 0.01
            joint_state_msg = JointState()
            joint_state_msg.header.stamp = self.get_clock().now().to_msg()
            joint_state_msg.name = ['left_hand_Thumb_Flexion', 'left_hand_Thumb_Opposition', 'left_hand_Index_Finger_Distal', 'left_hand_Index_Finger_Proximal', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal', 'left_hand_Ring_Finger', 'left_hand_Pinky', 'left_hand_Finger_Spread']
            joint_state_msg.position = self.current_joint_positions
            self.publisher_.publish(joint_state_msg)
            time.sleep(0.01)
        time.sleep(1.0)

def main(args=None):
    rclpy.init(args=args)
    node = RequestedNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()