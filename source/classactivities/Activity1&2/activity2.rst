Data Types
==========

**COMP 123**

Operations on Numbers
----------------------

Python has two main kinds of numbers: integers, and real, or
floating point, numbers. (There are other kinds of numbers, as
well, but we probably won't use any of them). Below is a table
showing basic numeric operations. Many more common mathematical
operations are in the math module, which you can add in when you
need it.



    +--------------------------+---------------------------------------------------+
    | Example                  | Meaning                                           |
    +==========================+===================================================+
    | 3 + 12                   | Adds two numbers, returning the result            |
    +--------------------------+---------------------------------------------------+
    | 45 - 19                  | Subtracts second from first, returning the result |
    +--------------------------+---------------------------------------------------+
    | 5\*100                   | Multiplies two numbers, returning the result      |
    +--------------------------+---------------------------------------------------+
    | 55.0 / 2                 | Divides first by the second, returning the result |
    +--------------------------+---------------------------------------------------+
    |  30 % 4                  | Computes the remainder of first divided by second |
    +--------------------------+---------------------------------------------------+
    |  2**3                    | Raises first to the power of the second           |
    |                          |                                                   |
    +--------------------------+---------------------------------------------------+
    |  max(1, 5, 3)            | A function that returns the largest of values     |
    +--------------------------+---------------------------------------------------+
    |  min(1, 5, 3)            | A function that returns the smallest of values    |
    +--------------------------+---------------------------------------------------+
    |  abs(-3)                 | A function that returns the absolute value of     |
    |                          |  its argument                                     |
    +--------------------------+---------------------------------------------------+
    |  int(3.2)                | Converts its argument to an integer               |
    +--------------------------+---------------------------------------------------+
    |  float(2)                | Converts its argument to a floating point         |
    +--------------------------+---------------------------------------------------+


Integers and floats are treated as different, though related, kinds
of data. This is why we have explicit operators to convert from one
type to the other.

 .. note:: Floating point results can differ from one machine to another.
           We will say more later about controlling the appearance of floating point output.
           See also `Floating Point Arithmetic Issues and Limitations`_ for a full discussion of some of the subtleties of floating point numbers and their representations.


.. _Floating Point Arithmetic Issues and Limitations: http://docs.python.org/release/3.1.5/tutorial/floatingpoint.html#tut-fp-issues

Try the following in the editor below to see how division and remainder works. Try some of the examples in the table above.

.. sourcecode:: python

    a = 25.0/3
    print a
    print(25.0/3)   #note that this is a shortcut for the two lines above.
    print(25.0/3.0) #we don't often use a syntax like this in a real program.
    print(25/3.0)   #We usually use the top two lines.
    print(25/3)
    print(25%3)

.. actex:: act_intro_3





Try a new program
------------------

Consider the problem of making change: figuring out how many bills
and coins to give someone to make a specific amount of money. This
example asks you to make a program to solve this problem. You might
start by discussing this question with a neighbor, and developing
together your ideas for how to solve the problem, in English or
pseudocode. The key idea to making change is to take the quotient
and remainder of an amount by the next monetary unit. For example,
given $7.32, represented as 732 cents. If we take the quotient of
732 by 100 (for one dollar bills), then we get 7, and the remainder
of 732 divided by 100 is 32. Then take the part left over, and
repeat for the next coin: quarters. Divide 32 by 25, and get 1, and
the remainder is 7 cents. Continue in this manner.

Now, see if you can write a Python program, a series of expressions
or statements in Python, that do this calculation and print out the
results.
Define a variable, ``money``, that contains a money amount, in cents
(like 732 for $7.32, for example).

Then, create a series of Python statements that calculate and print
how to give change for the money value, in dollars, quarters,
dimes, nickels, and pennies. The best solution will use integer
division, int() function and the remainder operation.

*Please include comments about what each statement of your program is accomplishing.*

Below is an example of what might print when this program is run:

.. sourcecode:: python

    Making change for 732 cents:
    Dollars: 7
    Quarters: 1
    Dimes: 0
    Nickels: 1
    Pennies: 2


Once you get the program working for 732, change the value of
``money`` and test it on other values to be sure it works
more generally.

Lastly, have your program take as input the value that you want to make change.

.. actex:: act_intro_4

