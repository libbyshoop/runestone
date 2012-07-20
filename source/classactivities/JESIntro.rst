An Introduction to JES
=======================

Overview
---------

This activity introduces you to the JES application for programming
Python, and some basic commands for working with images and sounds.
Most of these functions are integrated into Myro, [1]_ so you can
use Calico to do some of this, but JES has some nice features for
working with images and sounds that Calico lacks. The JES software
can be downloaded from the link on the Moodle site. Be sure when
installing JES on your own computer that you install version 4.3
from the web!

.. note:: If you have the first edition of the Guzdial
          textbook, there are significant differences in how JES worked, and
          in the organization of sections. I do `not` recommend that you use
          the first edition, but if you must, come see me to find out what is
          different.

Another Python Dialect: Jython
------------------------------

JES uses a different dialect of Python from both Wing and Calico.
Recall that Wing uses "normal" or C Python, and Calico a variant
called Iron Python. JES uses a variant called Jython, because it is
written Java and has access to some Java tools. When using JES,
expect to see some (minor) differences from what we've done so far.
This is a bit like learning English as spoken in the US, in the UK,
and in India; fortunately, programming languages are smaller and
more defined than human languages.

When you start up JES, you see a window with two parts. At the top
of the window is the program editor. At the bottom of the window is
the interactive shell for communicating with Python. You type your
program into the editor at the top, then click on the `Load
Program` button to load it into Python.

JES contains a number of menus you haven't seen before. The
`Watcher` menu starts up a debugging tool integrated into JES. It
is not as nice as Wing's debugger, but you can use it to watch how
variables change values through the course of a program.

The `Mediatools` menu provides access to tools for viewing sounds,
images, or movies; you'll see how to use them as we go along.

The `JES Functions` menu is very useful. Within it, you will see a
listing of all specialized functions that JES includes, organized
by the topic, or module, that they come from. Because JES is
designed for doing image and sound processing, all these modules
are automatically added to basic Python when you start JES up.
Select a function name from the `JES Functions` menu, and two
things happen: the beginning of a call to the function appears in
either the editor or interactive shell (depending on where the
focus currently is), and a new pane appears to the right,
containing the help information about that function. Try this for
the `pickAFile` function, and *read* the help information.

The last menu, `Window Layout`, allows you to switch between seeing
just the editor and shell, or seeing editor, shell, and help
system, or seeing editor, shell, and debugging tool.

You write your Python code in the editor part of the JES window.
You then click the `Load Program` button in the middle of the
window. When you are entering Python statements and expressions in
the interactive shell, you can retrieve previous items you typed
using the up arrow key, as in both Wing and Calico.

Sound and image function basics
-------------------------------

Call the function `pickAFile()` in the interactive shell, and
choose any file you like. Try the following, and look at the value
of the variable `fileInfo`. What *kind* of data does the function
return as its value?

.. sourcecode:: python

    >>> fileInfo = pickAFile()



