import numpy as np
import rospy

from drone_system import Status
from std_msgs.msg import String

class TrajectoryGenerator:

    def __init__(self):
        
        rospy.init_node("trajectory_generator")

        self.action = None



    def action_update(self,action_msgs):

        self.action = action_msgs



    def run(self):

        rospy.Subscriber("action_msgs", String, self.action_update)

        while not rospy.is_shutdown():
            
            pass
