Flying ardrone2
===============

This is a typical first program with ardrone2.

.. sourcecode:: python

    import libardrone
    from time import sleep

    drone = libardrone.ARDrone()

    drone.takeoff()
    sleep(5)
    drone.move_forward()
    sleep(3)
    drone.turn_right()
    sleep(2)
    drone.hover()
    sleep(2)
    drone.move_up()
    sleep(2)
    drone.move_down()
    sleep(2)
    drone.land()
    sleep(3)
    drone.halt()

