>In this section we will learn how to create a ROS Node inside pkg_ros_basics ROS Package which we created in the previous section  Navigate to pkg_ros_basics.

``` bash
cd ~/catkin_ws/src/pkg_ros_basics
```

OR
``` bash
roscd pkg_ros_basics
```

> Create a scripts folder for your Python scripts and navigate into the folder.

``` bash
mkdir scripts
cd scripts
```

>Create a Python script called node_hello_ros.py.

``` bash
touch node_hello_ros.py
```

> Open the script in any text-editor and start editing.

``` bash
gedit node_hello_ros.py
```

First line of all your Python ROS scripts should be the following shebang

``` bash
#!/usr/bin/env python
```

> Now write a ROS Node to print Hello World! on the console.

``` python
#!/usr/bin/env python

import rospy


def main():    
    
    # 1. Make the script a ROS Node.
    rospy.init_node('node_hello_ros', anonymous=True)

    # 2. Print info on console.
    rospy.loginfo("Hello World!")
    
    # 3. Keep the node alive till it is killed by the user.
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

```

> Now you have to make this script an executable.
``` bash
sudo chmod +x node_hello_ros.py
```

>Now in order to run your ROS Node, 
* Open up a terminal and run ROS Master.
    ``` bash
    roscore
    ```

* Once the roscore is up running, open a new termminal and run the ROS Node.

    ``` bash
    rosrun pkg_ros_basics node_hello_ros.py
    ```

