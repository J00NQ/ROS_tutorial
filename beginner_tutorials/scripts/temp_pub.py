#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import random

def temperature():
    pub = rospy.Publisher('temperature', Float32, queue_size=10)
    rospy.init_node('temperature_pub')
    rate = rospy.Rate(1)  # 1Hz = 1초에 1번
    temp = random.uniform(20.0, 40.0)

    while not rospy.is_shutdown():
        rospy.loginfo("온도 발행: %.1f도", temp)
        pub.publish(temp)
        temp = random.uniform(20.0, 40.0)
        rate.sleep()

if __name__ == '__main__':
    try:
        temperature()
    except rospy.ROSInterruptException:
        pass
