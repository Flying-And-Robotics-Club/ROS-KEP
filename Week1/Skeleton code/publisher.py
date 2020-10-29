#!/usr/bin/env python 

#import rospy library and String from std_msgs library
import ___ #python
from ___  import ___ #std_msgs

def publisher():

    #Initialize the node using a suitable name
    rospy.init_node('')

    #Make a publisher of any name ('pub' here, try experimenting with different names)
    #The publisher object is created using rospy.Publisher()
    #rospy.Publisher takes 3 arguments: name of topic its communicating over, type of msg and queue_size (ideally 10 in our case)
    pub = rospy.Publisher('', , )

    #Create a object of rospy.Rate() with a suitable name ('rate' in our case)
    #This is regulate the rospy.sleep() to keep sending msgs to meet the rate passed in this argument
    #example: rospy.Rate(10) which will send 10 msgs per second - 10 Hz

    rate = #Enter code here

    i = 0 
    while not rospy.is_shutdown():
        send_string = "Message - %s" % i
        #Publish the msg to topic using name_of_publisher.publish(send_string), name_of_publisher is the name given
        #in line 15
        
                                                             #Enter code here

        i = i +1
        #Make the python script to send something on the terminal depicting it has sent something
        #rospy.loginfo('Sent ' + send_string)

        #call rate.sleep() to make sure we set the rate to the rate passed in line 21
        
                                                             #Enter code here



if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass