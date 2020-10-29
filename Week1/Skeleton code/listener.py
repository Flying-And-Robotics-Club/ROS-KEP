#!/usr/bin/env python

#import rospy library and String from std_msgs library

import 
from __ import __   

#define the callback function which is called using a 'received_data'
def callback(received_data):
    rospy.loginfo('Recieved: ' + #enter code here' )

def listener():

    #Initialize node with a name
    rospy.init_node('')

    #Create a subscriber using rospy.Subscriber() which takes in 3 values:
    #name of topic its communicating over, type of msg over topic and name of callback function (callback) in our case
    rospy.Subscriber('', , callback)

    #call rospy.spin() to make sure this node runs until 'Ctrl + C'
    rospy.spin()



if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass