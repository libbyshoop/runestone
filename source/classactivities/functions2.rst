Functions Practice Activity
---------------------------
**COMP 123**

Overview
~~~~~~~~~

This activity follows on the earlier functions activity, giving you
more practice with defining functions, and looking particularly at
how parameter variables and local variables work, and how inputs
and return values work.

It will also ask you to practice with writing functions that are
called by other functions.

.. note:: All the code that is in this activity may be found in the

          :download:`functions2.py <functions2.py>` file! Open this file in an IDLE editor window.

Variables: global, parameter, and local
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open a new editor window- this will become the basis of the file
that you will hand in for this activity, so be sure to put your
name in its file name when you save it. Copy the code below from
the functions2.py file (variable assignment, function definition,
and call to function) into the new editor window. Then run the
script using "Run Module", and see what happens.

Global variables are the variables you define outside of any
function definition, either typing the variable assignment into the
interactive shell, or putting it in a script, outside of a
function. In the example below, *x* is a global variable. Global
variable assignment go into the "global namespace", and may be
accessed by any other Python script, statement, expression, or
function that occurs *after* the assignment takes place. Thus,
*sillyFn* can refer to *x* inside its body.

.. sourcecode:: python

    x = 35
    def sillyFn(a): # defining the function
        b = x - 10 * a
        return b
    print sillyFn(-2) # calling the function, and printing what it returns

.. codelens:: act_functions2

    x = 35
    def sillyFn(a): # defining the function
        b = x - 10 * a
        return b
    print sillyFn(-2) # calling the function, and printing what it returns

When you define a function, you declare a set of parameter
variables. These variables do not have values yet (not at the time
the function is defined). They will take on values only when the
function is actually called. The variable *a* above is a parameter
variable.

