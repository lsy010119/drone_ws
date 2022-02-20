import numpy as np
from std_msgs.msg import String,Bool


class FSM:

    def __init__(self):

        pass


    def transform_disarm(self,data_hub):
        """
        State : 'disarm'
        
        1. disarm =(/mission)====> arm
        """

        ''' disarm ===> arm (by /mission_msgs from ground_station) '''  
        if data_hub.mission == "arm" and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("arm") # send a mission to trajectory
            
            # inputing mission is not avaliable until the mission "arm" is done
            data_hub.pub2ground.publish(False)
            

        else:

            # print("Invalid mission recieved. please input the avaliable mission")
            data_hub.transform_trigger = False # turn off the trigger
            
            # give the input permission to input the valid mission
            data_hub.pub2ground.publish(True)



    def transform_arm(self,data_hub):

        """
        State : 'arm'
        
        1. arm =(/mission)====> disarm
        2. arm =(auto_disarm)=> disarm
        3. arm =(/mission)====> take_off
        """

        ''' arm ===> disarm (by /mission_msgs from ground_station) '''  
        if data_hub.mission == "disarm" and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("disarm") # send a mission to trajectory
            
            # inputing mission is not avaliable until the mission "disarm" is done
            data_hub.pub2ground.publish(False)

        ''' arm ===> take_off (by /mission_msgs from ground_station) '''  
        if data_hub.mission == "take_off" and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("take_off") # send a mission to trajectory
            data_hub.is_performing_action = True # the drone starts to performing an action
            
            # inputing mission is not avaliable until the mission "take_off" is done
            data_hub.pub2ground.publish(False)

        else:

            # print("Invalid mission recieved. please input the avaliable mission")
            data_hub.transform_trigger = False # turn off the trigger
            
            # give the input permission to input the valid mission
            data_hub.pub2ground.publish(True)



    def transform_take_off(self,data_hub):

        """
        State : 'take_off'
        
        1. take_off =(/is_done)====> hold
        """

        ''' take_off ===> hold (by /is_done from motion_controller) '''  
        if data_hub.is_performing_action == False and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("hold") # send a mission to trajectory
            
            # inputing mission is not avaliable until the mission "disarm" is done
            data_hub.pub2ground.publish(False)



    def transform_arm(self,data_hub):

        """
        State : 'arm'
        
        1. arm =(/mission)====> disarm
        2. arm =(auto_disarm)=> disarm
        3. arm =(/mission)====> take_off
        """

        ''' arm ===> disarm (by /mission_msgs) '''  
        if data_hub.mission == "disarm" and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("disarm") # send a mission to trajectory
            
            # inputing mission is not avaliable until the mission "disarm" is done
            data_hub.pub2ground.publish(False)

        ''' arm ===> take_off (by /mission_msgs) '''  
        if data_hub.mission == "take_off" and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("take_off") # send a mission to trajectory
            
            # inputing mission is not avaliable until the mission "take_off" is done
            data_hub.pub2ground.publish(False)

        else:

            # print("Invalid mission recieved. please input the avaliable mission")
            data_hub.transform_trigger = False # turn off the trigger
            
            # give the input permission to input the valid mission
            data_hub.pub2ground.publish(True)



    def transform_arm(self,data_hub):
        """
        State : 'arm'
        
        1. arm =(/mission)====> disarm
        2. arm =(auto_disarm)=> disarm
        3. arm =(/mission)====> take_off
        """
        ''' arm ===> disarm (by /mission_msgs) '''  
        if data_hub.mission == "disarm" and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("disarm") # send a mission to trajectory
            
            # inputing mission is not avaliable until the mission "disarm" is done
            data_hub.pub2ground.publish(False)

        ''' arm ===> take_off (by /mission_msgs) '''  
        if data_hub.mission == "take_off" and data_hub.transform_trigger:

            data_hub.transform_trigger = False # turn off the trigger
            data_hub.pub2trajec.publish("take_off") # send a mission to trajectory
            
            # inputing mission is not avaliable until the mission "take_off" is done
            data_hub.pub2ground.publish(False)

        else:

            # print("Invalid mission recieved. please input the avaliable mission")
            data_hub.transform_trigger = False # turn off the trigger
            
            # give the input permission to input the valid mission
            data_hub.pub2ground.publish(True)



    def transform_state(self,data_hub):

        #FSM Algorithm here

        if data_hub.cur_state == "arm":
            
            self.transform_arm(data_hub)


        elif data_hub.cur_state == "disarm":
        
            self.transform_disarm(data_hub)

        
        elif data_hub.cur_state == "take_off":
        
            pass

        
        elif data_hub.cur_state == "hold":
        
            pass

        
        elif data_hub.cur_state == "land":
        
            pass

        
        elif data_hub.cur_state == "park":
        
            pass


        elif data_hub.cur_state == "search":
        
            pass
