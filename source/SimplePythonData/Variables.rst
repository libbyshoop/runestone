


Variables
=========

.. index:: variable, assignment, assignment statement, state snapshot

.. video:: assignvid
    :controls:
    :thumb: ../_static/assignment.png

    http://knuth.luther.edu/~bmiller/thinkcsVideos/Variables.mov
    http://knuth.luther.edu/~bmiller/thinkcsVideos/Variables.webm

One of the most powerful features of a programming language is the ability to
manipulate **variables**. A variable is a name that refers to a value.

**Assignment statements** create new variables and also give them values to refer to.

.. sourcecode:: python

    message = "What's up, Doc?"
    n = 17
    pi = 3.14159

This example makes three assignments. The first assigns the string value
``"What's up, Doc?"`` to a new variable named ``message``. The second gives the
integer ``17`` to ``n``, and the third assigns the floating-point number
``3.14159`` to a variable called ``pi``.

The **assignment token**, ``=``, should not be confused with *equals*, which
uses the token `==`.  The assignment statement links a *name*, on the left hand
side of the operator, with a *value*, on the right hand side.  This is why you
will get an error if you enter:

.. sourcecode:: python

    17 = n

.. tip::

   When reading or writing code, say to yourself "n is assigned 17" or "n gets
   the value 17" or "n is a reference to the object 17" or "n refers to the object 17".  Don't say "n equals 17".

