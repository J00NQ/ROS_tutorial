# Day 3 실습 결과

## rosbag record

![rosbag record 중 거북이 경로](screenshots/rosbag_record.png)

### 기록 내용 확인

```bash
$ rosbag info my_turtle.bag
```
```
path:        my_turtle.bag
version:     2.0
duration:    18.2s
start:       Mar 04 2026 23:32:17.12 (1772695937.12)
end:         Mar 04 2026 23:32:35.35 (1772695955.35)
size:        94.1 KB
messages:    1148
compression: none [1/1 chunks]
types:       geometry_msgs/Twist [9f195f881246fdfa2798d1d3eebca84a]
             turtlesim/Pose      [863b248d5016ca62ea2e895ae5265cf9]
topics:      /turtle1/cmd_vel      8 msgs    : geometry_msgs/Twist
             /turtle1/pose      1140 msgs    : turtlesim/Pose
```
확인할 것:

duration이 몇 초인가요?         
- 18.2초

어떤 토픽이 기록되었나요?
- /turtle1/cmd_vel, /turtle1/pose

각 토픽의 메시지 수는 몇 개인가요? 
- 8, 1140


## rosbag play

![rosbag play 재생 결과](screenshots/rosbag_play.png)

# 터미널 4 — 재생
```bash
rosbag play my_turtle.bag
```
# 2배속으로 재생
```bash
rosbag play my_turtle.bag -r 2
```
# 무한 반복 재생
```bash
rosbag play my_turtle.bag -l
```
