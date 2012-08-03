Booleans and Conditionals Activity
==================================

**COMP 123**

Overview
--------

This activity will practice with the Boolean data type, and
conditional statements that let the computer choose an action.

Boolean data type
-----------------

The boolean data type is a very special one in most programming
languages. A boolean value is either `True` or `False`. We use
booleans to ask questions about data in a program, and to write
programs that can choose among alternative actions.

Boolean expressions
^^^^^^^^^^^^^^^^^^^

We can ask questions using functions that return true/false
answers, or with a set of boolean comparison operators. These form
boolean *expressions* that evaluate to `True` or `False`. The most
common boolean operators are shown in the table below.

      +--------------+--------------------------------------------------------------------------------+
      |  `A == B`    |     Takes two expressions, `A` and `B`, and evaluates to                       |
      |              |     `True` if the value of `A` is equal to the value of `B`.                   |
      +--------------+--------------------------------------------------------------------------------+
      |  `A != B`    |     Takes two expressions, `A` and `B`, and evaluates to                       |
      |              |     `True` if the value of `A` is not equal to the value of `B`.               |
      +--------------+--------------------------------------------------------------------------------+
      |  `A <= B`    |     Takes two expressions, `A` and `B`, and evaluates to                       |
      |              |     `True` if the value of `A` is less than or equal to the value of `B`.      |
      |              |                                                                                |
      |              |     .. note:: characters and strings are ordered more or less                  |
      |              |              alphabetically: a string that comes before another in alphabetical|
      |              |              order is seen as *less than*.                                     |
      +--------------+--------------------------------------------------------------------------------+
      |  `A < B`     |     Similar to previous, but the values cannot be equal                        |
      +--------------+--------------------------------------------------------------------------------+
      |  `A >= B`    |     Similar to previous, but "greater than or equal to"                        |
      +--------------+--------------------------------------------------------------------------------+
      |  `A > B`     |     Similar to previous, but "greater than"                                    |
      +--------------+--------------------------------------------------------------------------------+
      |  `A in B`    |     For strings, asks if the first value appears in the                        |
      |              |     second value as a substring                                                |
      +--------------+--------------------------------------------------------------------------------+


Try this:
^^^^^^^^^

Type each of the statements or expressions below in the editor.
Add a comment after each one that describes
what question is being asked, and what the answer should be.

.. sourcecode:: python

    #. first we'll assign three variables to values
    x = 25
    y = 30
    s ='boolean'
    # now we'll ask questions about them
    print(x <= y)
    print(x + 5 > y)
    print(x %2 == 0)
    print(s[2] > 'g')
    print(len(s) == 7)
    print('e' in s)
    print('c' in s)
    print('boo' in s)

.. actex:: act_condit_1




Boolean operators
^^^^^^^^^^^^^^^^^

We can also put boolean expressions like the ones above together
using the boolean operators: `and`, `or`, and `not`. The table
below describes how these operators work.

      +--------------+------------------------------------------------------------------------------+
      |  `A and B`   |    Evaluates to `True` if both the value of `A` and the                      |
      |              |    value of `B` are `True`, otherwise it evaluates to `False`                |
      +--------------+------------------------------------------------------------------------------+
      |  `A or B`    |    Evaluates to `True` if at least one of `A` or `B`                         |
      |              |    evaluates to `True`                                                       |
      +--------------+------------------------------------------------------------------------------+
      |  `not A`     |    Evaluates to `True` if `A` evaluates to `False`, and to                   |
      |              |    `False` if `A` evaluates to `True`                                        |
      +--------------+------------------------------------------------------------------------------+


Try this:
^^^^^^^^^

Type each of the following into the shell. Which of the
following are `True`, and which `False`? Can you explain why?

.. sourcecode:: python

    x=25
    y=30
    print((x % 5 == 0) and (y % 5 == 0))
    print((s[0] == 'b') or (len(s) >= 10))
    nums = [15, 20, 25, 30]
    print((x in nums) and not (y in nums))
    print((x >= 15) and (x <= 50))


