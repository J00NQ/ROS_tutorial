# ROS development install
ubuntu 20.04
ROS noetic

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
apt update
```bash
sudo apt update
```
install full-version of noetic
```bash
sudo apt install ros-noetic-desktop-full
```
setup noetic
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