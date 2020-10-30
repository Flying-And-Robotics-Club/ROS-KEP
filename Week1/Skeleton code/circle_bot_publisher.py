#!/usr/bin/env python

# import libraries
import rospy
from rospy.exceptions import ROSInterruptException

# define constant PI = 3.14

# the logic
def circle_logic():
    
    # define motion parameters
    ## linear_velocity
    ## angular_velocity
    ## radius
    ## frequency

    # create the node and register it as a publisher

    # create the messgae

    # initialize loop parameters
    ## rate
    ## distance_travelled
    ## target_distance

    # the publisher loop
    while not rospy.is_shutdown() and distance_travelled < target_distance:

        # publish the message
        # update the distance_travelled
        # log the acticvity
        # pause the thread

    # stop the bot
    # log the activity

if __name__ == "__main__":
    try: circle_logic()
    except ROSInterruptException: pass
