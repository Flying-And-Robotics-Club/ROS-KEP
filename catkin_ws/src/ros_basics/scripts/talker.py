import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node("talker", anonymous = True)
    