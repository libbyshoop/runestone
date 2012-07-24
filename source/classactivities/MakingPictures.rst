Making Pictures
===============

This activity will look at tools in JES for drawing
pictures from scratch. Using these tools, you can create and
animate simple scenes. Get a copy of the `makingpictures.py` file.

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
    >>> repaint(p) # Keep using repaint, but I'm going to leave it out
    >>> addRect(p, 150, 10, 200, 210)
    >>> addRectFilled(p, 300, 300, 75, 75, makeColor(220, 102, 192))
    >>> addArc(p, 20, 20, 100, 30, 0, 180, blue)
    >>> addArcFilled(p, 10, 400, 75, 75, 90, 90, makeColor(25, 160, 38))
    >>> addOvalFilled(p, 350, 20, 100, 75, yellow)
    >>> addText(p, 200, 350, 'Hi there!', orange)



Here is a table that describes each of the basic drawing functions
and what its inputs are:

        ====================    ===========================================================================
        `Function name`          `Call form and description`
        ====================    ===========================================================================
        `addLine`               `addLine(picture, startX, startY, endX, endY, color)`

                                Draws a line on the input picture. The line starts with the pixel
                                at `(startX, startY)` and goes to the pixel at `(endX, endY)`. The
                                `color` input is optional; if you leave it out the line will be
                                black, otherwise the line is the color given. The `color` variable
                                must be a Color object.
        `addRect`               `addRect(picture, startX, startY, width, height,color)`

        `addRectFilled`         `addRectFilled(picture, startX, startY, width,height, color)`

                                Draws a rectangle on the input picture. The upper left corner of
                                the rectangle is at `(startX, startY)` and it has the given width
                                and height. Color is, as always, optional. The `addRect` function
                                draws an outline rectangle, and `addRectFilled` draws a filled-in
                                rectangle.
        `addText`               `addText(picture, startX, startY, text, color)`
                                Draws text on the input picture. The lower left corner of the
                                text starts at `(startX, startY)`.
        `addOval`               `addOval(picture, startX, startY, width, height,color)`

        `addOvalFilled`         `addOvalFilled(picture, startX, startY, width, height, color)`

                                Draws an oval or circle on the input picture. The coordinate
                                `(startX, startY)` and `width` and `height` specify the
                                dimensions of a rectangle inside which the oval is drawn.
        `addArc`                `addArc(picture, startX, startY, width, height,startAngle, angle, color)`

        `addArcFilled`          `addArcFilled(picture, startX, startY, width,`
                                `height, startAngle, angle, color)`

                                Draws an arc or wedge on the input picture. The next four inputs
                                specify a rectangle, once again, inside which the arc will be
                                drawn. The last two required inputs specify where the arc starts
                                and how far it extends. The `startAngle` input should be an angle
                                in degrees. Zero degrees points to the right, 90 degrees points
                                upwards, and so on. The `angle` input tells how far the arc should
                                proceed, in degrees; its value may be positive (counterclockwise)
                                or negative (clockwise)
        ====================    ===========================================================================


Text with Style
---------------

You can create text that has different styles using the
`addTextWithStyle` option. You create a Style object that describes
the font, its size, and other details, and then you add text with
that style. The example below shows two different styles being
drawn. If the fonts below are not working, you will need to figure
out what fonts are available on your computer. I have written a
function to help you do this: `listAllFonts` that will list the
fonts available to JES on any given computer. You can find this
function in the `makingpictures.py` file. I have also written a
program, `displayAllFonts`, that will display the different styles,
show plain, italic, and bold versions of each one.

.. sourcecode:: python

    str1 = "Big font with attitude"
    style1 = makeStyle("Braggadocio",bold, 48)
    addTextWithStyle(p, 10, 200, str1, style1)
    str2 = "Little cute font"
    style2 = makeStyle("Gill Sans", plain, 10)
    addTextWithStyle(p, 50, 300, str2, style2, magenta)



Below is a table that summarizes how to use the two functions shown
here.

        ====================    ======================================================================
        `Function name`         `Call form and description`
        ====================    ======================================================================
        `makeStyle`             `makeStyle(fontName, emphasis, size)`
                                Creates a Style object that represents a particular combination
                                of font, emphasis, and font size. The `fontName` input must be a
                                string, a valid name for a font on this computer. Emphasis can be
                                either `plain`, `italic`, `bold`, or `italic + bold`.
                                Size is the font size, defined as usual.
        `addTextWithStyle`      `addText(picture, startX, startY, text, style,color)`

                                Draws text in a fancy font on the input picture. The lower left
                                corner of the text lies at `(startX, startY)`. The text must be a
                                string. The `style` must be a Style object, the result of calling
                                `makeStyle`.
        ====================    ======================================================================


Things to try
-------------

Try this 0:
^^^^^^^^^^^

In the `makingpictures.py` file, look at the `drawSmiley1`
function.


-  Change the function so that the smile is drawn in blue instead
   of red.

-  Change the function so the smiley face is drawn on a rectangle
   instead of a circle

-  Change the function so that it draws a frowney face instead of a
   smiley face.

-  Change the function so that it draws the face at 100, 50 instead
   of at 20, 20.


Look at the `drawSmiley2` function, which takes a picture as input,
but also an (x, y) coordinate where the picture should be drawn.
Note that one object, the background circle, is drawn at the input
(x, y) position, but all the others are drawn at offsets of that
position.

Try this 1: Draw a Sign:
^^^^^^^^^^^^^^^^^^^^^^^^

Create a function called `storeSign` that takes a picture object as
its input. It should draw a fanciful store sign, like the neon sign
for a diner or something like that, on the input picture. Make sure
the sign has at least three elements to it. Don't make the sign too
big, we're going to want to draw it in different places on the
picture next.

Try this 2: Draw the sign anywhere you want:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, create a new version of the function, called `storeSign2`,
that takes a picture object, and a starting x and y value. This
function should draw the sign so that the upper-left corner of the
sign is located at (x, y). Decide what the upper-left corner of the
sign is, and then figure out how to specify the positions in the
rest of the object as "offsets" from the upper-left corner.

Look at the `drawSmiley2` function I've provided in the file for an
example of how to do this.

Try this 3: Make the sign blink!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new program `blinkSign` that takes a picture as its input.
It draws the sign in a particular location, and then has it blink
on and off (note that you can call `storeSign2` to help draw the
sign as one step in this new program). This will only really work
if you have a plain background for the picture. To erase a drawn
picture, draw a rectangle that is the background color over it. To
make the blinking take some time, import the `time` module, and use
the `sleep` function within it, which acts much like the `wait`
function Myro provides, except it is normal Python. See the
`drawingWithPauses` function for an example.

.. sourcecode:: python

    >>> p = makeEmptyPicture(500, 300)
    >>> drawingWithPauses(p)



Try this 4: Make the sign shimmy!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is common these days to see computer-generated animations that
try to look crudely hand-drawn by having the shapes move around a
little bit. Create a program that does this, by drawing the sign in
a random location close to some main set of coordinates.

Try this 5: Make the sign glide!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the sign glide across the screen from left to right, by
drawing it, waiting, and then erasing it and drawing it further
over.


