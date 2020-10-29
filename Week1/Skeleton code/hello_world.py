#!/usr/bin/env python

#<Import the python library - rospy>
import 

def helloworld():

    #Initiate the node with suitable name using rospy.init_node('name_of_node')
    rospy.init_node('')

    #Print something to terminal using rospy.loginfo('Something')
    rospy.loginfo('')

    #Uncomment the below line if you want your node to run continously till you do 'Ctrl + C'
    #rospy.spin()



if __name__ == '__main__':
    try:
        helloworld()
    except rospy.ROSInterruptException:
        pass

