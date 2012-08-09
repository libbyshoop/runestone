Introduction to ardrone2.0
==========================
Getting Started
---------------
Before you start, you will need to download the files below and save all of them in a new directory.

| :download:`_init_.py<__init__.py>`
| :download:`arnetwork.py<arnetwork.py>`
| :download:`arvideo.py<arvideo.py>`
| :download:`demo.py<demo.py>`
| :download:`firsttrial.py<firsttrial.py>`
| :download:`libardrone.py<libardrone.py>`
| :download:`README<README>`
| :download:`test_libardrone.py<test_libardrone.py>`

AR.Drone2 comes with two bodies; a leaner body and one with protective foam rings which is often used while flying it indoors.
It has a rechargeable battery and a USB port. There are a few steps to connect your laptop to drone.

- Set the drone on a table. Remove the hull and insert the battery and fasten its belt.

    .. figure:: droneimages/Disconnected.JPG
           :align: center
           :scale: 50%
           :alt: image

           Disconnected

    .. figure:: droneimages/BatteryConnect.JPG
           :align: center
           :scale: 50%
           :alt: image

           Connecting the battery

    .. figure:: droneimages/Connected.JPG
           :align: center
           :scale: 50%
           :alt: image

           Battery Connected

- After connecting the battery, wait till the motors initialize. Now you can see the lights turn green.

- Insert the foam rings for a safe flying.

    .. figure:: droneimages/PlaceGuard.JPG
           :align: center
           :scale: 50%
           :alt: image

           Step 1

    .. figure:: droneimages/PlaceGuard2.JPG
           :align: center
           :scale: 50%
           :alt: image

           Step 2

- Now place the drone on the marks on the ground with the camera facing the front.

    .. figure:: droneimages/FrontWCamera.JPG
           :align: center
           :scale: 50%
           :alt: image

           Camera facing the front

    .. figure:: droneimages/Mark1.JPG
           :align: center
           :scale: 50%
           :alt: image

           Mark 1

    .. figure:: droneimages/Mark2.JPG
           :align: center
           :scale: 50%
           :alt: image

           Mark 2

    .. figure:: droneimages/OnMark1.JPG
           :align: center
           :scale: 50%
           :alt: image

           On Mark 1

    .. figure:: droneimages/OnMark2.JPG
           :align: center
           :scale: 50%
           :alt: image

           On Mark 2

- Perform a search for available wifi connections on your laptop and connect to ardrone2_003096. Wait for the laptop to connect
  to this network.

- Once the connection is successful, you can run your codes on wing.

Some functions
---------------
There are a set of functions that can be useful to you when you write your code to make drone do certain movements. This can be found in
libardrone.

takeoff(): This allows the drone to take off. This function gets the drone off the ground. In order to let it balance itself, you should give
at least 5 seconds by using the sleep function.

sleep(): This suspends execution for a given number of seconds. In order to give a more precise sleep time, you can use floating point number.

move_forward(): This moves the drone forward. Make sure you sleep it not more than 5 seconds.

move_backward(): This results in the drone moving backwards.

move_left(): This is used when you want to move the drone left.

move_right(): This function is used when you want to move the drone in the right direction.

turn_left(): This function makes the drone rotate left.

turn_right(): This function makes the drone rotate right.

reset(): This function toggles the drone emergency state. You would see the lights turn red and then green.

set_speed(): This function sets the drone speed. The default speed for drone is 0.2. In order to increase or decrease the speed, you can set the speed using floating point numbers between 0 to 1.

hover(): Make the drone hover.

land(): It makes the drone land.

halt(): This makes the drone halt.

