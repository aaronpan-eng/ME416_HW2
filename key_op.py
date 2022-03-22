#!/usr/bin/env python
"""Collect key presses and pass them to KeysToVelocities object"""

import rospy

from std_msgs.msg import String
import me416_utilities as mu
from geometry_msgs.msg import Twist

def main():
    from motor_command_model import KeyToVelocities
    #initialize node publisher
    rospy.init_node('key_op', anonymous='True')
    robot_twist = Twist()
    pub = rospy.Publisher('robot_twist', Twist, queue_size=10)

    #create object of class KeyToVelocities
    x = KeyToVelocities(object)

    #instructions and initializing variable types
    print('wasd for forward, left, down, and up, respectively')
    speed_angular = float()
    speed_linear = float()
    text_description = String()
    getch = mu._Getch()

    while not rospy.is_shutdown():
        #set key to a keyboard character using getch
        key = getch()

        #shutdown if q pressed
        if key == 'q' or key == 'Q':
            rospy.loginfo("Shutdown initiated")
            rospy.signal_shutdown(
                'Shutting down initiated by %s' % rospy.get_name())
        else:
            #any other key pressed
            speed_angular, speed_linear, text_description = x.update_speeds(key)

            #print output of update_speeds
            print(text_description)
            robot_twist.linear.x = speed_linear
            robot_twist.angular.z = speed_angular

            #publish to robot_twist
            pub.publish(robot_twist)
    #loop    
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    finally:
        #This is the place to put any "clean up" code that should be executed
        #on shutdown even in case of errors, e.g., closing files or windows
        pass

