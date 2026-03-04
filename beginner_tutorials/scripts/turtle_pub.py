#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def circle():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('circle_pub')
    rate = rospy.Rate(1)  # 1Hz = 1초에 1번
    msg = Twist()
    msg.linear.x = 2.0
    msg.angular.z = 1.8
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
