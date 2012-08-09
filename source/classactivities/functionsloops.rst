Functions and Loops Activity
============================

**COMP 123**

Overview
--------

These activities will practice with writing functions, both in
plain Python, and will introduce loops, both `while`
and `for` loops, which are a way of making the computer repeat a
set of actions over and over.

Plain Python
-------------


#. Read the following function, and then predict what the values
   would be when the function calls below are run. Then test yourself
   by typing the function into the activecode area and trying out the examples.

   .. sourcecode:: python

       def foo(x, y, z):
            q = max(x, y)
            r = max(y, z)
            s = max(x, z)
            return min(q, r, s)
       print foo(10, 15, 17)
       print foo(15, 10, 17)
       print foo(17, 10, 15)
       print foo(10, 10, 20)
       print foo(10, 20, 10)

   .. activecode:: act_floops_1



#. Consider the mathematical polynomial function:
   :math:`f(x) = 3x^2 + 2x+ 1`.
   Create a function in Python
   called `polyf` that takes a single input, `x`, and computes this
   polynomial value, and `returns` it.

   Once you have defined the function, it should behave as in the
   following examples:

   .. sourcecode:: python

       >>> polyf(1)
        6
       >>> polyf(10)
       321
       >>> polyf(1) + polyf(10)
       327

   .. actex:: act_floops_2


#. Define a `truncString` function that takes a string as input,
   and returns a new string that contains only the first five
   characters in the input string. (This kind of action is common in
   storing records, using a fixed number of characters from someone's
   name). It is nice if your function works on strings that are
   shorter than five characters in length: it should just return the
   entire input string.

   Once you have defined the function, it should behave as in the
   following example:

   .. sourcecode:: python

       >>> truncString('henrietta')
       'henri'
       >>> truncString('vladimir')
        'vladi'
       >>> truncString("a man a plan a canal - panama!")
       'a man'

   .. actex:: act_floops_3


#. Define a function `spliceLists` that takes two lists and a
   number as its inputs. The number should be a value that is greater
   than or equal to zero, and less than or equal to the length of the
   shortest list. Your function should slice the first list from the
   beginning to the input number, and should slice the second list
   from the input number to the end, and then should concatenate the
   results. See the sample calls below:

   .. sourcecode:: python

       >>> spliceLists([1, 2, 3, 4, 5, 6, 7, [100, 90, 80, 70, 60, 50,
       40], 4) [1, 2, 3, 4, 60, 50, 40]
       >>> spliceLists([1, 2, 3], [9, 8,7, 6, 5], 1) [1, 8, 7, 6, 5]
       >>> spliceLists(['a', 'b', 'c'], ['d','e'], 0) ['d', 'e']
       >>> spliceLists(['a', 'b', 'c'], ['d', 'e'], 2)['a', 'b']

   .. actex:: act_floops_4

Loop!
^^^^^

There are two kinds of loops we will use commonly in Python:
`while` and `for`. The `while` loop takes a boolean expression, an
expression that asks a question, and then has a block of indented
Python statements. It tests the expression, and so long as it
evaluates to true, Python will execute the statements in the block,
and repeat. A `for` loop repeats for a fixed number of times. Each
time through it sets its loop variable to be the next value in the
loop sequence. Look at the examples and questions below.


#. Look at the following loops. For each one, figure out what it
   does. After you work through it by hand, try the loops in activecode and run it.

   .. sourcecode:: python

        # loop 1
        for i in range(10):
           print i, i ** 2


        # loop 2
         i = 0
         while i < 10:
            print i, i ** 2
            i=i+1

        # loop 3
         for c in 'razzamatazz':
            print c.upper()

   .. activecode:: act_floops_5




