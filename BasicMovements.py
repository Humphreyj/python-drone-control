from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

print(f'{drone.get_battery()} % remaining')
centimers_per_foot = 30.48
# drone.send_rc_control(0,0,0,0) this line will stop the drone
#left-right, forward/back,up/down,yaw
