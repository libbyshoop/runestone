Making Pictures and Sounds
==========================

This activity will look at tools in JES for creating
pictures and sounds from scratch.

Basic drawing commands
----------------------

*Bear in mind: most drawing commands take an optional last  argument to specify the color to draw with, which can be any color  object: built-in, chosen from `pickAColor*,
or created with `makeColor`.`

Start off by creating a new, empty picture object, that is at least
500 pixels by 500 pixels in size. On that object, try out each of
the drawing commands in turn, using different color options. Bear
in mind that you need to repaint the picture each time to see the
results of your operations.

Try the following,
^^^^^^^^^^^^^^^^^^

typing each into the interactive shell. Then try some variations of
your own. Use the help in JES to look at the details

.. sourcecode:: python

    >>> p = makeEmptyPicture(500, 500)
    >>> show(p)
    >>> addLine(p, 1, 1, 250, 250, green)
    >>> repaint(p) # After this, I will leave out the repaint...
    >>> addRect(p, 150, 10, 200, 210)
    >>> addRectFilled(p,300, 300, 75, 75, makeColor(220, 102, 192))
    >>> addArc(p, 20, 20,100, 30, 0, 180, blue)
    >>> addArcFilled(p, 10, 400, 75, 75, 90, 90,makeColor(25, 160, 38))
    >>> addOvalFilled(p, 350, 20, 100, 75,yellow)
    >>> addText(p, 200, 350, 'Hi there!', orange)



You can create text that has different styles using the
`addTextWithStyle` option. You create a Style object that describes
the font, its size, and other details, and then you add text with
that style. The example below shows two different styles being
drawn (Note the special `import` command you need to do this!). I
have written a helper function called `listAllFonts` that will list
the fonts available to the system on any given computer. If the
fonts below are not working, use that function to figure out fonts
that *are* defined on your computer.

.. sourcecode:: python

    import java.awt.Font as Font
    str1 = "Big font with attitude"
    style1= makeStyle("Braggadocio", Font.BOLD, 48)
    addTextWithStyle(p, 10,200, str1, style1)
    str2 = "Little cute font"
    style2 =makeStyle("Gill Sans", Font.PLAIN, 10)
    addTextWithStyle(p, 50, 300,str2, style2, magenta)




In the `makingstuff.py` file, I have included code to draw a very
simple happy face. Take a look at my code for help as you work on
the next two tasks.

Draw a Sign
-----------

Create a function called `neonSign` that takes a picture object as
its input. It should draw a fanciful store sign, like the neon sign
for a diner or something like that, on the picture that was input.
Make sure the sign has at least three elements to it. Don't make
the sign too big, we're going to want to draw it in different
places on the picture next.

Draw the sign anywhere you want
-------------------------------

Next, create a new version of the function, called `neonSign2`,
that takes a picture object, and a starting x and y value. This
function should draw the sign so that the upper-left corner of the
sign is located at (x, y). Decide what the upper-left corner of the
sign is, and then figure out how to specify the positions in the
rest of the object as "offsets" from the upper-left corner.

Look at the `drawSmiley2` function I've provided in the file for an
example of how to do this.

Challenge Tasks
---------------


#. `Make the sign blink!` Create a program that draws the sign in a
   particular location, and then has it blink on and off. This will
   only really work if you have a plain background for the picture. To
   erase a drawn picture, draw a rectangle that is the background
   color over it. To make the blinking take some time, import the
   `time` module, and use the `sleep` function within it, which acts
   much like the `wait` function Myro provides, except it is normal
   Python.

.. sourcecode:: python

   import time

   time.sleep(3.0) # will wait for 3 seconds before continuing



#. `Make the sign shimmy!` It is common these days to see
   computer-generated animations that try to look crudely hand-drawn
   by having the shapes move around a little bit. Create a program
   that does this, by drawing the sign in a random location close to
   some main set of coordinates.

#. `Make the sign glide!` Make the sign glide across the screen
   from left to right, by drawing it, waiting, and then erasing it and
   drawing it further over.


Making sound waves
------------------

Synthesizers and electronic keyboards typically use three methods
to produce sounds: One is simply to output a recorded sound as is.
A second method is used to sample from a recorded sound at
different rates, changing its pitch. This is often used to generate
synthesized instrument sounds, like piano or violin. The third
method involves generating sound waves of a particular shape.

In the file `makingstuff.py` you will find three functions for
generating sound waves: one makes a sine wave, what we perceive as
a very pure tone, a second makes a simple square wave, and a third
makes a triangle wave. Try out these three functions, being sure to
use the `explore` sound tool to look at the resulting shapes.

Try this:
^^^^^^^^^

If you feel you understand these three, try to make a sawtooth wave
function. This function will be similar to the triangle shape,
except that it should rise from `-amplitude` to `+amplitude` over
the length of the whole cycle, and then it should start over: with
a straight drop from `+amplitude` to `-amplitude` between one
sample and the next. See the wikipedia page on `Sawtooth wave`_ for
a picture.

.. _Sawtooth wave: http://en.wikipedia.org/wiki/Sawtooth_wave


Making tunes
------------

JES includes a function `playNote`, described in the chapter on
generating sounds. This function takes a note number, a duration in
milliseconds, and an intensity, and it generates a simulated piano
tone. Try the `tune` function in the `makingstuff.py` file. If you
have something that can synthesize sounds for you, a program that
describes the tune takes up much less space than the sound file
itself!

The following web page shows how to map between piano keys, Midi
numbers, and frequencies:
http://www.phys.unsw.edu.au/jw/notes.html

Try your own:
^^^^^^^^^^^^^

Define your own simple tune using the `playNote` function.

Challenge activity:
^^^^^^^^^^^^^^^^^^^

Write a function that converts from a string description of a note
to the Midi note. Decide on a good way to specify octave
differences. Then, write a function that takes a list of strings
describing notes. This function should play the tune described by
the list of strings, using the earlier function to convert each
string to its corresponding number.


