# DAY 3

> Create the root workspace directory. You can name your directory anything but by ROS convention we will use catkin_ws as the name.
``` bash 
cd ~/
mkdir --parents catkin_ws/src
cd catkin_ws
```

> Initialize the catkin workspace.
``` bash 
catkin init
```

> Build the workspace.
``` bash 
cd ~/catkin_ws
catkin build
```

> Now your catkin workspace will have additional directories build, devel, logs.

``` bash
ls
```

> Now to make your workspace visible to ROS. Source the setup file in the devel directory.
``` bash
source ~/catkin_ws/devel/setup.bash
```

> By doing this, all the packages that you create inside the src folder will be visible to ROS.  
This setup.bash file of your workspace must be source everytime when you want to use ROS packages created inside this workspace.
 To save typing, add this to your .bashrc,

``` bash
gedit ~/.bashrc

#Add to the end: 
source ~/catkin_ws/devel/setup.bash

````

Save and close the editor.
