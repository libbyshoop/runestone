Activity 4: Using Turtle Graphics with the Wing IDE
===================================================

Background
----------

You have already used the Python turtle graphics library and the random library within the book for this course, using your browser and the python active code editor.  Now let's try an *Integrated Development Environment*, or IDE.  An IDE is a progam designed to aid the process of developing programs in langugaes such as Python.  We will use the Wing 101 IDE.

You will now need to edit your Python programs inside of this Wing 101 IDE and run them there, similar to how you ran your programs in the activecode areas in the book.  The results display in a separate area of the IDE, or in the case of Turtle Graphics, a new window pops up with the output displayed.

.. note::

	Wing 101 is installed on the lab machines in room 258 Olin-Rice.  There is also information on moodle for how to get both Python 3 and the Wing 101 IDE, if you wish to install in on your own laptop.

**Important:** You will now be writing your code and saving it to files.  *Each file's name should end with with the extension .py*;  This is the convention for files containing Python code, just as .doc or .docx are the convention for files that are Microsoft Word documents.  You will need to make sure that you save your work for later; the machines in the lab get cleaned often, so don't leave files on the computer's desktop there.

Your First task:  try out a simple turtle example
--------------------------------------------------

Launch the Wing IDE on your computer. Start with a fresh new file by choosing the `New` button.  Put the following code into the text editing area, then choose to save it using File-Save As.  
.. Need to have more here about saving files to their personal space?
This is designed to be a simple test to be certain that you can get the program running in Wing.  Once you have saved the file, try executing it by choosing the `Run` button (the one with the green arrow).


.. sourcecode:: python
	import turtle            # allows us to use the turtles library
	wn = turtle.Screen()     # creates a graphics window

	alex = turtle.Turtle()
	alex.forward(150)
	alex.left(90)
	alex.forward(75)

	###!!!!!!! Keep the following line in all of your turtle programs !!!!
	wn.exitonclick()

.. note::
	Wing may lock up and be unresponsive if you fail to add the last line in the above example.  As it did when you used turtle graphics in the book, this enable you to close the window by clicking on it.


Your next task: race the turtles using Wing 
--------------------------------------------

Now let's recreate one of your racing turtle examples as a program in the Wing IDE.  Start a new file in Wing.  Grab your code from the last activity that you saved in your browser (on the Macs in the lab, command-a will select all the code in the active code window; command-c will copy; command-v in the Wing editor will paste it).  Save the code in a file called *racingTurtles.py*. **Important:** don't forget to use the `exitonclick()` function on your window in the last line of your code.

Once you seem to have your racing turtles working, you can try the following challenge activity.

Challenge Activity
-------------------

A turtle can rotate left or right any number of degrees.  Write a new program in Wing to have a turtle create an octagon.  Once that is working, have the turtle put its pen up, move some distance, put its pen down, and draw another octagon.  You are free to experiment with other shapes, if you'd like.

