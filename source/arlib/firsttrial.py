import libardrone
from time import sleep

drone = libardrone.ARDrone()

drone.takeoff()
sleep(3)
drone.move_forward()
sleep(2)
drone.land()
sleep(3)
drone.halt()