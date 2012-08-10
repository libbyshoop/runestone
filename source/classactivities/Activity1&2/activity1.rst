Basic Python Activity
=====================

**COMP 123**

Overview
--------
Today you will learn a bit about Python, and some basic kinds of data Python can manipulate. You’ll learn
how to store values in variables, and how to build expressions that can be evaluated to produce a value. You
will learn how to put sequences of Python statements and expressions in a program which can be
saved and re-run at a later point.
.. TODO remove script reference

Python
------
Python provides an interactive shell that we use to communicate with it, much like a calculator provides an
interface that we use to communicate with it. With Python, you can type a series of Python statements into
the shell, and get immediate responses to each one. You can also package up a series of statements as a
program. When you run the program, Python executes each statement in order. Most modern operating systems
allow you to run a Python program as if it were an executable application, just by choosing *run*.
Behind the scenes, the Python shell is started up, and the statements are executed
in the shell one after another.

.. TODO rewrite this entire paragraph


Try these examples
^^^^^^^^^^^^^^^^^^
.. TODO edit this as well

Try the examples below in the activecode area, typing each one
in turn. Note how variables in computer science are similar to
variables in math, but not identical. Think of a variable as being
a name for a box in the computer's memory, where you can stick a
value of some kind.

.. sourcecode:: python

    print(5+2) #Compute the sum of two numbers.
    x=100 #Assign the value 100 to variable x.
    print(2*x)-33 #Compute the value 2x-33
    print(2**4) # Compute the value
    z=(x-(5*4)) #Assign the value of the expression to variable z.
    print(10*3,x,z) #Print the values of each expression on a line.
    strng="Hello there" #Assign variable strng to be the string.
    print(strng) #print strng

.. activecode:: act_intro_1



Common Errors
-------------
Here are a few errors you might encounter in python. Look through the examples below and determine what type of error each one has.

Common Error A
^^^^^^^^^^^^^^^
Step forward through the following program until an error occurs.

.. codelens:: act_code_01

    a=5
    b=10
    c=20
    a=0
    e=30
    print(e/a)


.. mchoicemf:: question1_01
   :answer_a: Syntax error
   :answer_b: Semantic error
   :answer_c: Runtime error
   :correct: c
   :feedback_a: A syntax error is an error in the structure of the python code that can be detected before the program is executed. This is not a syntax error as the structure of the code is good.
   :feedback_b: This is not an error in logic.
   :feedback_c: Python cannot tell if you are trying to divide by 0 until the program is run.

   What kind of an error is this?

Common Error B
^^^^^^^^^^^^^^^

.. activecode:: act_code_02

    x=3
    y=4
    z=10
     print(x,y,z)

.. mchoicemf:: question1_02
   :answer_a: Syntax error
   :answer_b: Runtime error
   :answer_c: Semantic error
   :correct: a
   :feedback_a: The incorrect indentation in the print statement is a problem with the formal structure of the program.
   :feedback_b: This is not a runtime error as it is a problem with the formal structure of the program.
   :feedback_c: This is a problem with the formal structure of the program, not in the logic of the program.

   What kind of an error is this?

Common Error C
^^^^^^^^^^^^^^^
Why is the following code incorrect?

.. activecode:: act_code_03

    #This program converts a value in centigrade to fahrenheit
    centigrade=30
    fraction=5/9
    fahrenheit=(centigrade*fraction)+32
    print(fahrenheit)

.. mchoicemf:: question1_03
   :answer_a: Runtime error
   :answer_b: Syntax error
   :answer_c: Semantic error
   :correct: c
   :feedback_a: This is an error in logic as the program doesnt produce the correct answer. So it is not a run-time error.
   :feedback_b: The formal structure of the program is correct.
   :feedback_c: The fraction should be 9/5 not 5/9. This is a semantic error which is why the program produced a wrong answer.

   What kind of an error is this?

Common Error D
^^^^^^^^^^^^^^^
How helpful is the error message when you run the following? Look real carefully if you can figure out what's wrong. Remove the last line and see what error message occurs.

