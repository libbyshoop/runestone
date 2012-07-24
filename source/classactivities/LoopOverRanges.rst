Looping Over Positions of Pixels and Samples
============================================

Today we'll look at several different image
manipulations that involve looping over the locations of pixels in
the image, and sound manipulations that loop over locations, as
well. In particular, we will look at problems that may not require
us to touch every pixel or sample in an image or a sound.

Looping over pixel locations
----------------------------

**Big Idea:** When we write this kind of function, typically we
choose either source pixels or target pixels as the "main" ones,
and we write `for` loops that repeat over all the (x, y) values for
those pixels. For the other (x, y) values we need, we must either
compute them based on the `for` loop variables, or keep track of
them with variables that are not part of a `for` loops, but that we
manage independently.

Try this as a warm-up:
^^^^^^^^^^^^^^^^^^^^^^

Suppose we wanted to find out the average color of a picture, or a
portion of a picture. It turns out that we can calculate the
average color over a set of pixels by computing the average red
value of the set, and the average green value over the set, and the
average blue value over the set. Combining together the average
red, green, and blue values produces the average color.

To find the average over an entire picture, we could use the same
kind of loop as you were using last week, over the list of all the
pixels. But you might also want to loop over all the rows and
columns: that makes it easier to modify the program so that it can
work on only a portion of a picture.

Below is an outline of what the loops in these functions typically
look like. Note that these loop will touch each pixel in the
specified range in vertical stripes from the left edge of the
picture to the right edge.

.. sourcecode:: python

    def outlineOfFunction(pic):
        ...
        for x in range(getWidth(pic)):
            for y in range(getHeight(pic)):
                pixel = getPixel(pic, x, y)
                ...
        ...



Define a function `averageColor` that takes one input, a picture
object. Using nested `for` loops like the outline above, the
function should determine and *return* the average color over the
picture. Below are some examples for pictures in the MediaSources
folder.

Use four accumulator variables to store the sum of the red values,
the sum of the green values, and the sum of the blue values, and
the number of pixels. Inside the loop, add to each accumulator
variable the next pixel's color channel values. After the loop,
compute the average red value, average green value, and average
blue value. Then, use `makeColor` to create a color object with
those values, and return that color object.

.. sourcecode:: python

    >>> p1 = makePicture("shops.jpg")
    >>> averageColor(p1)
    Color(123,115, 88)
    >>> p2 = makePicture("butterfly2.jpg")
    >>> averageColor(p2)
    Color(113, 132, 79)
    >>> p3 = makePicture("blackcat.jpg")
    >>> averageColor(p3)
    Color(75, 49,45)



Try this:
^^^^^^^^^

Once you can get the average color over the whole picture, you can
change it to average over just a region without much work. Create a
copy of `averageColor`, called `averageRegion`, that takes five
input values. The first should be a picture, the second two specify
the (x, y) values for the upper left corner of a rectangle, and the
last two specify the (x, y) values for the lower right corner of a
rectangle. The function will determine the average color within
that rectangle. The only parts of this copy that need to change are
the calls to `range` in each `for` loop. Instead of looping from 0
to the width or height of the picture, we only want to loop from
the starting x value to the ending x value (plus 1), and similarly
for the y values. Make this change. Here are some examples:

.. sourcecode:: python

    >>> averageRegion(p1, 22, 226, 63, 248)
     Color(227, 198, 53)
    >>>averageRegion(p2, 139, 11, 194, 71)
    Color(167, 204, 81)


Challenge question:
^^^^^^^^^^^^^^^^^^^

Write a function `patchPicture` that takes a picture and the same
kind of (x, y) coordinates as `averageRegion`. This function should
call `averageRegion` to determine the average color in its
rectangle, and it should then loop over the positions in that
rectangle,changing the color of each pixel to be the average color
of the whole rectangle. Below is an example of what this would do
if called as `patchPicture(p1, 204, 96, 239, 161)`.

    .. figure:: Images/patchedshops.jpg
       :align: center
       :alt: image

       patchedshops


Horizontal mirroring
--------------------

Guzdial talks about mirroring in the reading for today. We are
going to look at horizontal mirroring, and try to develop the code
to do it independently of the book.

Below is a tiny picture, just 5 pixels tall and 6 pixels wide. The
picture on the left is the original; the picture on the right shows
the new picture we want to make, where the top half has been
mirrored onto the bottom half.

    .. figure:: Images/mirrorOrig.jpg
       :align: left
       :alt: image

       *mirror Original*

    .. figure:: Images/mirrorTopToBottom.jpg
       :align: center
       :alt: image

       *mirror Top To Bottom*

