> Here is the code for the publisher we wrote on Day 5. Visit [publisher_code.md](./publisher_code.md) file to see how to create a publisher and learn the basics.

```python
#!/usr/bin/env python

# import libraries
import rospy
from rospy.exceptions import ROSInterruptException
from geometry_msgs.msg import Twist

# define constant PI = 3.14
PI = 3.14

# the logic
def circle_logic():
    
    # define motion parameters
    linear_velocity = 1.0
    radius = 1.0
    angular_velocity = linear_velocity / radius
    frequency = 100

    # create the node and register it as a publisher
    rospy.init_node("node_circle_publisher")
    publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)

    # create the message
    message = Twist()
    message.linear.x = linear_velocity
    message.angular.z = angular_velocity

    # initialize loop parameters
    rate = rospy.Rate(frequency)
    distance_travelled = 0
    target_distance = 2 * PI * radius

    # the publisher loop
    while not rospy.is_shutdown() and distance_travelled < target_distance:

        # publish the message
        publisher.publish(message)

        # update the distance_travelled
        distance_travelled = distance_travelled + linear_velocity / frequency

        # log the acticvity
        rospy.loginfo("Moving the Bot.")
        print(distance_travelled)

        # pause the thread
        rate.sleep()

    # stop the bot
    message.linear.x = 0
    message.angular.z = 0
    publisher.publish(message)

    # log the activity
    rospy.loginfo("Goal Reached...")

if __name__ == "__main__":
    try: circle_logic()
    except ROSInterruptException: pass
```