Find the folder where all the image and sound files from the book
are stored (I'll show you where). Then, using `pickAFile` and
`makePicture`, create a variable `bfly` which contains the Picture
object for the file `butterfly2.jpg`. Use the `show` function to
view the picture. Here are two ways to do this:

.. sourcecode:: python

    >>> bflyFile = pickAFile()
    >>> bfly = makePicture(bfly)
    >>> show(bfly)

    >>> bfly = makePicture(pickAFile())
    >>> show(bfly)



Now, do something similar to create a Sound object `getty` from the
file `gettysburg.wav`, and use `play` to listen to it (make sure
the sound on your computer is not muted or very low).

Using `pickAFile` to select a file each time can be rather a pain.
You can pass a string containing *the entire path of a file* to
either `makeSound` or `makePicture`, but that can also be a pain,
especially since the MediaSources files may be in different places
on different computers.

There is also a function called `setMediaFolder` which tells JES
which folder to look for media files in. You can then use *only*
the filename to load files.

Try this:
^^^^^^^^^

Type the script below into the editor pane. Then load the file into
Python, selecting the MediaSources folder when requested. What
happens when the script is loaded? How is it different if you
change the calls to `play` to be calls to `blockingPlay`?

.. sourcecode:: python


        setMediaFolder()
        pic1 = makePicture('butterfly2.jpg')
        pic2 = makePicture('horse.jpg')
        pic3= makePicture('redDoor.jpg')

        snd1 = makeSound('gettysburg.wav')
        snd2 = makeSound('preamble10.wav')
        snd3 = makeSound('g4.wav')

        show(pic1)
        show(pic2)
        show(pic3)
        play(snd1)
        play(snd2)
        play(snd3)



Manipulating pictures
---------------------

Pictures are objects belonging to the Picture type; it isn't
built-in to normal Python, so we called it a Picture 'class.' These
objects have methods, just as lists, strings, and dictionaries do,
but for now we will just work with pictures using the functions JES
has defined.

Table pictures below lists the Picture-related functions and
methods that you need to know right now. There are many more, as
you can see in the JES functions menu, but you will learn those
over time. Each picture contains a two-dimensional grid of pixels.
Each pixel's data is encapsulated in a Pixel object.

.. table:: Table 1: Picture functions and methods to get started(pictures)

        ================================    ==================================================================
        Picture functions                   Assume that pic is a Picture object
        ================================    ==================================================================
        makePicture(filename)               Takes a string describing a filename and creates a Picture object
        getWidth(pic)                       Returns the width in pixels (the x dimension) of pic
        getHeight(pic)                      Returns the height in pixels (the y dimension) of pic
        getPixels(pic)                      Returns a list containing all the Pixel objects from pic
        getPixel(pic, x, y)                 Returns the Pixel object at column x and row y in pic
        **Picture methods**                    Assume that pic is a Picture object
        pic.getWidth()                      Returns the width in pixels (the x dimension) of pic
        pic.getHeight()                     Returns the height in pixels (the y dimension) of pic
        pic.getPixels()                     Returns a list containing all the Pixel objects from pic
        pic.getPixel(x, y)                  Returns the Pixel object at column x and row y in pic

        ================================    ==================================================================




Pixel objects contain information about the color at their location
in the grid, and also where that location is. With a Pixel, you can
either access the color as a Color object, or as its three
components: red, green, and blue values, which are integers between
0 and 255. Table pixels contains the most useful pixel functions
and methods.

.. table:: Table 2: Pixel functions and methods(pixels)

        ================================    ==================================================================
        Pixel functions                     Assume that pix is a Pixel object
        ================================    ==================================================================
        getRed(pix)                         Returns a number representing the red component of pix's color
        getGreen(pix)                       Returns a number representing the green component  of pix's color
        getBlue(pix)                        Returns a number representing the blue component  of pix's color
        getColor(pix)                       Returns a Color object that is the color of pix number
        setGreen(pix, num)                  Sets the green part of pix to be the input  number
        setBlue(pix, num)                   Sets the blue part of pix to be the input  number
        setColor(pix, color)                Sets the color of pix to the color object passed in
        getX(pix)                           Returns the x coordinate (column) of the pixel's location
        getY(pix)                           Returns the y coordinate (row) of the pixel's location
        **Pixel methods**                       Assume that pix is a Pixel object
        pix.getRed()                        Returns a number representing the red component of pix's color
        pix.getGreen()                      Returns a number representing the green component of pix's color
        pix.getBlue()                       Returns a number representing the blue component of pix's color
        pix.getColor()                      Returns a Color object that is the color of pix
        pix.setRed(num)                     Sets the red part of pix to be the input number
        pix.setGreen(num)                   Sets the green part of pix to be the input number
        pix.setBlue(num)                    Sets the blue part of pix to be the input number
        pix.setColor(color)                 Sets the color of pix to the color object passed in
        pix.getX()                          Returns the x coordinate (column) of the pixel's location
        pix.getY()                          Returns the y coordinate (row) of the pixel's location
        ================================    ==================================================================



.. table:: Table 3: Useful color functions and methods(colors)

    ================================    =========================================================================
        Color functions                 Assume that col is a Color object
    ================================    =========================================================================
        makeColor(r, g, b)              Takes three numbers and creates a Color object
        makeDarker(col)                 Takes a color and returns a new color that is darker
        makeLighter(col)                Takes a color and returns a new color that is lighter
        pickAColor()                    Lets you select a color using visual tools
        distance(col1, col2)            Takes two colors and returns a number for  how different the colors are
        **Color methods**                   Assume that col is a Color object
        col.getRed()                    Returns the red component of col
        col.getGreen()                  Returns the green component of col
        col.getBlue()                   Returns the blue component of col
        col.distance(col2)              Takes a second color and returns the distance between them
    ================================    =========================================================================




A Color object represents a specific color. You can access the
Color object associated with a Pixel, or you can construct colors.
Each color has three values associated with it: a red value, a
green value, and a blue value. The mixture of those three values
defines the color. To make a new color, you can either specify the
RGB values with `makeColor`, or use `pickAColor` to select a color
visually. Table colors lists the most useful color functions and
methods. Note that the `distance` function (or method) uses a
three-dimensional variant on the Pythagorean Theorem to compute its
distance. The formula below defines distance, assuming that
:math:`r_1`, :math:`g_1`, and :math:`b_1` are the values for
the first color, and :math:`r_2`, :math:`g_2`, and
:math:`b_2` are the values for the second color.

:math:`{distance} = \sqrt{(r_1 - r_2)^2 + (g_1 - g_2)^2 + (b_1 - b_2)^2}`


Try this:
^^^^^^^^^

Define a list `pixList` to be the result of calling `getPixels` on
the butterfly picture. How many pixels are in the butterfly
picture?

Try this:
^^^^^^^^^

The function below increases or decreases the amount of red in a
picture by multiplying the red value of each pixel by some factor.
Try this out on a picture or two. Use `show` to see the picture,
then call `changeRed` on the picture, with some factor or other.
.. note:: you must call `repaint` on the picture to see the changes.
What happens if you keep either increasing or decreasing the amount
of red in a picture?

.. sourcecode:: python

    def changeRed(picture, factor):
        for pix in getPixels(picture):
            redVal = getRed(pix)
            newVal = factor * redVal
            if newVal > 255:
                newVal = 255
            elif newVal < 0:
                newVal = 0
            setRed(pix, newVal)

    # example calls:
    # >>> horsePic = makePicture("horse.jpg")
    # >>> show(horsePic)
    # >>> changeRed(horsePic, 2.0)
    # >>> repaint(horsePic)




Try this:
^^^^^^^^^

Create a copy of `changeRed` called `changeAll`. This new function
should also modify the green value and the blue value by
multiplying by the same factor. What effect does it have?

Manipulating Sounds
-------------------

Sound objects contain a sequence of Samples. In this case, the
Samples are similar to Pixel objects, in that they connect a
location in the sequence of Samples with the actual numeric sample
value. However, since Sounds are one-dimensional, and each sample
consists of only a single value, it is often much more useful to
bypass the Samples and access the Sample values directly. Therefore
I will show you a slightly different set of functions than Guzdial
does. Table sounds lists the functions and methods that are most
useful for now.

.. table:: Table 4: Sound function and methods(sounds)

        ================================  ===============================================
        Sound functions                   Assume that snd is a Sound object.
        ================================  ===============================================
        getDuration(snd)                  Returns the length in seconds of snd
        getLength(snd)                    Returns the length in samples in snd
        getNumSamples(snd)                Another name for getLength
        getSamplingRate(snd)              Returns the number of samples per second in snd
        getSampleValueAt(snd, pos)        Returns the value of the sample at
        setSampleValueAt(snd, pos, val)   Sets the value at pos in snd to be val
        ================================  ===============================================

.. table::

        ================================  ================================================
        Sound methods                     Assume that snd is a Sound object.
        ================================  ================================================
        snd.getNumSamples()               Returns the number of samples in snd
        snd.getSamplingRate()             Returns the number of samples per second in snd
        snd.getSampleValueAt(pos)         Returns the value of the sample at  pos in snd
        snd.setSampleValueAt(pos, val)    Sets the value at pos in snd to be val
        ================================  ================================================

Try this:
^^^^^^^^^

Load a sound object into JES. Then, using the `getSamplingRate` and
`getNumSamples` functions, calculate what the length in seconds
ought to be. Then compare your value to the value returned by
`getDuration`.

The function below is very similar in structure to the `changeRed`
function for images, above. In this case, it is changing the volume
of the sound object.

.. sourcecode:: python

    def changeVolume(sound, factor):
        for pos in range(getNumSamples(sound)):
            oldVal = getSampleValueAt(sound, pos)
            newVal = factor \* oldVal # value may overflow if too big or too small, so bound it!
                if newVal > 32767:
                    newVal = 32767
                elif newVal < -32768:
                    newVal = -32768
                setSampleValueAt(sound, pos, newVal)



Try this:
^^^^^^^^^

Listen to a sound, then change it using the function above. Can you
hear the difference? Use the Sound Tool (under the `Mediatools`
menu) to look at the original and the changed sound. Can you see
the difference there?

Raise the volume high enough to generate some "clipping." Clipping
occurs when the amplitude of the wave exceeds the maximum value we
can represent, and the peaks and valleys get flattened on top, as
if their tops have been cut off. What happens if you then reduce
the volume by calling `changeVolume` with a factor between 0.0 and
1.0?

Try this:
^^^^^^^^^

Create a new sound function called `addNoise` that is similar in
form to `changeVolume`. Import the `random` module before the
function definition. Inside the `for` loop, for each sample value,
generate a random integer in the range between -1000 and +1000 (see
below for how to do this). Instead of multiplying the old sample
value by some factor, add this random value to it. How does the
result sound different than the original? What happens if you
increase or decrease the range of random values?

.. sourcecode:: python

    >>> import random
    >>> random.randint(-1000, 1000)
    923
    >>> random.randint(-1000, 1000)
    -104



Challenge problems
------------------

Try this:
^^^^^^^^^

Create a function `removeBlue` that takes a picture as its input.
It should iterate over all the pixels in the image, setting the
blue values to be 0.

Try this:
^^^^^^^^^

Create a function `dampen` that takes a sound object and a
`threshold` number as its inputs. It should change small positive
or negative values to be zero. In other words, positive sample
values between 0 and `threshold` should be set to zero, and
negative sample values between `-threshold` and 0 should also be
set to zero. What is the effect of this function on a sound?

Try this:
^^^^^^^^^

Create a function `makeFrame` that takes a picture, a color object,
and an integer, `frameWidth`, as inputs. The function should
iterate over the pixels of the picture. If the pixel is within
`frameWidth` of the edge of the picture, then set the pixel's color
to be the input color value. If it is not within that range, then
leave the pixel unchanged. The key for this function is to put a
conditional inside the loop. The tests for the `if/elif` should
determines whether a pixel is close enough to one of the edges of
the picture.


Try this:
^^^^^^^^^

Create a function `allPositive` that takes a sound object as its
input. It should convert all negative values to positive. What is
the effect of this change?

.. [1]
   Mark Guzdial is involved in both the Myro and JES projects

