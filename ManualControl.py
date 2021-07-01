from typing import ForwardRef
from djitellopy import tello
import Keypress as kp
import time
import cv2
global image

kp.init()
drone = tello.Tello()
drone.connect()
centimers_per_foot = 30.48
print(f'{drone.get_battery()} % remaining')


def getKeyboardInput():
    left_right, forward_back, up_down, yaw = 0, 0, 0, 0

    speed = 40
    # lateral movement
    if kp.getKey("a"):
        left_right = -speed
    if kp.getKey("d"):
        left_right = speed
        # yaw
    if kp.getKey("q"):
        yaw = -speed
    if kp.getKey("e"):
        yaw = speed
    # thrust
    if kp.getKey("w"):
        forward_back = speed
    if kp.getKey("s"):
        forward_back = -speed
    # altitude
    if kp.getKey("LCTRL"):
        up_down = -speed
    if kp.getKey("SPACE"):
        up_down = speed

    # landing
    if kp.getKey("n"):
        drone.land()
        time.sleep(5)
    # takeoff
    if kp.getKey("r"):
        drone.takeoff()
    # capture photo
    if kp.getKey('RSHIFT'):
        cv2.imwrite(f'Captures/Images/{time.time()}.jpg', image)
        # add a short delay to prevent multiple captures
        time.sleep(0.5)
    # get height
    if kp.getKey("h"):
        print(f'Altitude is {drone.get_height() / centimers_per_foot} feet.')
    return [left_right, forward_back, up_down, yaw]


while True:

    values = getKeyboardInput()

    drone.send_rc_control(values[0], values[1], values[2], values[3])
    image = drone.get_frame_read().frame
    image = cv2.resize(image, (360, 306))
    cv2.imshow("Drone Feed", image)
    cv2.waitKey(1)
