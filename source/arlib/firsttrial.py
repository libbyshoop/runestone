import libardrone
from time import sleep

drone = libardrone.ARDrone()

drone.takeoff()
sleep(5)
drone.move_forward()
sleep(3)
for i in range(3):
    drone.turn_left()
sleep(2)
drone.hover()
sleep(2)
drone.move_up()
sleep(2)
drone.move_down()
sleep(2)
drone.hover()
sleep(2)
drone.land()
sleep(3)
drone.halt()