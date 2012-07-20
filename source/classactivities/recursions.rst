Writing Recursive Functions Activity
====================================

**COMP 123**


Form a group of two or three, and you will be assigned one of the problems below.
Write a solution to the problem you've been given, using recursion,
and test it thoroughly. When you are satisfied, call me over to see your solution, and then post
your solution to the "Recursive Functions" topic of the Questions
forum. Then use the remaining time to complete as many of the
others as you can. Upload all your solutions to the Moodle
assignment.

Problem 1: multsOfFive
----------------------

Define a function `multsOfFive` that takes a number, `n` as its
input parameter. It should build and return a list containing the
multiples of five from 0 up to `n` (including `n` if it is a
multiple of five).

The examples below illustrate how the function should work, but
they don't necessarily exercise the function.

.. sourcecode:: python

    >>> multsOfFive(13)
    [0, 5, 10]
    >>> multsOfFive(55)
    [0, 5, 10, 15,20, 25, 30, 35, 40, 45, 50, 55]

.. actex:: act_recurfunc_01


Problem 2: forwardNPaces
------------------------

Write a recursive function `forwardNPaces` for controlling the
robot. The function should have one input parameter, `n`. The
purpose of the function is to let us specify a number of paces, and
for the robot to move forward that number of paces. A pace should
be the distance the robot moves forward at speed 0.75 and time 0.5
seconds. The robot should stop for between 0.25 and 0.5 seconds
between moves.

The examples below illustrate how the function should work, but
they don't necessarily exercise the function.

.. sourcecode:: python

    >>> forwardNPaces(3)
    >>>

.. actex:: act_recurfunc_02



Problem 3: sumList
------------------

Write a recursive function `sumList` that takes a list of numbers
and an index into the list as its inputs. It should add together
and return the numbers in the list starting with the input index and
going to the end of the list.

The examples below illustrate how the function should work, but
they don't necessarily exercise the function.

.. sourcecode:: python

    >>> sumList([5, 1, 8], 0)
    14
    >>> sumList([+12, -3, +1, -4, +5, -1],3)
     0
     >>> sumList([12], 0)
     12
     >>> multList([], 100)
     0

.. actex:: act_recurfunc_03


Problem 4: printApproach
------------------------

Write a recursive function `printApproach` that takes two numbers
as its inputs. The first number should be less than or equal to the
second number. The function should print two columns of numbers.
The first column should show the low number gradually increasing,
the second column should show the high number gradually decreasing.
The function should stop when the low number becomes larger than
the high number.

The examples below illustrate how the function should work, but
they don't necessarily exercise the function.

.. sourcecode:: python

    >>> printApproach(3, 13)
    3   13
    4   12
    5   11
    6   10
    7   9
    8   8
    >>> printApproach(-3, +3)
    -3  3
    -2  2
    -1  1
     0  0

.. actex:: act_recurfunc_04

Problem 5: sumUser
------------------

Write a recursive function `sumUser` that takes no input parameters
at all! This may seem impossible, but this function gets the value
that determines whether to recur or not by asking the user for it.
This function should first ask the user to enter an integer (using
`input` or `raw_input`). If the user enters zero, then the
function should return zero. Otherwise, it should call itself
recursively, getting some number back, and should return the number
the user entered plus the recursive sum.

The examples below illustrate how the function should work, but
they don't necessarily exercise the function.

.. sourcecode:: python

    >>> sumUser()
    Enter an integer (0 to quit): 2
    Enter an integer (0 to quit): 5
    Enter an integer (0 to quit): -3
    Enter an integer (0 to quit): 0
    4
    >>> sumUser()
    Enter an integer (0 to quit): 2
    Enter an integer (0 to quit): 2
    Enter an integer (0 to quit): 2
    Enter an integer (0 to quit): 2
    Enter an integer (0 to quit): 0
    8

.. actex:: act_recurfunc_05

Problem 6: countSet
-------------------

Write a recursive function `countSet` that takes three input
parameters. The first two inputs should be list: `target` and
`data`, and the third input should be an `index` into the `data`
list. The function should use recursion to count the number of
elements in the `data` list that appear in the `target` list,
starting with the `index` into `data` and going on to the end of
`data`. Use the operator `in` to figure out whether an element of
`data` occurs in `target`.

The examples below illustrate how the function should work, but
they may not completely test every part of your function.

.. sourcecode:: python

    >>> countSet(['f', 'g', 'h'], ['a', 'f', 't', 'g', 'o'], 0)
    2
    >>> countSet([5, 1, 12], [9, 2, 6, -12, 16], 0)
    0
    >>> countSet([5, 1, 12], [1, 5, 12, 5, 12], 2)
    3

.. actex:: act_recurfunc_06

Problem 7: shimmy
-----------------

Write a recursive function that makes the robot wiggle left and
right a certain number of times. The function should take in one
input value, `n`. At the heart of this function is a movement
similar to the `sayNo` problem from Homework 1. The robot should
turn left in place for a fixed amount of time, then right for twice
that amount of time, and then left again for the initial fixed
amount of time. However, in this case the robot should repeat that
action {n} times.

.. sourcecode:: python

    >>> shimmy(5)
    >>>

.. actex:: act_recurfunc_07