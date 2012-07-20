Iterative Loops Activity
========================

**COMP 123**

Overview
--------
This activity will introduce *iterative loops*, called `while` and
`for` loops, which are another way to make the computer repeat a
set of actions over and over. Get a copy of the file
`iteration.py`, which contains the code examples from this
activity.

There are two kinds of loops we will use commonly in Python:
`while` and `for`. The `while` loop contains a boolean test
expression, and then has a block of indented Python statements in
its body. It evaluates the test expression, and so long as the test
expression evaluates to `True`, Python will execute the statements
in the block, and then go back and repeat.

.. sourcecode:: python

    while test-expression:
        body



A `for` loop repeats a fixed number of times. When you create a
`for` loop, you must specify a loop variable and a sequence (a
list, string, or tuple). The `for` loop assigns its loop variable
to be the first value in the sequence, and then it performs the
statements in the body of the loop. Then, it assigns its loop
variable to be the next value in the sequence and repeats. For
lists and tuples, a `for` loop will repeat for each value; for a
string it repeats for each character in the string.

.. sourcecode:: python

    for var in sequence:
        body



While Loops
-----------

Look at the following loops, embedded in functions. For each one,
try to figure out what it does before putting it into Python. Then
check yourself by opening the `iteration.py` file and loading these
examples. Run them on some sample inputs.

.. sourcecode:: python

    # loop 1

    def printEveryOther(x):
        while x >= 0: # x is the loop variable
           print x
           x = x - 2 # when indentation stops, while loop is over
        print "Done!"
    # end of printEveryOther

.. activecode:: act_iteration_01

     # loop 1
    def printEveryOther(x):
        while x >= 0: # x is the loop variable
           print x
           x = x - 2 # when indentation stops, while loop is over
        print "Done!"
    # end of printEveryOther

.. sourcecode:: python

    # loop 2

    def printBigNums(numList):
        i = 0
        while i < len(numList): # i is the loop variable
            if numList[i] > 10:
                print i, numList[i]
            i = i + 1
        # end of while loop
    # end of printBigNums

.. activecode:: act_iteration_02

    # loop 2
    def printBigNums(numList):
        i = 0
        while i < len(numList): # i is the loop variable
            if numList[i] > 10:
                print i, numList[i]
            i = i + 1
        # end of while loop
    # end of printBigNums

You can go through the function step by step.

.. codelens:: act_iteration

    # loop 2
    def printBigNums(numList):
        i = 0
        while i < len(numList): # i is the loop variable
            if numList[i] > 10:
                print i, numList[i]
            i = i + 1
        # end of while loop
    # end of printBigNums

    printBigNums([54,65,43,10,9,3,42])

Try these:
^^^^^^^^^^

Try the following problems that use `while` loops.


#. Define a function `printSquares` that has one input parameter,
   `n`, which will be an integer. The function should use a `while`
   loop to print the squares from :math:`0^2` up to :math:`n^2`.
   See examples below.

   .. sourcecode:: python

       >>> printSquares(5)
       0
       1
       4
       9
       16
       25

   .. actex:: act_iteration_03

#. Define a function `substAll` that has three input parameters.
   The first two inputs should be values of any kind, and the third
   input should be a list. The function should use a `while` loop to
   iterate over the positions in the list (see `printBigNums` above).
   If the value at a given position is equal to the first input, then
   the function should change the list at that position to have the
   second input value. See examples below.

   .. sourcecode:: python

        >>> lista = [5, 2, 7, 1, 5]
        >>> listb = ['f', 'h', 'k', 'k', 'g']
        >>> substAll(5, 50, lista)
        >>> lista
        [50, 2, 7, 1, 50]
        >>> substAll('k', 'v', listb)
        >>> listb
        ['f', 'h', 'v', 'v', 'g']

   .. actex:: act_iteration_04


*Can you identify the loop variable(s) for each of the functions you wrote above?*

Accumulator variables
---------------------

Sometimes we need to use a loop to *accumulate* a answer. In this
case, a common pattern is to have an "accumulator variable" that is
set to some initial value before the loop, and then updated each
time through the loop. See the examples below.

.. sourcecode:: python

    def sumNums(numList):
        index = 0 # the loop variable
        total = 0 # the accumulator variable
        while index < len(numList):
            total = total + numList[index] # add next value to accumulator
            index = index + 1
        # end of while loop
        return total

.. activecode:: act_iteration_05

    def sumNums(numList):
        index = 0 # the loop variable
        total = 0 # the accumulator variable
        while index < len(numList):
            total = total + numList[index] # add next value to accumulator
            index = index + 1
        # end of while loop
        return total




