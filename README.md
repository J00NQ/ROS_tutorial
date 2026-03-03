# ROS development install
- ubuntu 20.04
- ROS noetic

# ROS install
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
```bash
sudo apt install curl # if you haven't already installed curl
```
```bash
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

```
1. apt update
```bash
sudo apt update
```
2. install full-version of noetic
```bash
sudo apt install ros-noetic-desktop-full
```
3. setup noetic
```bash
source /opt/ros/noetic/setup.bash
```
4. Environment setup
```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
5. Create a ROS Workspace
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

## turtlesim 토픽 정리

### /turtle1/cmd_vel (geometry_msgs/Twist)

거북이에게 보내는 속도 명령
```c
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
```
### /turtle1/pose (turtlesim/Pose)

거북이의 현재 위치와 방향
```c
x: 5.6494669914245605
y: 5.448278903961182
theta: -1.482805848121643
linear_velocity: 0.0
angular_velocity: 0.0
```
### /turtle1/color_sensor (turtlesim/Color)

거북이 발 아래의 배경 색상
```c
r: 179
g: 184
b: 255
```

## 4. rostopic pub으로 정사각형 그리기
```bash
rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist
```

```bash
rostopic echo /turtle1/cmd_vel
```
```bash
 rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'    # 직진
 rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.5708]' # 반시계방향으로 약 90도 회전
```
```c
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 1.5708
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 1.5708
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 1.5708
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 1.5708
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 1.5708
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 1.5708
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 1.5708
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
```

## 5. turtlesim 2개 동시 실행

```bash
rosrun turtlesim turtlesim_node                         # 기본 터틀심 실행
rosrun turtlesim turtlesim_node __name:=my_turtle       # my_turtle 실행
```

```bash
rosnode list
```
출력
```
/my_turtle/turtle1/cmd_vel
/my_turtle/turtle1/color_sensor
/my_turtle/turtle1/pose
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

### 동시 제어?
```bash
rosrun turtlesim turtle_teleop_key
rostopic info /turtle1/cme_vel
```
```
rostopic info /turtle1/cmd_vel
Type: geometry_msgs/Twist

Publishers: None

Subscribers: 
 * /turtle1 (http://ubuntu:36093/)
 * /turtlesim (http://ubuntu:43887/)
 * /my_turtle (http://ubuntu:34133/)
```
- 두 터틀심이 같은 토픽을 구독하고있어서 동시에 움직임

### name 대신 ns(namespace) 사용
```bash
rosrun turtlesim turtlesim_node __ns:=my_turtle
$ rosnode list
```
```
/my_turtle
/my_turtle/turtlesim
/rosout
/rostopic_11583_1772526821846
/turtle1
/turtlesim
```
구독 정보 비교
```bash
$ rostopic info /my_turtle/turtle1/cmd_vel
```
```
Type: geometry_msgs/Twist

Publishers: None

Subscribers: 
 * /my_turtle/turtlesim (http://ubuntu:38815/)
```
```bash
$ rostopic info /turtle1/cmd_vel
```
```
Type: geometry_msgs/Twist

Publishers: None

Subscribers: 
 * /turtle1 (http://ubuntu:36093/)
 * /my_turtle (http://ubuntu:34133/)
 * /turtlesim (http://ubuntu:34001/)
 ```