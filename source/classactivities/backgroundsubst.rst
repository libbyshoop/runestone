Background Substitution and Chromakey
=====================================

There are two main methods used to replace the
existing background of a picture with some second background. We
will look at these two methods with this activity. First, look at
the Photo Booth application on the Macs (look in the Applications
folder). Click on the "Effects" button, and go to the third screen
of effects. This screen performs background substitution to put
your image in front of a picture or video. Try it out. Next, take a
look at the following video on Moodle: Weatherman Wearing a Green
Tie. Weather forecasters typically use chromakey or "green screen"
technology to place themselves in front of images. In this video,
the weatherman wore a green tie accidentally and you can see a
glimpse of how the chromakey algorithm works.

After Monday,get a copy of the `greenscreenFiles.zip` file from
Moodle. This file will contain pictures of you and your classmates
in front of our homemade green screen, at least one picture of the
blank green screen, and several background pictures that are a good
size to use with these techniques. If you start this on Monday,
look for Guzdial's examples, including a homemade "bluescreen."

Background Substitution
-----------------------

Background substitution uses an image of the background we want to
replace, an image with that background and the foreground objects
in it, and the new background we want to use in place of the
original background. Three images. Make sure that the new
background is at least as big as the other two pictures.

Below is the background substitution algorithm, written in
pseudocode:

::

    1. BackSubstitute(forePic, oldBack, newBack)
    2. Create a new picture the same size as the foreground picture
    3. for every x index in the new picture
    4.   for every y index in the new picture
    5.      get the pixels at (x, y) in all four pictures
    6.      set col1 = the color of the foreground pixel
    7.      set col2 = the color of the old background pixel
    8.      if col1 is close enough to  col2 then
    9.          Set the new pixel's color to the new background pixel's color
    10.     else
    11.         Set the new pixel's color the the foreground pixel color
    12. return the new picture



Try this:
^^^^^^^^^

Write a background substitution function for JES, based on the
pseudocode above. Test it on the picture of an empty chair and the
picture of you, or all `wall.jpg` and `wall-two-people.jpg`
provided by Guzdial. You can also look at `movie-background.jpg`
and the files in the `kids-in-bg-seq` folder. The tricky part for
background substitution is determining what "is close enough to"
means: I recommend you use the `distance` function, and then try
varying the threshold value to see how well you can do.

This is *hard* to do well: when making movies the boundaries of
foreground versus background are often laid out by a human being by
hand.

Chromakey
---------

Chromakey is different from background substitution because we
control the background environment and make it be a single color.
This is sometimes called greenscreen or bluescreen technology.
Instead of matching the foreground pixel colors to an old
background picture, we check if the colors lie in some acceptable
range of colors we've selected from the background. It can work
very well, but works best with controlled lighting and camera
effects, as well as careful choice of clothing (and makeup).

Below is pseudocode for the Chromakey algorithm. It is very similar
to the back substitution above, but involves fewer pictures. I have
separated the if statement into a separate function, to make it
easier to experiment with different approaches to detecting the
background color.

::

    1.    Chromakey(forePic, newBack)
    2.    Create a new picture the same size as the foreground picture
    3.    for every x index in the new picture
    4.      for every y index in the new picture
    5.          set forePix = the pixel at (x, y) in the foreground picture
    6.          set newPix = the pixel at (x, y) in the new picture
    7.          set backPix = the pixel at (x, y) in the new background picture
    8.          if pixelIsBackground forePix then
    9.              Set the new pixel's color to the new background pixel's color
    10.          else
    11.              Set the new pixel's color the the foreground pixel color
    12.    return the new picture


To define the pixelIsBackground function, you
could use the built-in `distance` function and pick a middle green
(or blue) color value from your backdrop. Or, you could look at the
range of red, green, and blue values across all the backdrop
pixels, and check for those ranges (this can allow for more
variability in the red values than the green, for example). Or any
other method you can think of!

Try this:
^^^^^^^^^^

Implement the `chromakey` function, based on the pseudocode above.
Define a helper function `pixelIsBackground` that takes a pixel as
input, and determines whether it belongs to the foreground or
background of the picture. The easiest apporach is to use the
`distance` function comparing the pixel's color to a typical green
color from your background. Try this first, then get fancy!


