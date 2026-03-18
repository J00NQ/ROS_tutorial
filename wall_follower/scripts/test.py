#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int16MultiArray

class LEDController:
    def __init__(self):
        rospy.init_node('led_controller')

        self.cmd_sub = rospy.Subscriber('/cmd_vel', Twist, self.cmd_callback)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        self.led_pub = rospy.Publisher('/led_color', Int16MultiArray, queue_size=10)

        self.current_linear = 0.0
        self.min_distance = 999

        self.rate = rospy.Rate(10)

    def cmd_callback(self, msg):
        self.current_linear = msg.linear.x

    def scan_callback(self, msg):
        # 전방 최소 거리
        valid_ranges = [r for r in msg.ranges if msg.range_min < r < msg.range_max]
        if valid_ranges:
            self.min_distance = min(valid_ranges)

    def run(self):
        while not rospy.is_shutdown():
            led_msg = Int16MultiArray()

            # 기본값 OFF
            r, g, b = 0, 0, 0

            # 1. 장애물 근접 (우선순위 가장 높음)
            if self.min_distance < 0.3:
                r, g, b = 255, 0, 0  # 빨강

            # 2. 전진
            elif self.current_linear > 0:
                r, g, b = 0, 255, 0  # 초록

            # 3. 후진
            elif self.current_linear < 0:
                r, g, b = 0, 0, 255  # 파랑

            led_msg.data = [r, g, b]
            self.led_pub.publish(led_msg)

            self.rate.sleep()

if __name__ == '__main__':
    node = LEDController()
    node.run()