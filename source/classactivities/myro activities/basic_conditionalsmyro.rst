from basic conditionals
=======================

#. There are several different ways for generating random numbers
   in Python. The `random` module contains a function `random` that
   returns a random value between 0.0 and 1.0. For convenience, the
   Myro module also contains a function, called `randomNumber()` that
   returns a random value between 0.1 and 1.0.

   Create a function called `randomMove` using Myro and the
   Scribblers. It should generate two random values between 0.0 and
   1.0, assigning them to variables. These values will be speeds for
   the left motor and the right motor of the robot. It should then use
   the `motors` command to run the robot for two seconds with those
   speeds. Use the `wait` command to control the two seconds of
   running, and then use `stop` to turn the motors off. (Google Myro
   Reference if you need help using these functions).

   *Extra:* Can you convert the random values to the range from -1.0
   to +1.0, and try the function with those values? How does it
   differ?

   .. actex:: act_condit_5

from function loops
===================
Myro
----

Get your hands on a robot, and try out these exercises in writing
functions.


#. Look at the following function. Try to figure out what it will
   do, then try it out to check yourself.

   .. sourcecode:: python

       def dance(speed):
          beep()
          turnRight(speed, 1)
          beep()
          turnLeft(speed,2)
          beep()
          turnRight(speed, 2)
          beep()
          turnLeft(1)
          beep()
          beep()
          beep()
          stop()

   .. actex:: act_floops_8

#. Implement a `yoyo` function that makes the robot move forward
   and then back twice. It should take two inputs, the speed for the
   robot and how long to wait before returning.

   .. actex:: act_floops_9

#. Create a function `moveAndPic` that takes in a turn time as its
   input. It should cause the robot to take a picture, show the
   picture, and then turn left for the input turn time. It should
   repeat this process four times (you don't have to use a loop here,
   but you may if you've already figured them out).

   .. actex:: act_floops_10

#. Create a function, `driveSquare` that tries to have the robot
   move in a square. It should take a speed value as its input. Note
   that Real Robots Don't Drive Straight, so be forgiving!

  .. actex:: act_floops_11

Myro from iteration
===================
While loops in Myro
--------------------

Get your hands on a robot, and try out these exercises in writing
functions.


#. To trace a square, as you did in an earlier activity, the robot
   must move forward a fixed time, turn left a fixed time that is more
   or less 90 degrees, and then repeat that process four times. Create
   a function `traceSquare` that takes no inputs (or you could specify
   the forward time, and therefore the size of the square). It should
   use a `while` loop to repeat the forward-turn left movement four
   times.

   .. actex:: act_iteration_07

#. Look in the online Myro Reference (put 'Myro Reference' into
   Google) to see the `timeRemaining` function form Myro provides. Use
   this function as the test expression in a `while` loop to write a
   function called `circle` that takes one input parameter. The input
   should be a number of seconds, and the function should make the
   robot move in a circle for the input number of seconds. Note that
   the easiest way to make the robot circle is to use the `motors`
   command and specify a slower speed for the left motor compared to
   the right motor.

   .. actex:: act_iteration_08

JES Intro
=========
Most of these functions are integrated into Myro, [1]_ so you can
use Calico to do some of this, but

.. [1]
   Mark Guzdial is involved in both the Myro and JES projects