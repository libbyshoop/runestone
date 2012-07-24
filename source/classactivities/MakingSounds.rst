Making Sounds
=============

This activity will look at tools in JES for creating
sound waves from scratch. This is what synthesizers do to generate
different pitches.

Making sound waves
------------------

Synthesizers and electronic keyboards typically use three methods
to produce sounds: One is simply to output a recorded sound as is.
A second method samples from a recorded sound at different rates,
changing its pitch. This is often used to generate synthesized
instrument sounds, like piano or violin. The third method generates
sound waves of a particular shape.

The sine wave makes a very pure, pretty sound. Here is what a sine
wave looks like (more or less):

    .. figure:: Images/sinewave.jpg
       :align: center
       :alt: image

       Sine Wave


In the file `makingsounds.py` you will find a function called
`sinewave`, which creates a sound object the correct length long,
and then computes the values for a sine wave with the given
frequency and amplitude. Try out the examples in the file, or other
examples, and use the `explore` tool to look at the resulting wave
form.

The sine wave is rather expensive to calculate, and we want
different kinds of sounds, so other wave forms can be generated.
The square wave is very simple, just flat sequences at the
amplitude and the negative amplitude. Here is what a square wave
might look like (there is a function for generating square waves in
the file):

    .. figure:: Images/squarewave.jpg
       :align: center
       :alt: image

       Square wave


The triangle wave is slightly better sounding than a square wave,
but a bit more complex to calculate. Take a look at the program,
and see how it generates this form:

    .. figure:: Images/trianglewave.jpg
       :align: center
       :alt: image

       Triangle Wave


Try this:
^^^^^^^^^

If you feel you understand these three, make a sawtooth wave
function. This function will be similar to the triangle shape,
except that it should rise from `-amplitude` to `+amplitude` over
the length of the whole cycle, and then it should start over: with
a straight drop from `+amplitude` to `-amplitude` between one
sample and the next. See below for an example:

    .. figure:: Images/sawtoothwave.jpg
       :align: center
       :alt: image

       Sawtooth Wave


Making tunes
------------

JES includes a function `playNote`, described in the chapter on
generating sounds. This function takes a note number, a duration in
milliseconds, and an intensity, and it generates a simulated piano
tone. Try the `tune` function in the `makingsounds.py` file. If you
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
differences. For instance you might input `"A4 flat"` and it should
produce the A flat note just below middle C on the piano.

Then, write a function that takes a list of strings describing
notes. This function should play the tune described by the list of
strings, using the earlier function to convert each string to its
corresponding number.

Get really fancy and add to each note string something that
indicates duration, and modify your function so it can play lists
that describe tunes with notes and durations and even loudness.