A common way to represent variables on paper is to write the name with an arrow
pointing to the variable's value. This kind of figure, known as a **reference diagram**, is often called a **state
snapshot** because it shows what state each of the variables is in at a
particular instant in time.  (Think of it as the variable's state of mind).
This diagram shows the result of executing the assignment statements.

.. image:: Figures/refdiagram1.png
   :alt: Reference Diagram

If you ask Python to evaluate a variable, it will produce the value
that is currently linked to the variable.  In other words, evaluating a variable will give you the value that is referred to
by the variable.

.. activecode:: ch02_9
    :nocanvas:

    message = "What's up, Doc?"
    n = 17
    pi = 3.14159

    print(message)
    print(n)
    print(pi)

In each case the result is the value of the variable.
To see this in even more detail, we can run the program using codelens.

.. codelens:: ch02_9_codelens


    message = "What's up, Doc?"
    n = 17
    pi = 3.14159

    print(message)
    print(n)
    print(pi)

Now, as you step thru the statements, you can see
the variables and the values they reference as those references are
created.




Variables also have
types; again, we can ask the interpreter what they are.

.. activecode:: ch02_10
    :nocanvas:

    message = "What's up, Doc?"
    n = 17
    pi = 3.14159

    print(type(message))
    print(type(n))
    print(type(pi))


The type of a variable is the type of the object it currently refers to.


We use variables in a program to "remember" things, like the current score at
the football game.  But variables are *variable*. This means they can change
over time, just like the scoreboard at a football game.  You can assign a value
to a variable, and later assign a different value to the same variable.

.. note::

    This is different from math. In math, if you give `x` the value 3, it
    cannot change to refer to a different value half-way through your
    calculations!

To see this, read and then run the following program.
You'll notice we change the value of `day` three times, and on the third
assignment we even give it a value that is of a different type.


.. codelens:: ch02_11


    day = "Thursday"
    print(day)
    day = "Friday"
    print(day)
    day = 21
    print(day)




A great deal of programming is about having the computer remember things,
e.g.  *The number of missed calls on your phone*, and then arranging to update
or change the variable when you miss another call.

**Check your understanding**

.. mchoicemf:: test_question2_3_2
   :answer_a: Nothing is printed, a runtime error occurs.
   :answer_b: Thursday
   :answer_c: 32.5
   :answer_d: 19
   :correct: d
   :feedback_a: It is not illegal to change the type of data that a variable holds.
   :feedback_b: This is the first value assigned to the variable day, but the next statements reassign that variable to new values.
   :feedback_c: This is the second value assigned to the variable day, but the next statement reassigns that variable to a new value.
   :feedback_d: The variable day will contain the last value assigned to it when it is printed.

   What is printed after the following set of statements?
   <pre>
   day = "Thursday"
   day = 32.5
   day = 19
   print(day)
   </pre>

.. index:: keyword, underscore character

Variable Names and Keywords
---------------------------

**Variable names** can be arbitrarily long. They can contain both letters and
digits, but they have to begin with a letter or an underscore. Although it is
legal to use uppercase letters, by convention we don't. If you do, remember
that case matters. ``Bruce`` and ``bruce`` are different variables.

The underscore character ( ``_``) can appear in a name. It is often used in
names with multiple words, such as ``my_name`` or ``price_of_tea_in_china``.
There are some situations in which names beginning with an underscore have
special meaning, so a safe rule for beginners is to start all names with a
letter.

If you give a variable an illegal name, you get a syntax error.  In the example below, each
of the variable names is illegal.

.. sourcecode:: python

    76trombones = "big parade"
    more$ = 1000000
    class = "Computer Science 101"


``76trombones`` is illegal because it does not begin with a letter.  ``more$``
is illegal because it contains an illegal character, the dollar sign. But
what's wrong with ``class``?

It turns out that ``class`` is one of the Python **keywords**. Keywords define
the language's syntax rules and structure, and they cannot be used as variable
names.
Python has thirty-something keywords (and every now and again improvements to
Python introduce or eliminate one or two):

======== ======== ======== ======== ======== ========
and      as       assert   break    class    continue
def      del      elif     else     except   exec
finally  for      from     global   if       import
in       is       lambda   nonlocal not      or
pass     raise    return   try      while    with
yield    True     False    None
======== ======== ======== ======== ======== ========

You might want to keep this list handy. If the interpreter complains about one
of your variable names and you don't know why, see if it is on this list.

Programmers generally choose names for their variables that are meaningful to
the human readers of the program --- they help the programmer document, or
remember, what the variable is used for.

.. caution::

    Beginners sometimes confuse "meaningful to the human readers" with
    "meaningful to the computer".  So they'll wrongly think that because
    they've called some variable ``average`` or ``pi``, it will somehow
    automagically calculate an average, or automagically associate the variable
    ``pi`` with the value 3.14159.  No! The computer doesn't attach semantic
    meaning to your variable names.

    So you'll find some instructors who deliberately don't choose meaningful
    names when they teach beginners --- not because they don't think it is a
    good habit, but because they're trying to reinforce the message that you,
    the programmer, have to write some program code to calculate the average,
    or you must write an assignment statement to give a variable the value you
    want it to have.

**Check your understanding**

.. mchoicemf:: test_question2_4_1
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: -  The + character is not allowed in variable names.
   :feedback_b: -  The + character is not allowed in variable names (everything else in this name is fine).

   True or False:  the following is a legal variable name in Python:   A_good_grade_is_A+




Reassignment
------------

.. video:: reassignmentvid
    :controls:
    :thumb: ../_static/reassignmentthumb.png

    http://knuth.luther.edu/~pythonworks/thinkcsVideos/reassignment.mov
    http://knuth.luther.edu/~pythonworks/thinkcsVideos/reassignment.webm


As we have mentioned previously, it is legal to make more than one assignment to the
same variable. A new assignment makes an existing variable refer to a new value
(and stop referring to the old value).

.. activecode:: ch07_reassign1

    bruce = 5
    print(bruce)
    bruce = 7
    print(bruce)


The first time ``bruce`` is
printed, its value is 5, and the second time, its value is 7.  The assignment statement changes
the value (the object) that ``bruce`` refers to.

Here is what **reassignment** looks like in a reference diagram:

.. image:: Figures/reassign1.png
   :alt: reassignment



It is important to note that in mathematics, a statement of equality is always true.  If ``a is equal to b``
now, then ``a will always equal to b``. In Python, an assignment statement can make
two variables equal, but because of the possibility of reassignment,
they don't have to stay that way:

.. activecode:: ch07_reassign2

    a = 5
    b = a    # after executing this line, a and b are now equal
    print(a,b)
    a = 3    # after executing this line, a and b are no longer equal
    print(a,b)

Line 4 changes the value of ``a`` but does not change the value of
``b``, so they are no longer equal. We will have much more to say about equality in a later chapter.

.. note::

	In some programming languages, a different
	symbol is used for assignment, such as ``<-`` or ``:=``.  The intent is
	that this will help to avoid confusion.  Python
	chose to use the tokens ``=`` for assignment, and ``==`` for equality.  This is a popular
	choice also found in languages like C, C++, Java, and C#.

**Check your understanding**

.. mchoicemf:: test_question2_9_1
   :answer_a: x is 15 and y is 15
   :answer_b: x is 22 and y is 22
   :answer_c: x is 15 and y is 22
   :answer_d: x is 22 and y is 15
   :correct: d
   :feedback_a: Look at the last assignment statement which gives x a different value.
   :feedback_b: No, x and y are two separate variables.  Just because x changes in the last assignment statement, it does not change the value that was copied into y in the second statement.
   :feedback_c: Look at the last assignment statement, which reassigns x, and not y.
   :feedback_d: Yes, x has the value 22 and y the value 15.


   After the following statements, what are the values of x and y?
   <pre>
   x = 15
   y = x
   x = 22
   </pre>


Updating Variables
------------------

.. video:: updatevid
    :controls:
    :thumb: ../_static/updatethumb.png

    http://knuth.luther.edu/~pythonworks/thinkcsVideos/update.mov
    http://knuth.luther.edu/~pythonworks/thinkcsVideos/update.webm

One of the most common forms of reassignment is an **update** where the new
value of the variable depends on the old.  For example,

.. sourcecode:: python

    x = x + 1

This means get the current value of x, add one, and then update x with the new
value.  The new value of x is the old value of x plus 1.  Although this assignment statement may
look a bit strange, remember that executing assignment is a two-step process.  First, evaluate the
right-hand side expression.  Second, let the variable name on the left-hand side refer to this new
resulting object.  The fact that ``x`` appears on both sides does not matter.  The semantics of the assignment
statement makes sure that there is no confusion as to the result.

.. activecode:: ch07_update1

    x = 6        # initialize x
    print(x)
    x = x + 1    # update x
    print(x)


If you try to update a variable that doesn't exist, you get an error because
Python evaluates the expression on the right side of the assignment operator
before it assigns the resulting value to the name on the left.
Before you can update a variable, you have to **initialize** it, usually with a
simple assignment.  In the above example, ``x`` was initialized to 6.

Updating a variable by adding 1 is called an **increment**; subtracting 1 is
called a **decrement**.  Sometimes programmers also talk about **bumping**
a variable, which means the same as incrementing it by 1.




.. admonition:: Advanced Topics

   * `Topic 1: <at_1_1.html>`_ Python Beyond the Browser.  This is a gentle
     introduction to using Python from the command line.  We'll cover this
     later, but if you are curious about what Python looks like outside of this
     eBook, you can have a look here.  There are also instructions for
     installing Python on your computer here.

   * `Topic 2: <http://diveintopython3.org>`_ Dive Into Python 3,
     this is another oline textbook by Mark Pilgrim.  If you've had some
     programming experience already this book takes you off the deep end with
     both feet.

**Check your understanding**

.. mchoicemf:: test_question2_10_1
   :answer_a: 12
   :answer_b: -1
   :answer_c: 11
   :answer_d: Nothing.  An error occurs because x can never be equal to x - 1
   :correct: c
   :feedback_a: The value of x changes in the second statement.
   :feedback_b: In the second statement, evaluate the current value of x before subtracting 1.
   :feedback_c: Yes, this statement sets the value of x equal to the current value minus 1.
   :feedback_d: Remember that variables in Python are different from variables in math in that they (temporarily) hold values, but can be reassigned.


   What is printed by the following statements?
   <pre>
   x = 12
   x = x - 1
   print (x)
   </pre>

Exercises
---------

#. Take the sentence: *All work and no play makes Jack a dull boy.*
   Store each word in a separate variable, then print out the sentence on
   one line using ``print``.

   .. actex:: ex_2_5