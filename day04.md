# Day 4 실습 결과

## action 환경설정

### 1. package.xml 수정(아래 내용 추가)
```xml
<build_depend>actionlib</build_depend>
<build_depend>actionlib_msgs</build_depend>
<exec_depend>actionlib</exec_depend>
<exec_depend>actionlib_msgs</exec_depend>
```

### 2. CMakeLists.txt 수정(아래 내용 추가)
```make
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  actionlib              # 추가
  actionlib_msgs         # 추가
)

add_action_files(
  FILES
  Timer.action
)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs         # 추가
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs   # 추가
)
```
- action 디렉토리 생성
```bash
cd ~/catkin_ws/beginner_tutorials
mkdir action
```

## Timer.action 실습

### 1. Timer.action 작성

- [Timer.action](beginner_tutorials/action/Timer.action)
- 환경설정 적용
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
- 생성된 메시지 확인
```bash
rosmsg list | grep Timer
```

### 2. timer_server.py, timer_client.py 작성 및 권한 부여

- [timer_server.py](beginner_tutorials/scripts/timer_server.py)
- [timer_client.py](beginner_tutorials/scripts/timer_client.py)

- 권한 부여
```bash
chmod +x ~/catkin_ws/src/beginner_tutorials/scripts/timer_server.py
chmod +x ~/catkin_ws/src/beginner_tutorials/scripts/timer_client.py

```

### 3. 실행
```bash
cd ~/catkin_ws && catkin_make
source devel/setup.bash
```
- 서버 실행(터미널1)
```bash
rosrun beginner_tutorials timer_server.py
```
- 클라이언트 실행(터미널2)
```bash
rosrun beginner_tutorials timer_client.py
```
- 취소 테스트(터미널3)
```bash
rostopic pub /timer/cancel actionlib_msgs/GoalID "{}"
```