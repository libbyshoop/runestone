Happy Robots and Recursion Activity
===================================

**COMP 123**


To understand how recursion works, we need the
"happy robots" metaphor from earlier this term.

When a function call happens, imagine that Python selects a
"happy robot". Python gives that robot a *copy* of the function
definition, and the robot assigns its input parameters to the
values of the arguments in the function call. The robot then
performs its actions, which might include making function calls of
is own.

We are going to act out the process involved in a call to a
recursive function, taking on the roles of the happy robots for the
process. Divide up into groups of about 5-7 people. Each person
should take two or three slips of paper.

Examine the Python program listed below:

.. sourcecode:: python

    def fact(n):
        if n == 0:
            return 1
        else:
            recAns = fact(n - 1)
            return n * recAns

.. activecode:: act_recur_01

    def fact(n):
        if n == 0:
            return 1
        else:
            recAns = fact(n - 1)
            return n * recAns



Act out, step by step, what would happen for a call to `fact{4}`.
One volunteer should be the happy robot for this first call. Each
person, when called upon to be a happy robot, should write down on
a slip of paper the value of your parameter variable, and then
should work through the steps of the function. When happy robot
person A reaches the recursive call, s/he should pick another group
member to be the happy robot for the recursive call, happy robot
person B. Person A should then wait until person B completes their
work and passes back a value. To pass back a value, write it on a
slip of paper and hand it back to the person who called you.

Once you successfully act out this function call, try the more
complicated function below instead, with the call
`sumList([3, 6, 2, 4], 1, 3)`.

.. sourcecode:: python

    def sumList(lst, startPos, endPos):
        if startPos > endPos:
            return 0
        else:
            ans = sumList(lst, startPos + 1, endPos)
            return lst[startPos]+ ans

.. activecode:: act_recur_02

    def sumList(lst, startPos, endPos):
        if startPos > endPos:
            return 0
        else:
            ans = sumList(lst, startPos + 1, endPos)
            return lst[startPos]+ ans

If you want a bigger challenge, try a function like the one below
that performs more than one recursive call. Be sure to keep track
of which group members are currently active, and which ones have
finished, so that you can reuse people. Consider the call
`fib(4)`.

.. sourcecode:: python

    def fibonacci(m):
        if m == 0:
            return 0
        elif m == 1:
            return 1
        else:
            prev = fibonacci(m - 1)
            prevPrev = fibonacci(m - 2)
            return prev +prevPrev

.. activecode:: act_recur_03

    def fibonacci(m):
        if m == 0:
            return 0
        elif m == 1:
            return 1
        else:
            prev = fibonacci(m - 1)
            prevPrev = fibonacci(m - 2)
            return prev +prevPrev



