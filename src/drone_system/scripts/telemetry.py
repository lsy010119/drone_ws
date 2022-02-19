import asyncio
import numpy as np
import rospy

from drone_system.msg import Status
from std_msgs.msg     import String
from behavior_planner import BehaviorPlanner
from mavsdk import System

class Telemetry:


    def __init__(self):
        
        self.drone = System()

        rospy.init_node("telemetry")
        self.pub = rospy.Publisher("/sensor_msgs",Status,queue_size=1)

        self.rate = BehaviorPlanner().telem_rate
        self.sensor_msgs = Status()


    async def publish_sensor(self):

        # await self.drone.connect(system_address="serial:///dev/ttyUSB0:921600")
        await self.drone.connect(system_address="udp://:14540")

        print("Connecting ...")
        async for state in self.drone.core.connection_state():
            if state.is_connected:
                print(f"Connected              ",end="\r")
                break
        
        async for posvelned in self.drone.telemetry.position_velocity_ned():
            
            self.sensor_msgs.pos_n = posvelned.position.north_m
            self.sensor_msgs.pos_e = posvelned.position.east_m
            self.sensor_msgs.pos_d = posvelned.position.down_m
            self.sensor_msgs.vel_n = posvelned.velocity.north_m_s
            self.sensor_msgs.vel_e = posvelned.velocity.east_m_s
            self.sensor_msgs.vel_d = posvelned.velocity.down_m_s

            self.pub.publish(self.sensor_msgs)
            self.rate.sleep()    

       
            
            
if __name__ == "__main__":

    T = Telemetry()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.gather(T.publish_sensor()))

