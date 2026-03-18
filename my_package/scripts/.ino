#include <ros.h>
#include <std_msgs/Int16MultiArray.h>

ros::NodeHandle nh;

// RGB 핀
const int RED_PIN = 9;
const int GREEN_PIN = 10;
const int BLUE_PIN = 11;

void ledCallback(const std_msgs::Int16MultiArray& msg) {
  if (msg.data_length < 3) return;

  int r = msg.data[0];
  int g = msg.data[1];
  int b = msg.data[2];

  analogWrite(RED_PIN, r);
  analogWrite(GREEN_PIN, g);
  analogWrite(BLUE_PIN, b);
}

ros::Subscriber<std_msgs::Int16MultiArray> sub("led_color", ledCallback);

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(10);
}