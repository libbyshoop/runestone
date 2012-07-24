Blending Images and Sounds
==========================

Blending of images and sounds operates on the same
principle. To blend together two images, we set up a correspondence
between pixels in one image and pixels in a second image, and we
average their colors together (average the red values, green
values, and blue values separately, as we've done before). To blend
together two sounds, we set up a correspondence between samples in
the sound, and we average corresponding sample values together.

Complete overlay of images
--------------------------

Suppose you want to blend together two images. You can imagine
laying one image on top of the other, and then averaging together
the colors of corresponding pixels. The only possible complication
is if the two pictures are not the exact same size. See the picture
below for an example; we want to blend together the blue picture
with the red picture, but the red picture is taller and the blue
picture is longer.

    .. figure:: Images/fullOverlap.jpg
       :align: center
       :alt: image

       full Overlap


In this case, we need to make a new picture whose dimensions are
the region that shows the purple blending (outlined by a green
box). This picture will have as many columns as the minimum of the
column sizes of the two starting pictures, and as many rows as the
minimum of the row sizes of the two starting pictures.

Try this:
^^^^^^^^^

Define a function `totalBlend` that takes two pictures as inputs.
It should first create a new picture with the proper dimensions.
Then it should loop over the rows and columns of the new picture.
For each pixel in the new picture at position :math:`(x, y)`, the
function should look up the pixel in the first picture at
:math:`(x, y)`, and the pixel in the second picture at
:math:`(x, y)`. It should blend together red, green, and blue
values from those two pixels, and set the color of the new
picture's pixel to be the result. Be sure to return the new picture
at the end.



Blending sounds, part 1
-----------------------

Blending sounds works in much the same way as blending images. We
align two sound objects, conceptually, and average together
corresponding sample values.

Try this:
^^^^^^^^^

Try defining a function `soundBlend` that takes two sound objects.
It should make a new sound object that is the length of the shorter
of the two. For every sample value position in the new sound, look
up the corresponding sample values in the input sounds, average
them, and set the result to be the value in the new sound.


Partial overlay of images
-------------------------

Suppose that you want to overlay two images, but not overlap them
completely. The picture below illustrates this. We want to overlap
the blue picture and the red picture, forming a new picture
indicated by the green box.

    .. figure:: Images/overlapblend.jpg
       :align: center
       :alt: image

       Overlap Blend

You will be defining a function `blendHoriz` that takes two picture
objects and a number, `overlapWidth` as inputs. The `overlapWidth`
number is the number of pixels to overlap the two pictures.

The first task is to figure out the width and height of the new
picture. Its height should be the smaller of the heights of the
input pictures. Its width should be the sum of the widths of the
two pictures, *minus* the overlap width.

Start the function:
^^^^^^^^^^^^^^^^^^^

Write the first few lines of the function, to calculate the new
width and height, and make a new, empty picture of that size. Show
the new picture, and return it at the end of the function. Debug
these lines before moving on, making sure that the new picture
seems to be the right dimensions.

Break the problem into parts:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The next task is to figure out the formulas for mapping pixels in
the target picture onto the source pictures. There are three
separate sections of the target picture to consider: the left part
that comes only from the first picture object, the middle part
where the blending actually takes place, and the right part that
comes only from the second picture. Work on each section
separately, whether you write three separate sets of loops, or one
set of loops with three different `if-elif` sections within it.

First part:
^^^^^^^^^^^

When the pixel values come only from the first picture object, the
copying is mostly easy. For a pixel in the new picture at position
:math:`(x, y)`, the source pixel is the one at :math:`(x, y)`
in the first picture. The only tricky part is figuring out where
the boundary is between this section and the next, where blending
takes place.

Consider a concrete example to help with this. Suppose that the
first picture is 480 pixels wide, and we want an overlap of 200
pixels. The x values in the first picture will run from 0 up to
479. For an overlap of 200, the overlap section will run from 479 -
200 = 279 to 479. That means the last unblended x value is 278.
Generalize this example to make a formula that would work for any
picture width and overlap width.

Create nested `for` loops that loop over the x and y values to copy
the pixels from the first picture into the left portion of the new
picture. Be sure that you are returning the new picture *after*
these loops.

Blended part:
^^^^^^^^^^^^^

For the blended section, we have already figured out the range of x
values that will be blended (see two paragraphs above). The new
picture's :math:`(x, y)` pixel will take on the average of a
pixel from the first picture and a pixel from the second picture.
As before, the first picture's pixel will be the one at
:math:`(x,y)`. The pixel from the second picture is more tricky.
Its :math:`y` value will be the same as the :math:`y` values of
the new picture. But its :math:`x` value needs more thought.
Imagine the concrete example from above. In the first blended
column, when :math:`x = 279`, we want to get the pixel from the
second picture at column 0. Similarly, when :math:`x = 280`, we
want the pixel at 1. Thus, to compute the :math:`x` value for the
second picture, we want to take the new picture's x value, and
subtract the starting point, :math:`279`!

Add to your function a part that iterates over the locations in the
blended section of the new picture. Read the values from the
correct pixels of the input pictures, and average their red, green,
and blue values. Set the new picture's corresponding pixel to have
that color.

Last part:
^^^^^^^^^^

The last section is, again, more simple. It simply needs to copy
the pixel color from the second picture. The only complication is
knowing what column it starts in (the width of the first picture),
and how to map :math:`x` values from the new picture to
:math:`x` values in the second input picture. This part follows
the same rule as the blended section.



Blending sounds, part 2
------------------------

Try this:
^^^^^^^^^

Create a function called `offsetBlend` that takes two sound objects
as inputs, along with a number of seconds qto overlap. Given that
you know that sampling rate of the two sounds (make sure you pick
sounds that have the same sampling rate!), compute the number of
samples in the overlap by converting seconds to samples, and
turning it into an integer.

Once you know the number of samples to overlap, you can figure out
the length of the new sound as the sum of the lengths of the two
inputs sounds, minus the size of the overlap.

Filling in the sample values is a similar idea as for images: the
first section of the sound is copied from the first input sound,
the second section is the average of the two sounds, and the last
section comes from the second input sound. Figure out how sample
positions correspond, and write three loops that do the copying.

What happens when you pass the same sound object to `offsetBlend`
twice, as both input sounds?



Echoes
------

An echo can be created by blending a sound with itself. Make a copy
of `offsetBlend`, change its name to `oneEcho`. First of all, pass
in only one sound object, and modify your code to read from two
different locations in the sound object rather than two different
sounds.

An echo is usually not quite as loud as the original sound. We can
simulate that by not doing an even average of samples in the
blended section. Try, instead, computing the blended value as 0.75
times the first sample value, plus 0.25 times the second sample
value. Experiment with different percentages.

Challenge question:
^^^^^^^^^^^^^^^^^^^

Can you make an analogous function for images, that blends a
picture with itself to make a visual "echo"?




