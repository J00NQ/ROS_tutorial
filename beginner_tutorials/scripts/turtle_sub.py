#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def callback(msg):
    if msg.x < 1.0 or msg.x > 10.0:
        rospy.loginfo("X축 경고: %.1f", msg.x)
    if msg.y < 1.0 or msg.y > 10.0:
        rospy.loginfo("Y축 경고: %.1f", msg.y)

def listener():
    rospy.init_node('turtle_sub')
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
