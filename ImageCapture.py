from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()

print(f'{drone.get_battery()} % remaining')

drone.streamon()

while True:
    image = drone.get_frame_read().frame
    image = cv2.resize(image, (360, 360))
    cv2.imshow("Drone Feed", image)
    # add a slight delay so we see the frame before it goes away
    cv2.waitKey(1)