Try this:
^^^^^^^^^

Write a function `countNegatives` that takes a list of numbers as
its input. Using a `while` loop and an accumulator variable, count
the number of negative numbers in the input list. See examples
below.

.. sourcecode:: python

    >>> countNegatives([2, 5, -1, 3, -6])
    2
    >>> countNegatives([1, 5,9])
    0

.. actex:: act_iteration_06

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


For loops
----------

For loops repeat a fixed number of times. The number of times
corresponds to the length of the specified sequence: list, string,
or tuple.

The range function
^^^^^^^^^^^^^^^^^^^

Python has a built-in function for building lists of numbers. It
takes in one, two, or three inputs. Given one input, it generates a
list of integers from 0 up to, but not including, the input number.
Given two inputs, it generates a list of integers from the first
input up to, but not including, the second, and given three inputs
it generates a list of integers from the first input up to, but not
including the second, skipping the third integer steps each time.
Try out the examples below in the interactive shell, and make up
some of your own.

.. sourcecode:: python

    range(5)
    range(10, 20)
    range(10, 40, 4)
    range(12, 6, -1)

.. activecode:: act_iteration_09

    print(range(5))
    print(range(10, 20))
    print(range(10, 40, 4))
    print(range(12, 6, -1))



For loop examples
^^^^^^^^^^^^^^^^^^

We tend to create `for` loops in one of three ways: using the
`range` function to generate a list, looping over elements of an
existing list, and looping over elements of an existing string.
Look in the `iteration.py` file for examples that demonstrate these
patterns: `catNTimes`, `countLetters`, and `mult2List`. Try each
function on several sample inputs until you understand how they
work. If you need help figuring out what is happening, consider
adding in print statements that show you the value of the loop
variable and other local variables.

Try these:
^^^^^^^^^^

Try writing the following functions that use `for` loops.


#. Redo the `printSquares` function from earlier, using a `for`
   loop instead of a `while` loop.

   .. actex:: act_iteration_10

#. Create a function `collectNums` that takes a list as its input.
   The values in the list may be of any type. This function should use
   a `for` loop to iterate through the values in the list. It should
   include an accumulator variable that holds a list. The loop should
   add a value from the input list to the accumulator list if that
   value is a number. Return the new list.

   You can check the type of the value in a variable in one of the two
   ways shown below, along with some examples of how collectNums
   should work.

   .. sourcecode:: python

       >>> isinstance(12, int)
       True
       >>> v = 25.0
       >>> isinstance(v, int)
       False
       >>> type(v) == float
       True
       >>> isinstance(v, (int, float))
       True
       >>> listA = [3, 'a', 4, False, 5, "foo"]
       >>> newList = collectNums(listA)
       >>> newList [3, 4, 5]

   .. actex:: act_iteration_11

#. Redo the `traceSquare` function, using a `for` loop instead of a
   `while` loop.

   .. actex:: act_iteration_12

The break Statement
-------------------


Sometimes you want a program to loop, but if certain circumstances
occur, you want the loop to end before finishing its iterations.
The `break` statement causes the current loop to stop immediately
at the point where the `break` occurred. The program continues on
with any Python statements that come after the loop.

The program below breaks out of the `for` loop as soon as the total
gets above 100.

.. sourcecode:: python

    def cappedTotal(numList):
        """Takes in a list of numbers and adds the numbers up. If it gets to a result that is more than 100, then the loop stops and it returns 100"""
        total = 0
        for val in numList:
            total = total + val
            if total > 100:
                total = 100
                break
            # end if statement
        # end for loop
        return total

.. activecode:: act_iteration_13

    def cappedTotal(numList):
        """Takes in a list of numbers and adds the numbers up. If it gets to a result that is more than 100, then the loop stops and it returns 100"""
        total = 0
        for val in numList:
            total = total + val
            if total > 100:
                total = 100
                break
            # end if statement
        # end for loop
        return total



Try this:
^^^^^^^^^

Write a function `countUpTo` that takes an item of any type and a
list as inputs. The function should loop through the list, looking
for an occurrence of the item. When it finds an occurrence, the
function should break out of the loop. At the end of the loop,
whether it breaks out or exits normally after all iterations, the
function should print the number of times the loop repeated.

.. sourcecode:: python

    >>> listA = [3, 2, 5, 10]
    >>> countUpTo(5, listA)
    Loop repeated 3 time(s)
    >>> countUpTo(3, listA)
    Loop repeated 1 time(s)
    >>> countUpTo(12, listA)
    Loop repeated 4 time(s)

.. actex:: act_iteration_14




