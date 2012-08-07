Activity 11: Debugging with Wing
================================

Overview
--------

While you have read about debugging, and you have some practice
trying to debug, this activity will focus on strategies for
debugging programs, and in particular will introduce the debugger
in Wing.

When a program you write doesn't run and produce the
correct result, you need to debug it. If there are syntax errors,
so that you cannot even load the Python file into the shell, then
those must be handled first. After that, you need to debug problems
where either a runtime error occurs or the wrong answer is
produced.

Get a copy of the 
:download:`debuggingstuff.py <debuggingstuff.py>` file, which contains the
longer code segments you'll use for this activity. Since you are going to correct errors in
this file, you will want to `save a new copy of it by using the
file-save-as option and saving this as` `fixed\_debuggingstuff.py`.
You will want to get back to the buggy version during this
exercise.

Debugging Syntax Errors
-----------------------

The first problem with debugging syntax errors is determining where
the error is in your program. Notice first of all that the Wing
editor puts a red squiggly line under parts of your Python code
that look like syntax errors to it.

If that doesn't help, start by reading the error message that is
printed in the Python shell. Error messages start with the word
"Traceback," and give the computer's best information about the
error.

.. note:: The following example 'programs' are to illustrate
          points. You should be in the habit of writing functions by now for
          most of your work.

Example 1:
^^^^^^^^^^

Examine the sourcecode below. When run, this generated the error
message that appears below that. Note that in Wing's editor this
program underlined all of line 4.

.. sourcecode:: python

    # program with bugs

    x = 3
     y = 4



    Traceback (most recent call last): File "<string>", line 4, in
    <fragment> IndentationError: unexpected indent (<wingdb\_compile>,
    line 4)



The "traceback" is showing you what was happening in the computer
to get to the point where the error occurred. In this case that
information isn't useful. The bottom line describes the error that
it found. Note that Wing shows you the line number for the error.
This error message is telling us that there was a problem with
indentation on line 4, and that line 4 was indented more than was
expected.

Example 2:
^^^^^^^^^^

Here is another program with a more obscure error message. In this
case the 5 and the character after it were underlined in red.

.. sourcecode:: python

    # program with bugs

    if x > 5
    print 2



    Traceback (most recent call last): File "<string>", line 3, in
    <fragment> invalid syntax: <string>, line 3, pos 9



This error message isn't very helpful about what the problem is, it
just knows that there is bad syntax here. However, notice that it
tells you both the line number (3) and the character position
within the line (the 9th character) where the error was detected.
In this case, it is missing the colon at the end of the if
conditional line.

Notice, also, that there actually are two syntax errors in this
program, but Python will always stop and report only the first error
it finds.

Example 3:
^^^^^^^^^^

Sometime Python detects a syntax error far from where the error
actually took place. Consider this example:

