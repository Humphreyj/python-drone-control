from typing import ForwardRef
from djitellopy import tello
import Keypress as kp
import time
import cv2
import numpy as np
import math
global image


##PARAMETERS##
fSpeed = 117/10
aSpeed = 360/10
interval = 0.25
dInterval = fSpeed*interval
aInterval = aSpeed*interval
# PARAMTERS

x, y = 500, 500
a = 0
yaw = 0


kp.init()
drone = tello.Tello()
drone.connect()
print(f'{drone.get_battery()} % remaining')

points = []


def getKeyboardInput():
    left_right, forward_back, up_down, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    global yaw, x, y, a
    d = 0
    # lateral movement
    if kp.getKey("a"):
        left_right = -speed
        d = dInterval
        a = -180
    if kp.getKey("d"):
        left_right = speed
        left_right = -speed
        d = -dInterval
        a = 180
        # yv
    if kp.getKey("q"):
        yv = -aspeed
        yaw -= aInterval

    if kp.getKey("e"):
        yv = aspeed
        yaw += aInterval
    # thrust
    if kp.getKey("w"):
        forward_back = speed
        d = dInterval
        a = 270
    if kp.getKey("s"):
        forward_back = -speed
        d = -dInterval
        a = -90
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
    time.sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))
    return [left_right, forward_back, up_down, yv]


def drawPoints(image, points):
    for point in points:
        cv2.circle(image, point, 5, (0, 0, 255), cv2.FILLED)
        cv2.circle(image, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(
        image, f'({points[-1][0] - 500/100}, {points[-1][1] - 500/100} meters', (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)


while True:

    values = getKeyboardInput()

    drone.send_rc_controls(vals[0], vals[1], vals[2], vals[3])
    image = np.zeros((1000, 1000, 3), np.uint8)
    points.append((values[4], values[5]))
    drawPoints(image, points)
    cv2.imshow("Drone Feed", image)
    cv2.waitKey(1)
