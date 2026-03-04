#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

last_warn_time = rospy.Time(0)  # 마지막 경고 시각

def callback(msg):
    global last_warn_time

    now = rospy.Time.now()

    if (msg.x < 1.0 or msg.x > 10.0 or
        msg.y < 1.0 or msg.y > 10.0):

        # 마지막 경고 이후 1초 이상 지났을 때만 출력
        if (now - last_warn_time).to_sec() >= 1.0:
            rospy.loginfo("경고! 위치: x=%.1f y=%.1f",
                          msg.x, msg.y)
            last_warn_time = now

def listener():
    rospy.init_node('turtle_sub')
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()