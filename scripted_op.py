#!/usr/bin/env python

import rospy
import csv
import me416_utilities as mu
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('scripted_op', anonymous='True')
    pub = rospy.Publisher('robot_twist', Twist, queue_size=10)
    list_speedpair = mu.read_two_columns_csv(
        'scripted_op.csv')
    robot_twist = Twist()
    speed_linear = float()
    speed_angular = float()

    rate = rospy.Rate(1)

    i = 0

    while not rospy.is_shutdown():
        i = (i+1) % len(list_speedpair)
        list = list_speedpair[i]
        speed_linear = list[0]
        speed_angular = list[1]
        robot_twist.linear.x = speed_linear
        robot_twist.angular.z = speed_angular
        pub.publish(robot_twist)

        rate.sleep()


if __name__ == '__main__':
    main()

