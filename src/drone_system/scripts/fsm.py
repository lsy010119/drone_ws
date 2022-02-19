import numpy as np

from drone_system import Status
from std_msgs.msg import String,Bool


class FSM:

    def __init__(self):

        pass


    def transform_state(self,data_hub):

        #FSM Algorithm here

        if data_hub.cur_state == "arm":

            pass

        elif data_hub.cur_state == "disarm":
        
            pass

        
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