.. activecode:: act_code_04

    a=5
    b=10
    c=7
    d=16
    print((a*d)/(b/c)
    print("goodbye")

.. mchoicemf:: question1_04
   :answer_a: Runtime error
   :answer_b: Syntax error
   :answer_c: Semantic error
   :correct: b
   :feedback_a: Unbalanced parenthesis is a problem with the formal structure of the program, not a runtime error and can be figured out before program execution.
   :feedback_b: Unbalanced parenthesis is an error in the structure of the python code that can be detected before the program is executed.
   :feedback_c: This is a problem with the formal structure of the program and not in its logic.

   What kind of an error is this?

Common Error E
^^^^^^^^^^^^^^^

.. codelens:: act_code_05

    strng="Hi there"
    sentence="The quick brown fox jumps over the lazy dog"
    print(string)


.. mchoicemf:: question1_05
   :answer_a: Syntax error
   :answer_b: semantic error
   :answer_c: runtime error
   :correct: c
   :feedback_a: A syntax error is an error in the structure of the python code that can be detected before the program is executed. This is not a syntax error as the structure of the code is good.
   :feedback_b: This is not an error in logic and the code doesnt produce the wrong answer.
   :feedback_c: Python cannot tell if string is not defined until the program is run.

   What kind of an error is this?


Try More on your own
^^^^^^^^^^^^^^^^^^^^^^^
For more practice, try generating your own errors.

Create your own program
-----------------------
.. TODO change scripts to program and editor

Suppose I want to fence in my backyard. Given the length and width
of the space, I can figure out how much fencing I need by computing
the perimeter of the rectangle. Define a variable ``w`` to hold the
value 50 (the width in feet of my yard), and define variable ``l`` to
be the value 75 (the length in feet of my yard). Then write a
Python expression to calculate how many feet of fencing I would
need to enclose my yard. Try it out in the editor below.

Copy the statements
you used to compute the length of fencing. Make
sure each statement starts at the beginning of the line (no leading
spaces). To run your program, select "Run". Does it work? When you run a program, Python automatically suppresses the values of each expression
. Thus, if you want to see the result of your
calculations, you will need to add ``print`` statements to see the
final result. Next, change the values of ``w`` and ``l`` to new values.
Does the program work correctly on these new values? Add a comment
above your Python statements that describes what your program does.

.. actex:: act_intro_2





Strings
-------

Strings are collections of characters, and characters are keyboard
symbols. For now, we'll use strings to be little bits of text, so
that we can print out more interesting messages.

Strings and characters are written the same in Python. A character
is just a string of length 1. Strings are written with quotes
before and after them. You can either use double-quotes or
single-quotes, as the examples below show. There are special
strings called "doc-strings" that are written with three
double-quotes before and after. These strings can be more than one
line long.

.. sourcecode:: python

     'Hi there'
     "Hi there"
     "I contain an apostrophe, don't I"
     'I was told, "double quotes go inside single quotes"'
     s = 'hi mom'
     longstr= """As I was going to St. Ives, I met a man with seven wives.   Each wife had seven sacks,
     Each sack had seven cats,   Each cat had seven kits.    Kits, cats, sacks, and wives:   How many were going to St.Ives?"""



We won't do much with string operations today, but here are a
couple to keep in mind:

    +--------------------------+---------------------------------------------------+
    |``len('foo')``            |  returns the number of characters in its argument |
    +--------------------------+---------------------------------------------------+
    |``'foo' + 'bar'``         |   concatenates the two strings together           |
    +--------------------------+---------------------------------------------------+
    |``'foo' * 3``             | concatenates the string with itself the number of |
    |                          |              times given                          |
    +--------------------------+---------------------------------------------------+
    |``'mom' in s``            |   checks if first string occurs in second string  |
    +--------------------------+---------------------------------------------------+
    |``s[3]``                  |   returns the character at the given position,    |
    |                          |     zero-based                                    |
    +--------------------------+---------------------------------------------------+
    |``s[3:5]``                |    returns a substring starting at 3 and          |
    |                          |      ending before 5                              |
    +--------------------------+---------------------------------------------------+

A string script
^^^^^^^^^^^^^^^

Create a program that starts with:

.. sourcecode:: python

    sentence = 'We must go to the movies on Saturday'


The program should pull out the last word in the sentence, using the
substring operation from above, and should print a new string
formed by concatenating the last word with itself 4 times.

.. actex:: act_intro_5

