import rospy
import asyncio
from fsm            import FSM
from drone_system.msg   import Status
from std_msgs.msg       import String
from std_msgs.msg       import Bool

class BehaviorPlanner:


    def __init__(self):
        
        self.pos_n, self.pos_e, self.pos_d = 0.0, 0.0, 0.0
        self.vel_n, self.vel_e, self.vel_d = 0.0, 0.0, 0.0
        self.yaw_ang = 0.0
        self.yaw_ang_vel = 0.0

        self.cur_state = "disarm"
        self.mission = None
        self.transform_trigger = False
        self.is_performing_action = False

        self.pub2trajec = rospy.Publisher("/action_msgs", String, queue_size=1)
        self.pub2ground = rospy.Publisher("/input_permission", Bool, queue_size=1)
        
        self.telem_rate = rospy.Rate(10)
        self.img_rate = rospy.Rate(10)
        self.trajectory_rate = rospy.Rate(10)



    def action_done(self,msg):

        self.is_performing_action = False
        


    def status_update(self,telem):

        self.pos_n, self.pos_e, self.pos_d = \
        telem.pos_n, telem.pos_e, telem.pos_d
        
        self.vel_n, self.vel_e, self.vel_d = \
        telem.vel_n, telem.vel_e, telem.vel_d

        self.yaw_ang, self.yaw_ang_vel = \
        telem.yaw_ang, telem.yaw_ang_vel

    

    def mission_update(self,mission):

        self.mission = mission.data
        self.transform_trigger = True



    def main(self):

        rospy.Subscriber("/sensor_msgs", Status, self.status_update)
        rospy.Subscriber("/mission_msgs", String, self.mission_update)  
        rospy.Subscriber("/is_done", Bool, self.action_done)  
    
        while not rospy.is_shutdown():

            FSM().transform_state(self)

            print(self.cur_state+"             ",end="\r")
            self.telem_rate.sleep()

        


if __name__ == "__main__":

    rospy.init_node("data_hub")
    
    B = BehaviorPlanner()
    B.main()