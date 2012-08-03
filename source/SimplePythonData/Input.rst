



Input
=====

.. index:: input, input dialog

.. _input:

.. video:: inputvid
    :controls:
    :thumb: ../_static/inputthumb.png

    http://knuth.luther.edu/~pythonworks/thinkcsVideos/input.mov
    http://knuth.luther.edu/~pythonworks/thinkcsVideos/input.webm


The program in the previous section works fine but is very limited in that it only works with one value for ``total_secs``.  What if we wanted to rewrite the program so that it was more general.  One thing we could
do is allow the use to enter any value they wish for the number of seconds.  The program would then print the
proper result for that starting value.

In order to do this, we need a way to get **input** from the user.  Luckily, in Python
there is a built-in function to accomplish this task.  As you might expect, it is called ``input``.

.. sourcecode:: python

    n = input("Please enter your name: ")

The input function allows the user to provide a **prompt string**.  When the function is evaluated, the prompt is
shown.
The user of the program can enter the name and press `return`. When this
happens the text that has been entered is returned from the `input` function,
and in this case assigned to the variable `n`.

.. activecode:: inputfun

    n = input("Please enter your name: ")
    print("Hello", n)

Even if you asked the user to enter their age, you would get back a string like
``"17"``.  It would be your job, as the programmer, to convert that string into
a int or a float, using the `int` or `float` converter functions we saw
earlier.

To modify our previous program, we will add an input statement to allow the user to enter the number of seconds.  Then
we will convert that string to an integer.  From there the process is the same as before.

.. activecode:: int_secs

    str_seconds = input("Please enter the number of seconds you wish to convert")
    total_secs = int(str_seconds)

    hours = total_secs // 3600
    secs_still_remaining = total_secs % 3600
    minutes =  secs_still_remaining // 60
    secs_finally_remaining = secs_still_remaining  % 60

    print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)


The variable ``str_seconds`` will refer to the string that is entered by the user. As we said above, even though this string may be ``7684``, it is still a string and not a number.  To convert it to an integer, we use the ``int`` function.
The result is referred to by ``total_secs``.  Now, each time you run the program, you can enter a new value for the number of seconds to be converted.

**Check your understanding**

.. mchoicemf:: test_question2_7_1
   :answer_a: &lt;class 'str'&gt;
   :answer_b: &lt;class 'int'&gt;
   :answer_c: &lt;class 18&gt;
   :answer_d: 18
   :correct: a
   :feedback_a: All input from users is read in as a string.
   :feedback_b: Even though the user typed in an integer, it does not come into the program as an integer.
   :feedback_c: 18 is the value of what the user typed, not the type of the data.
   :feedback_d: 18 is the value of what the user typed, not the type of the data.

   What is printed from the following statements?
   <pre>
   n = input("Please enter your age: ")
   # user types in 18
   print ( type(n) )
   </pre>

Exercises
=========

#. You look at the clock and it is exactly 2pm.  You set an alarm to go off
   in 51 hours.  At what time does the alarm go off? Write a comment in english as to how you would do this calculation.

   .. actex:: ex_2_2

#. Write a Python program to solve the general version of the above problem.
   Ask the user for the time now (in hours), and ask for the number of hours to wait.
   Your program should output what the time will be on the clock when the alarm goes off.

   .. actex:: ex_2_3

#. You go on a wonderful holiday
   leaving on day number 3 (a Wednesday).  You return home after 137 nights.
   Write a general version of the program which asks for the starting day number, and
   the length of your stay, and it will tell you the number of day of the week you will return on.

   .. actex:: ex_2_4

       # Problem 4
       # My Name:

#. Write a program that will compute the area of a circle.  Prompt the user to enter the radius and print a nice message
   back to the user with the answer.

   .. actex:: ex_2_8

#. Write a program that will compute the area of a rectangle.  Prompt the user to enter the width and height of the rectangle.
   Print a nice message with the answer.

   .. actex:: ex_2_9

#. Write a program that will compute MPG for a car.  Prompt the user to enter the number of miles driven and the number of
   gallons used.  Print a nice message with the answer.

   .. actex:: ex_2_10

#. Write a program that will convert degrees celsius to degrees fahrenheit.

   .. actex:: ex_2_11

#. Write a program that will convert degrees fahrenheit to degrees celsius.

   .. actex:: ex_2_12
