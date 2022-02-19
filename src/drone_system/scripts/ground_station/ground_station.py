import numpy as np
import rospy

from drone_system.msg import Status
from std_msgs.msg     import String
from std_msgs.msg     import Bool

class GroundStation:


    def __init__(self):

        rospy.init_node("ground_station")
        rospy.Subscriber("/input_permission", Bool, self.input_handler)
        self.pub2datahub = rospy.Publisher("mission_msgs", String, queue_size=1)
        self.input_avaliable = True
        self.gs_rate = rospy.Rate(10)



    def user_input(self):

        while not rospy.is_shutdown():
            
            if self.input_avaliable:
                
                mission = input("Mission : ")
                self.input_avaliable = False
                self.pub2datahub.publish(mission)

            self.gs_rate.sleep()
    

    def input_handler(self, permission):

        print("permission recieved")
        self.input_avaliable = permission



if __name__ == "__main__":

    GS = GroundStation()
    GS.user_input()