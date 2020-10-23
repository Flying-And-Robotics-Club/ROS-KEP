# ROS Installation

> Every version or ROS works stably with a particular version of Ubuntu.

> Throughout this KEP, we will be using ***ROS Melodic*** which requires ***Ubuntu 18.04 (Bionic Beaver)*** to run.

## Step 0 - Install Ubuntu 18.04

There are 2 ways to go about this...

* Install Ubuntu on your system by Dual Boot (recommended) or as your Primary OS.
* Install Ubuntu in a VM on your Windows / MAC Machine.

**Either way, [here](https://releases.ubuntu.com/18.04.5/?_ga=2.151950462.655073189.1602001766-309397952.1602001766) is the link to the official download site.**

> Move to the next step only after installing Ubuntu on your system.

<hr>

## Step 1 - Install ROS Melodic

**Head over to the [official documentation](http://wiki.ros.org/melodic/Installation/Ubuntu) and follow the steps for installing *Desktop-Full Install Version od ROS Melodic*.**

> The commands for the same are given below.

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

```bash
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

```bash
sudo apt update
```

```bash
sudo apt install ros-melodic-desktop-full
```

```bash
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

```bash
sudo apt install python-rosdep
```

```bash
sudo rosdep init
rosdep update
```

<hr>

## Step 2 - Create your ROS Workspace

> Use the following commands to setup your workspace. What this terms means, will be explained as the KEP begins.

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

```bash
source devel/setup.bash
```

To make sure your workspace is properly overlayed by the setup script, make sure ROS_PACKAGE_PATH environment variable includes the directory you're in.

```bash
echo $ROS_PACKAGE_PATH
> /home/youruser/catkin_ws/src:/opt/ros/melodic/share
```

That's it :)
