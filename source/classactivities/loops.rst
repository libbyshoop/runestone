Loops Activity
==============

**COMP 123**

Overview
--------

We'll try writing some different kinds of loops with this
activity.

Loop!
-----

There are two kinds of loops we will use commonly in Python:
`while` and `for`. The `while` loop takes a boolean expression, an
expression that asks a question, and then has a block of indented
Python statements. It tests the expression, and so long as it
evaluates to true, Python will execute the statements in the block,
and repeat. A `for` loop repeats for a fixed number of times. Each
time through it sets its loop variable to be the next value in the
loop sequence. Look at the examples and questions below.

Look at the following functions, which use loops to repeat a
process. Try these out in the activecode until you understand what the loop is doing.

.. note:: `perfectSquares` contains a common pattern for loops: it
            uses a variable, `ansLst` as an "accumulator" to hold the part of
            the answer that has been computed so far. At the end of the loop
            `ansLst` contains the answer.


.. sourcecode:: python

    def divByTwo(x):
        """Takes an input integer, x, and prints x and the
            result of repeatedly dividing x by 2. It stops when x becomes <= to
            zero"""
        while x > 0:
            print x
            x = x / 2
            # end of while
        print x
    # end of divByTwo


.. activecode:: act_loop_01



.. sourcecode:: python

    def perfectSquares(n):
        """Takes a non-negative input integer, n,
        and creates a list containing the squares of the numbers from zero
        to n"""
        ansLst = []
        for i in range(n+1): # Do you know why I put n+1 here?
            ansLst.append(i**2)
            # end of for loop
        return ansLst
    # end of perfectSquares

.. activecode:: act_loop_02



.. sourcecode:: python

    def printAlpha(string):
        """Takes a string as input, and loops
        through the characters of the string. For each character, if it is
        an alphabetic character, then it is printed. All characters are
        printed on one line, separated by spaces"""
        for c in string:
            if c.isalpha():
                print c,
            # end of if
        # end of for loop
        print
    # end of printAlpha

.. activecode:: act_loop_03






Now you try it:
---------------


#. Create a function called `evensToN` that takes a single number,
   `n`, as input, and prints the even numbers from 1 to `n`.

   .. actex:: act_loop_04

#. Create a version of the function from the recursion activity:
   `printApproach`. This function that takes two numbers as input.
   Within, use a `while` loop that repeats until the first number is
   greater than the second number. Each time through the loop, print
   the numbers, then add one to the first number, and subtract one
   from the second number.

   .. actex:: act_loop_05

Turtle Activities with loops
-----------------------------

Write the programs in Wing to have the turtle perform these activities. Try out these exercises in writing
functions.

#. Write a program that draws a row of bricks. For this you need to first define a function that helps you draw a brick and then generate a row of bricks. The row of bricks should be centered in the window and should use the following parameters:

    brickwidth: The width of the brick,

    brickheight: The height of each brick.

    .. figure:: Images/turtle.png
        :align: center
        :alt:



#. Implement a `yoyo` function that makes the turtle move forward
   and then back twice. It should take two inputs, the speed and how long to wait before returning.

   .. actex:: act_floops_8

#. Create a function `moveAndPic` that takes in a turn time as its
   input. It should have the turtle take a picture, show the
   picture, and then turn left for the input turn time. It should
   repeat this process four times (you don't have to use a loop here,
   but you may if you've already figured them out).

   .. actex:: act_floops_9

#. Create a function, `driveSquare` that tries to have the turtle
   move in a square. It should take a speed value as its input.

  .. actex:: act_floops_10

Loops
^^^^^

Reading the Loops section above for information about the basic
structure of `while` and `for` loops. Then try the following:


#. Modify the `moveAndPic` function from earlier so it also takes
   in a number `n`, and uses a loop to repeat the turning and taking
   pictures `n` times, instead of 4 times.

   .. actex:: act_floops_11

#. Using the `yoyo` and `dance` functions from before, create a
   function called `danceRoutine` that repeats some combination of
   yoyo-ing and dancing some number of times.

   .. actex:: act_floops_12

#. Create a function called `keepYoing` that takes an input number
   `n`. It should call the `yoyo` function `n` times. Choose your kind
   of loop, or recursion, to make this work.

   .. actex:: act_loop_08

#. Using the `yoyo`, `keepYoing`, and `dance` functions from
   before, create a function called `danceRoutine` that repeats some
   combination of yoyo-ing and dancing some number of times. Make the
   number of times to repeat be an input to `danceRoutine`.

   .. actex:: act_loop_09

#. Create a function `turnAndBeep` or `turnAndPic` that takes in a
   number `n`, and uses a loop to repeatedly have the turtle turn to
   the left a fixed distance.

   .. actex:: act_loop_10
