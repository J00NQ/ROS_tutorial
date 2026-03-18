#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int16MultiArray

# =========================
# 전역 상수 정의
# =========================

DIST_THRESHOLD = 0.8  # 벽 근접 기준 (m)

# LED 색상 (R, G, B)
COLOR_STOP   = (0, 0, 0)
COLOR_FORWARD = (0, 255, 0)
COLOR_BACKWARD = (0, 0, 255)
COLOR_NEAR_OBS = (255, 0, 0)


class LEDController:
    def __init__(self):
        rospy.init_node('led_controller')

        self.cmd_sub = rospy.Subscriber('/cmd_vel', Twist, self.cmd_callback)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        self.led_pub = rospy.Publisher('/led_color', Int16MultiArray, queue_size=10)

        self.current_linear = 0.0
        self.min_distance = float('inf')

        self.rate = rospy.Rate(10)

    def cmd_callback(self, msg):
        self.current_linear = msg.linear.x

    def scan_callback(self, msg):
        valid_ranges = [r for r in msg.ranges if msg.range_min < r < msg.range_max]
        if valid_ranges:
            self.min_distance = min(valid_ranges)

    def decide_color(self):
        """
        상태 판단 로직 분리 (가독성 + 테스트 용이)
        """

        # 1. 장애물 근접 (최우선)
        if self.min_distance < DIST_THRESHOLD:
            return COLOR_NEAR_OBS

        # 2. 전진
        if self.current_linear > 0:
            return COLOR_FORWARD

        # 3. 후진
        if self.current_linear < 0:
            return COLOR_BACKWARD

        # 4. 정지
        return COLOR_STOP

    def run(self):
        while not rospy.is_shutdown():
            r, g, b = self.decide_color()

            led_msg = Int16MultiArray()
            led_msg.data = [r, g, b]

            self.led_pub.publish(led_msg)
            self.rate.sleep()


if __name__ == '__main__':
    node = LEDController()
    node.run()