When the function is called, as it is at the bottom of the example
above, then a new, local namespace is created, just for that call.
To use the "Happy Robot" metaphor, each happy robot has its own
space to keep its variables. This is a local, private space, that
belongs only to this particular happy robot: only to this function
call. In the example above, a local namespace is created, and *a*
is assigned the value of *-2* in that namespace. The variable *a*
does not exist in the global namespace (you can try typing *a* into
the shell after running this script: Python will tell you it
doesn't know a value for *a*).

The function *sillyFn* also has a local variable, *b*. Local
variables also exist only in the function call's namespace. When
the function call is done, its namespace goes away, along with the
assignment of local and parameter variables to values.

When a function call "happy robot" sees a variable in its body, it
first looks to see if that variable has an assigned value in its
own local namespace. If it does, then it uses that value. If it
doesn't, then it looks to the global namespace outside to find a
value.

Try this:
^^^^^^^^^

Add the code below to the file from before. Try to predict what
values will be printed before running the script. Check your work
by running the script.

.. sourcecode:: python

    #these 3 variables are 'global' in this script
    a = 6
    b = 15
    c = 25
    def moreSilly(c, d):        #c, d become local to the function
        print a
        print c
        b = 2 * d
        print b
    moreSilly(1, 4)
    print b

.. activecode:: act_func2_1

    #these 3 variables are 'global' in this script
    a = 6
    b = 15
    c = 25
    def moreSilly(c, d):        #c, d become local to the function
        print a
        print c
        b = 2 * d
        print b
    moreSilly(1, 4)
    print b


Fruitful functions: handling returned values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a simple program made up of two functions. The first
function does some work and prints the result, it is not a
"fruitful function." The second function does a calculation and
returns a value, it *is* a fruitful function. (Note: This code was
used in a video Prof. Fox made that talks about this same
material.)

.. sourcecode:: python

    def main():
        x = 5
        ans = helper(x, 10)
        print ans

    def helper(a, b):
        return 2 * b + a

.. actex:: act_func2_2

    def main():
        x = 5
        ans = helper(x, 10)
        print ans

    def helper(a, b):
        return 2 * b + a



When you call *helper*, you get a value back. If you call it in the
interactive shell, Python automatically displays the returned
value:

.. sourcecode:: python

    >>> helper(6, 3)
    12
    >>>


You can use a call to *helper* in a larger expression, and the
value returned by *helper* takes the place of the function call in
the expression:

.. sourcecode:: python

    >>> helper(6, 3) * 4
    48
    >>> z = helper(1, 2)
    >>> z
    5
    >>>


In order to keep the value of a call to *helper* around for later
use, we must assign a variable to catch *helper's* value. In the
example just above, we assigned *z* to hold that value. In the
original program, *main* assigns *ans* to hold that value.



Try this:
^^^^^^^^^

Try removing the `ans =` part from *main*, and see what happens.

On the other end, a function like *helper* can only be fruitful if
it explicitly *returns* a value. If it *prints* the value, then it
won't work.

.. actex:: func2_3

Try this:
^^^^^^^^^

Change helper so it says *print* instead of *return*. Then call
*main* and see what happens, and try the examples above, as well.
The *print* operation displays a value, but does not give it back
to Python for further use.

.. actex:: act_func2_4

Functions that call other functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We build programs in Python out of collections of functions. Many
functions must call other functions to help perform their task.
Because writing programs accurately is difficult and
time-consuming, one program design principle is to avoid writing
the same code over and over. If you write the exact same statements
in more than one place, then you have to debug each place
separately. it might be worth your time to package those statements
as a function, so that you can debug it once, and then only have to
call the function for every use.

Suppose we want a program to help a carpet company to generate an
estimate for carpeting a house. The company needs to take in the
dimensions of three rooms, and the cost per square foot of
carpeting for each room. It should then print, for each room, the
number of square feet for the room, and the cost for that room. It
should print the total cost at the bottom. I've given you the
(rather complicated) main function below:

.. sourcecode:: python

    # this is a bit ugly, but bear with it
    def carpetEstimate(wid1,
    len1, price1, wid2, len2, price2, wid3, len3, price3):
        area1 = rectArea(wid1, len1)
        cost1 = roomCost(area1, price1)
        area2 = rectArea(wid2, len2)
        cost2 = roomCost(area2, price2)
        area3 = rectArea(wid3, len3)
        cost3 = roomCost(area3, price3)
        print "Room 1"
        print " Area =", area1
        print " Cost =", cost1, "dollars"
        print "Room 2"
        print " Area =", area2
        print " Cost =",cost2, "dollars"
        print "Room 3"
        print " Area =",area3
        print " Cost =", cost3, "dollars"
        print "------------"
        print "Total cost =",cost1 + cost2 + cost3, "dollars"

.. activecode:: act_func2_5

    # this is a bit ugly, but bear with it
    def carpetEstimate(wid1,
    len1, price1, wid2, len2, price2, wid3, len3, price3):
        area1 = rectArea(wid1, len1)
        cost1 = roomCost(area1, price1)
        area2 = rectArea(wid2, len2)
        cost2 = roomCost(area2, price2)
        area3 = rectArea(wid3, len3)
        cost3 = roomCost(area3, price3)
        print "Room 1"
        print " Area =", area1
        print " Cost =", cost1, "dollars"
        print "Room 2"
        print " Area =", area2
        print " Cost =",cost2, "dollars"
        print "Room 3"
        print " Area =",area3
        print " Cost =", cost3, "dollars"
        print "------------"
        print "Total cost =",cost1 + cost2 + cost3, "dollars"



Try this:
^^^^^^^^^

Define a simple, fruitful function, *rectArea*, that takes in the
width and length of a rectangle and returns its area. Also define a
simple function *roomCost*, that takes in the the area of a room and the price
per square foot of carpeting for the room, and it returns the total cost for that room.

.. actex:: act_func2_6

Try this:
^^^^^^^^^

You probably wrote very simple functions for the previous step,
that just multiplied the input values together. Suppose that the
carpet company decides that it must charge customers for full feet
distances. So a room that measures 14.25 feet in length and 12.8
feet in width should be charged as a 15 by 13 room. Modify your
`rectArea` function so that it rounds up to the nearest integer and
computes the area based on that. Notice that making this change
once, in the `rectArea` function, is much easier than trying to
make the change in each place in `carpetEstimate` where `rectArea`
is called. Having the function defined saves work!

.. actex:: act_func2_7