.. sourcecode:: python

    # bug not where detected

    s = """here is a multiline string,
    but I have forgotten something
    l= s.split()
    print l



    Traceback (most recent call last): File "<string>", line 6, in
    <fragment> EOF while scanning triple-quoted string literal:
    <string>, line 6, pos 88



In this case, Python found an error at the very end. EOF stands for
"End of File;" Python was reading a triple-quoted string and got to
the end of the file without finding the end of the string. You
would have to figure out where the end of the string was supposed
to be.

If you have a syntax error and you cannot figure out where it is,
use either of the first two strategies listed in the next section
to find it.

Debugging Strategies
--------------------

There are many strategies for debugging programs, but these three
are good ones to cultivate for this class.


1. `Consider all possible test cases for functions.` When you are
   developing a function, also develop enough test cases to handle all
   possible results.

2. `By-hand walk-through of the code.` For this strategy, you
   pretend to be the computer. Walk through your program line by line,
   performing the actions each line says to do. You need to act like
   the computer: read each line closely and carefully. If you aren't
   sure what a given line would do, use the Python shell to try out
   the line by itself, filling in any variables with appropriate
   values. Often, through this process, you will discover the error.
   You will also gain a deeper understanding of what your Python
   programs do, in general.

Try this:
^^^^^^^^^

Try working through the following buggy program to determine where
things go wrong. This program appears in the `debuggingstuff.py`
file. There are three errors in total. Begin by first developing
enough test cases to determine which order of inputs causes
problems. Then walk through each line to determine where the errors
are and fix them.

.. sourcecode:: python

   # This function takes in three numbers and returns them in a list,
   # in increasing order
   def orderNums(num1, num2, num3):
    smallest = min(num1, num2, num3)
    biggest = max(num1, num2, num3)
    if num1 == smallest:
       if num2 == biggest:
        return [smallest, num2, biggest]
       else:
        return [smallest, num3, biggest]
    elif num2 == smallest:
       if num1 == biggest:
        return [smallest, num3, biggest]
       else:
        return [smallest, num2, biggest]
    else:
       if num1 == biggest:
        return [smallest, num2, biggest]
       else:
        return [smallest, num1, biggest]



3. `Insert print statements to see what is happening.` For this
   strategy, you insert print statements in strategic locations of
   your program, so that when you run the program it will tell you
   what is happening. Sometimes you just need to know that the program
   reached a particular line, other times you might want to print out
   values of variables.
   *It is always worth the time to make easily  understood outputs!*
   By this I mean that simply spitting out a bunch of numbers may get
   confusing. Label each print statement with what it is printing and
   where it occurs.

Try this:
^^^^^^^^^

   Try this with the example function in the file `debuggingstuff.py`
   called `between`. First uncomment the initial test given to you,
   then develop new tests to completely exercise all the code in this
   function (do this by trying a case where it should return an empty
   list). There is one print statement already in the function as an
   example of how to write helpful ones. Try inserting more print
   statements to see what else is happening in this code. Can you
   devise a way to fix it? If you can't quite do this, then comment
   out the whole function by moving the line with the three
   double-quotes just past the last line of the function, som it
   becomes one big long quoted string. You can come back to it and try
   the 'dubugger' method described next later.

4. `Use the Wing debugger.` The debugger will let you step,
   line-by-line, through your program. Through the debugger you can
   see the values of all the variables, what functions are active, and
   other useful information. The next section will walk you through
   the basics of using the debugger.


The Wing Debugger
-----------------

Prerequisites to using the debugger
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The debugger only works with saved files, so the first thing you
must do is to save your code as a file with the `.py` extension.
Also, your program must run itself automatically when you click the
`Run` button. If you are writing a program, there is no problem, but
if you are defining a function, then you *must* include a call to
the function after the definition, in the file.

You should also set up the Wing window so that you can see the
debugger information. At the right side of the window, you should
see a box with two tabs on it, labeled `Exceptions` and `Call
Stack`. If you cannot see them, then look for the little grid of
dots about halfway down the screen. You can click there and drag to
the left, and the box should appear.

To the left of the `Python Shell` box, which also has a tab called
`Debug I/O`, you should see another box with two tabs: `Search` and
"Stack Data." If you don't see it, look for the grid of dots just
left of the Python shell box, and drag it to the right. Note that
the `Search` tab is just a general search-and-replace function, not
specifically part of the debugger tools.

Using the debugger to find a runtime error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your program generates a runtime error when you run it, then you
can simply click on the `Debug` button (the one that looks like a
little green bug), and the debugger will run until the error
happens. At that point you can see the state the program was in at
the time of the error.

Uncomment (remove the `#` symbols) the line that has the call to the `getChar5` function. Then click
on the Debug button (the one that looks like a bug to the right of
the Run button and the one that looks like a 'Hand' and see what
happens.

.. sourcecode:: python

    # This function returns the character at position 5
    # in its input string. Note that is the sixth character.
    def getChar5(string):
        return string[5]

    print getChar5("tiny")



Let's look at what was produced:


-  The `Debug I/O` tab will show any output generated by your file.
   In this case, unless you removed the `print` statement of a call to
   `orderNums` and/or `between`, that may appear in this tab. You
   know, then, that the program was fine through that `print`
   statement.

-  The `Exceptions` tab, on the right size, prints the error
   message that was generated. This is essentially the same
   information that would have been printed in the Python Shell. What
   is the actual error in this case?

-  The `Call Stack` tab, also on the right, shows you that the
   computer was executing the line

   `return string[5]`,

   in response to the function call `getChar5("tiny")`.

-  The `Stack Data` tab, on the lower left, shows you the current
   local variables, and any global variables that are defined.
   Parameter variables are considered "local" in this context. You can
   see that the local variable `string` is bound to the value
   `'tiny'`.


From this information you can identify where the runtime error
occurred, and what information the code was using at that moment.
You can probably figure out what is wrong just from that.

If you wish, you can now fix this error and also add more test
cases. Then you can either Run or Debug again.

Using the debugger to walk through the code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To debug errors where the program runs but gives incorrect results,
or to get a better sense for what the program is doing in general,
you can use the debugger to walk, step-by-step, through the
program. To do this, you place one or more "breakpoints" in your
program. To place a breakpoint you click in the gray area between
the line number and the code, and a red dot should appear.

Comment out the `getChar5` code and call for now, if you didn't fix
it.

Now get back the buggy version of `orderNums`. You could do this by
changing the name of your working function and copying back in the
buggy one from the original `debuggingstuff.py` file.

Try placing a breakpoint on the first line of the `orderNums`
function. Make sure that the call to `orderNums `is uncommented and
correct. Then click the Debug button. Python will start to evaluate
the function call, and will stop when it reaches the line with the
breakpoint, *before evaluating that line*. Look at what the `Call
Stack` and `Stack Data` tabs are telling you. Note the values of
the parameter values.

To step through the program line by line, you will use the three
buttons at the right end of the button toolbar. They are called
`Step Into`, `Step Over`, and `Step Out`, and the icons include an
arrow that turns from horizontal to downward, an arrow that points
straight to the right, and an arrow that starts vertical and turns
to point to the right.

The `Step Into` and the `Step Over` buttons with both move line by
line through your program. But they differ from each other in what
they do when they encounter a line that contains a call to a
user-defined function. The `Step Into` button will make the
function call, and will shift to moving line by line through the
code for that function. The `Step Over` button will treat the
function call as a single step, and will go on to the next line in
this function.

The `Step Out` button will move line by line through program
statements, but if the debugger is currently stepping through a
function because of a function call, `Step Out` will stop going
line by line and will simply run the remaining lines, stopping
after the function call has ended to resume stepping line by line.

Try this:
^^^^^^^^^

Try using these tools to step through the call to `orderNums`, and
see where the error takes place. Change the call to step through
other paths of the function.

To end a debugging session:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you are done with one run of your program, you can click on
the `Stop` button to end the debugging session.

Challenge problem
-----------------

If you want a bit more challenge, then uncomment the function and
call at the bottom of the `debuggingstuff.py` file. It contains a
variety of bugs. Use the methods and tools described here to debug
the program until it runs correctly.

*Note: to comment out or to uncomment a region of a file, select  the region, and then select "Toggle comment" from the `Source*
menu.`

