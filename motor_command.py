#!/usr/bin/env python

import rospy
import motor_command_model
import me416_utilities

from std_msgs.msg import String
from me416_lab.msg import MotorSpeedsStamped
from geometry_msgs.msg import Twist

motor_left = me416_utilities.MotorSpeedLeft()
motor_right = me416_utilities.MotorSpeedRight()

def main():

    rospy.init_node('motor_command', anonymous = 'True')
    pub = rospy.Publisher('motor_speeds', MotorSpeedsStamped, queue_size = 10)
    rospy.Subscriber('robot_twist', Twist, callback)
    rospy.spin()

def callback(info):
    left, right = motor_command_model.twist_to_speeds(info.linear.x, info.angular.z)
    motor_left.set_speed(left)
    motor_right.set_speed(right)

    msg = MotorSpeedsStamped(rospy.Time.now(), motor_left, motor_right)

if __name__ == '__main__':
    try:
        main()
    finally:
        #This is the place to put any "clean up" code that should be executed
        #on shutdown even in case of errors, e.g., closing files or windows
        pass