Discuss:
^^^^^^^^

Think about the questions that follow, and then discuss them with
your partner or others nearby.


#. The "source" region of the picture is the portion we want to
   copy values from. In the sample picture above, what are the
   smallest and largest x values for the source region? What are the
   smallest and largest y values for the source region? Extrapolate to
   larger pictures: if a picture was 250 pixels wide by 370 pixels
   tall, what would be the range of x and y values that define the
   source region?

#. The "target" region of the picture is the portion we are going
   to overwrite with the mirrored values from the source region. In
   the sample picture above, what are the smallest and largest x and y
   values for the target region? For a larger picture (like the 250 by
   370 pixel example above) what would the range of x and y values
   be?

#. Consider the pixel at (3, 0) above, in the source region. What
   are the coordinates of its corresponding target pixel? For each of
   the source region pixels below, determine the corresponding pixel
   location in the target region.

          ============       =============
            Source             Target
          ============       =============
           x  ,  y              x , y
           3  ,  0
           0  ,  0
           0  ,  1
           2  ,  1
           5  ,  1
          ============       =============


#. How can we convert from a source pixel location to the
   corresponding target pixel location? Develop a general formula that
   words for any location.


Try this:
^^^^^^^^^

Write the function `mirrorHoriz`, filling in the definition I've
started below. This function introduces a new idea: instead of
changing the input picture, it creates a new picture that is a copy
of the original. We then modify the new picture and return it at
the end.

.. sourcecode:: python

    def mirrorHoriz(picture):
        w = getWidth(picture)
        h = getHeight(picture)
        newPic = duplicatePicture(picture)
        show(newPic)
        # here you must put in nested for loops to do the copying # --
        return(newPic)



Challenge questions:
^^^^^^^^^^^^^^^^^^^^

The pictures below show other ways you could mirror a picture.
Mirroring the bottom half up to the top, mirroring the left half
over the right, and mirroring the right half over the left. Make
copies of your function and try to implement each of these
variations on mirroring.


    .. figure:: Images/mirrorBottomToTop.jpg
           :align: left
           :alt: image

           *mirror Bottom To Top*

    .. figure:: Images/mirrorLeftToRight.jpg
           :align: center
           :alt: image

           *mirror Left To Right*

    .. figure:: Images/mirrorRightToLeft.jpg
           :align: center
           :alt: image

           *mirror Right To Left*


Looping over samples
--------------------

We have already looped over the locations of samples in sounds.
Today we are going to look at two different applications where we
want to loop over different parts of a sound object.

Try this:
^^^^^^^^^

There are two ways we could consider mirroring a sound. One is to
switch positive and negative values. However, because sound waves
are so repetitive, this doesn't really change anything. The second
way is to mirror the first half of the sound backwards as the
second half. Guzdial does one version of this in the chapter, but
you should try to build this function from scratch.

For this version, we will start with a sound, and will copy the
*entire sound* backwards. To do this, we will start by making a new
sound that has twice as many samples in it as the original sound.
Use `makeEmptySound` to do this. Then, copy each sample in the
original sound into the corresponding location in the new sound,
and to the mirrored location in the new sound. You might try a
small example like we did for pictures above to help you figure out
how to do this.

.. sourcecode:: python

    def mirrorSound(snd):
        length = getLength(snd)
        newLen = 2 * length
        newSound = makeEmptySound(newLen)
        # You fill in the rest with a for loop over samples

Try this:
^^^^^^^^^

Write a function `concatSounds` that takes two sound objects, and
builds a new sound object that has the two sounds spliced together.
The length of the new sound should be the sum of the lengths of the
two input sounds. Use `makeEmptySound` to create the new sound.
Then, loop over first the first sound, and then the second sound,
copying the sample values into the new sound. Be sure to `return`
the new sound.

Challenge question:
^^^^^^^^^^^^^^^^^^^

This second example is a bit more complicated. I am giving you a
partial program in the file `soundsplicing.py`. Go and read through
this program.

For this program to work you must set the media folder
(`setMediaFolder`) to be the Speech folder inside the Mediasources
folder. This program is supposed to take in a string which must be
made up of words that have corresponding .wav files in the Speech
folder (no punctuation!). My program is supposed to get the sound
files that correspond to each word, and then splice them all
together to make one big sound file.

My program depends on a function called `spliceAtPos`, that takes a
target sound object, a source sound object, and a starting index.
This function should copy the entire source sound object into the
target sound object, starting not at the beginning of the target,
but at the starting index. `Define this helper function!`