.. admonition:: True or False

    .. mchoicemf:: question1_01
       :answer_a: True
       :answer_b: False
       :correct: a
       :feedback_a: x and y when divided by 5 give a remainder of 0.
       :feedback_b: x and y when divided by 5 give a remainder of 0.

       (x % 5 == 0) and (y % 5 == 0)

    .. mchoicemf:: question1_02
       :answer_a: True
       :answer_b: False
       :correct: a
       :feedback_a: only the first expression holds true
       :feedback_b: only the first expression holds true

       (s[0] == 'b') or (len(s) >= 10)

    .. mchoicemf:: question1_03
       :answer_a: True
       :answer_b: False
       :correct: b
       :feedback_a: y is in nums
       :feedback_b: y is in nums

       (x in nums) and  not (y in nums)

    .. mchoicemf:: question1_04
       :answer_a: True
       :answer_b: False
       :correct: a
       :feedback_a: both expressions hold true
       :feedback_b: both expressions hold true

       (x >= 15) and (x <= 50)


Conditional statements
^^^^^^^^^^^^^^^^^^^^^^

We often use boolean expressions in conditional statements, `if`
statements, to cause the computer to choose one or another sets of
actions. Look at sections 5.4 through 5.6 in Downey to remind
yourself of the syntax for `if` statements.

Try this:
^^^^^^^^^

Look at the example below. Try to
figure out what it's value might be. Then put it in your Python
file, and run it.

.. sourcecode:: python

    x=50
    y=100
    if x > y:
        print x, y
    elif y > x:
        print y, x
    else:
        print x


.. fillintheblank:: actcondit
        :correct: 100 50

        The correct answer is ___

*How the code works*

.. codelens:: act_condit

     x=50
     y=100
     if x > y:
        print x, y
     elif y > x:
        print y, x
     else:
        print x


Activity 1: Cropping Values
----------------------------

Create a function called `crop` that has one parameter variable.
When `crop` is called, it should be passed a number as input. If
the number is between 1 and 10, `crop` should return the number
itself. If it is less than 1, it should return 1, and if it is
greater than 10, then it should return 10. This way, it converts
any number given to it into the range from 1 to 10. Here are some
examples showing what the function should do for some sample
inputs:

.. sourcecode:: python

    >>> crop(8)
    8
    >>> print crop(-1), crop(5), crop(50)
    1 5 10


.. actex:: act_condit_2


Activity 2: Tele-operated Robot
-------------------------------

"Tele-operation" of robots means controlling a robot from a
distance. This is used for entertainment and education: some
science museums have robots you can connect to over the Internet
and operate. It is also used for hazardous situations and
environments: bomb squads, search and rescue, deep-sea exploration,
space exploration.

Create a little function that could be used for simple
tele-operation of the Scribblers. The function, `go`, should have
one input parameter. When it is called, the user should pass in a
single string, one of: `"f"`, `"b"`, `"l"`, and `"r"`.

If the string is `"f"` then the robot should move forward for one
second. If the string is `"b"` then the robot should move backward
for one second. If the string is `"r"` then the robot should turn
about forty five degrees to the right , and if the string is `"l"`
then the robot should turn about forty five degrees to the left.
Test your program by having the robot navigate all the way around
the classroom.

.. actex:: act_condit_3

Challenge Activities
--------------------


#. Create a function `middleValue` that has three parameter
   variables: it should be passed three numbers when it is called. The
   function should use `if` statements, including nesting one `if`
   inside another, to determine which of the three numbers is the
   middle value. That value should be returned as the value of the
   function.

   .. sourcecode:: python

       >>> middleValue(5, 2, 77)
       5
       >>> middleValue(-10, 50, 57)
       50
       >>> middleValue(-1, -6, -3)
       -3

   .. actex:: act_condit_4


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

#. Letter grades in the US are commonly assigned according to
   "deciles:" a score that is greater than or equal to 90% is given an
   A, a score that is greater than or equal to 80%, but less than 90%
   is given a B, a score similarly between 70% and 80% is a C, a score
   similarly between 60% and 70% is a D, and anything below 60% is an
   F.

   Write a function `percentToLetter` that has one input parameter. It
   should be passed a percentage (which may be a real number) as its
   input, and it should return a string containing the corresponding
   letter grade.

   .. actex:: act_condit_6
