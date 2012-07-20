Posterizing and Blurring
========================

This activity looks at a couple of the examples from
Chapter 5, of more advanced image manipulations. The *structure* of
these functions is no different than what we have done before,
though what we do within the structure may be.

Posterizing
-----------

Posterizing modifies a picture so that fewer colors are used. It
derives from certain printing processes that might only have four
or five different colors to mix.

First kind of posterizing
~~~~~~~~~~~~~~~~~~~~~~~~~

Look at the first program in the file `posteretc.py`. Run the
`posterize` function on some pictures and notice the results.
Figure out what each piece of the program does. What is the purpose
of `modifyColor`, and what is the purpose of `scaleCValue`?

Try this:
^^^^^^^^^^

Change the `scaleCValue` function so that, instead of limiting each
red, green, or blue value to one of two values, it can take on one
of four values: divide the range from 0 to 255 into four sections.
Can you extend it to five, six, or eight sections?

Second kind of posterizing
~~~~~~~~~~~~~~~~~~~~~~~~~~

Next in the file is a second approach to posterizing. In this case,
instead of limiting the values that red, green, and blue can take
on, we will provide a list of colors and require that each pixel
take on the closest color from the list. Note that I have provided
a helper function called `makeColorList` for building such a list.

Try the following to create lists of colors:

.. sourcecode:: python

    >>> color3 = makeColorList(3)
    >>> color5 = makeColorList(5)



Questions to consider:
^^^^^^^^^^^^^^^^^^^^^^

Try making lists with 3 to 10 colors, then posterize a picture
using your lists. How well does it work? What happens if you pick
only shades of green? How does the time taken change as the number
of colors in the color list increases? Is this version faster or
slower than the other? Which results do you like better?

Blurring images
---------------

Blurring a picture might be done after scaling a picture up, or to
remove ugly digital "jaggies", or just for effect. It is usually
done by averaging together the colors of pixels in a small
neighborhood, and then setting the center of the neighborhood to be
the average color.

In the file there is a blur function, that uses a neighborhood of
nine pixels, a 3x3 grid (another way to think about it is that we
look at all pixels whose x or y value is within one of the central
pixel).

Try this:
~~~~~~~~~

Make a copy of this program, including `blurPic` and
`avgNeighborhood`. Modify the function `aveNeighborhood` so that
it takes an extra input, `size`. If 1 is input for `size`, then the
function should act just like the original, averaging over a 3x3
neighborhood centered on the pixel at :math:`$(x, y)$`. If 2 is
input, then the neighborhood size should be 5x5, etc.

Next: Modify `blurPic` so that it takes an extra input, `size`, for
the neighborhood size. Pass the neighborhood size to the new
`avgNeighborhood`. How does the effect change as the neighborhood
size grows?
*Only test this on fairly small neighborhood sizes, or it  will be too slow!*

Challenge: Weighted averages for blurring
-----------------------------------------

Many real-world blur functions don't use a straight average,
instead they apply a 2-dimensional function like a Gaussian
function (a bell curve), centered on the main pixel. Each pixel in
the neighborhood is multiplied by a different weight value: the
weight value is determined by the function being applied. You can
do this by specifying the set of weights for the neighborhood.
There is a lot of mathematics behind these methods for blurring,
but for our purposes we will refer to a "kernel" as a
two-dimensional matrix of values by which to multiply each
neighbor. In the examples below, the kernel on the left represents
a straight average of all neighbors (note that 0.11 is 1/9). On the
right is a kernel that emphasizes the diagonal elements over the
central ones. In the middle is a kernel that estimates a Gaussian
function.


        ====== ====== ======
         0.11   0.11   0.11
         0.11   0.11   0.11
         0.11   0.11   0.11
        ====== ====== ======

            ====== ====== ======
             0.06  0.13   0.06
             0.13  0.24   0.13
             0.06  0.13   0.06
            ====== ====== ======


                ====== ====== ======
                0.16   0.05   0.16
                0.05   0.16   0.05
                0.16   0.05   0.16
                ====== ====== ======


Try this:
~~~~~~~~~

Make another copy of the original blurring program. Modify the
`blurPic` function so that it takes in a list of lists that
represents a kernel to use in blurring. The kernel will be a list
containing lists. Each sublist represents a row of values in the
kernel, and each value in each sublist is a real number. The values
in the kernel should add up to 1.0. The `blurPic` function should
pass the kernel list to the new `avgNeighborhood` function. This
function should now use the values in the kernel list to determine
how combine the red, green, and blue values.

Blurring sounds
---------------

Blurring a sound is a similar process to blurring a picture: we can
take adjacent sample values and average them together. As for
pictures, we might want to blur a sound that has been scaled to a
lower pitch, to smooth the jaggedness that results, to remove high
frequency noise, or to disguise the sound.

Try this:
~~~~~~~~~

Define a program for blurring a sound that takes in the sound
object. It should use a helper program for averaging the
neighboring sample values. Make your program take in a sound and a
number that represents how many sample values on either side of the
central sample make up its neighborhood. Test your program with
different sizes of neighborhoods. How does increasing the
neighborhood affect the resulting sound?

