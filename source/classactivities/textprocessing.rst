Text Processing
===============

Overview
--------

This activity will explore reading and writing text files, by
looking at the format string command, the `os` module, exceptions,
and computing the frequency of letters and words in a text
document.

**DO THIS:** For part of this activity, it is important to understand
what we mean by a `file path` on a computer. Make sure that you can
look this up and determine what that is. Write out a definition of
these terms that are related:


-  directory

-  folder

-  file

-  file path

-  current working directory (cwd)


**DO THIS:** *Create a directory for this activity* and place these
files into it:

:download:`textProcessing.py <textProcessing.py>`

:download:`alice.txt <FilesandText/alice.txt>`

:download:`macbeth.txt <FilesandText/macbeth.txt>`

:download:`mobydick.txt <FilesandText/mobydick.txt>`

:download:`emma.txt <FilesandText/emma.txt>`

The format operator
-------------------

You may find this information quite useful as you work on the rest
of these activities and other tasks you will be doing later in this
course. We often want to be able to print out strings that
"look nice" because they are formatted in a particular way.

If you have several values that you want to insert into a string,
or a piece of text, and to format in a certain way, then the
*string format method* will help you.

The concept behind string formatting is that you first create a new
string that is a template for how you will want your final printed
output to look like. Then you use the `format` operator on that
template string and give it names of variables that you wish to
print in a particular way.

Try this example script code, found at the top of
`textprocessing.py`:

.. sourcecode:: python

    ageList = [3, 17, 65, 22, 40, 18]
    tot = 0
    sumAges = 0.0
    for age in ageList:
        tot = tot + 1
        sumAges = sumAges + age
    avgAge = sumAges/tot

    print "Before formatting, the avgAge floating point number prints like this:"
    print avgAge

    print "After formatting, we can print a nice statement like this:"

    templateString = '{0:d} people have an average age of {1:4.2f}'
    strToPrint = templateString.format(tot, avgAge)
    print strToPrint



Let's examine these two lines of the above code very carefully:

.. sourcecode:: python

    templateString = '{0:d} people have an average age of {1:4.2f}'
        strToPrint = templateString.format(tot, avgAge)

The curly braces in the first line represent a place where a value
from a variable will be placed in the final string called
`strToPrint` in the second line. When considering these 2 lines
together, the 0: in the first line means that the value from the
variable `tot` will be placed there when the `format` method is
executed in the second line. The 'd' in the 0:d means that the
value expected is a decimal number (without a decimal point). In
that case we use that because we know tot should be an integer
value.

Try varying the 4 and the 2 in the first line to see what effect
they have. Note that the f code is for floating point numbers that
contain decimal points. There are many other codes, see the web
page:
http://docs.python.org/library/string.html
for more details. (Warning: some of this page is complicated; you
have to find the nuggets of use full information there. You can also
simply follow the next few examples I provide and refer to this
later when you might need it.)

Now let's look at other examples provided in `textprocessing.py`.
There are four example functions that take different kinds of
dictionaries as input.


-  formatOut

-  formatColumns

-  formatColumns2

-  formatColumns3


Please look at each of these examples and make sure that you
understand how each one works.

In `formatOut`, what is less appealing about the output format?

In `formatColumns`, what would you change if you wanted to specify
that every name should use 12 characters and then be right
justified?

`formatColumns2` shows how justification of output works when
formatting.

`formatColumns3` shows how the same template for formatting can be
used for both headings that you might put in the output and the
actual data that you ar printing, so that they line up very
nicely.

`Try this:` Suppose you had a dictionary where people's names were
of varying lengths and you did not know what the longest one was
ahead of time. Update `formatColumns3` to handle this situation by
first going through the dictionary to find the longest name in it.
Do this by completing the function called `longestName` in the
file called `textprocessing.py`. Then use the length of what is
returned by `longestName` inside of the `formatColumns3` function.
Once you have the length, you can use it inside an if statement to
vary what the templateString should look like, like this:

.. sourcecode:: python

    if longestNameLen <20 :
        templateString = '{0:<10}{1:>20}'
    elif
        ...



Set up lengths for 0 to 20, 21 to 30, and greater than 30.

The os module
-------------

You have seen other modules such as the `math` module already. Now
let's look at another one called `os`, which helps us find
information about directories and files held by our machines
operating system (thus the name os for this module).

These commands may be helpful when we begin exploring how we can
open files in directories on our file system and read them line by
line, which you will be doing in the next section.

Here are the list of `os` module commands we will be using:


        =======================     ===================================================
        `os method`                  What is does
        =======================     ===================================================
        `os.getcwd()`               returns as a string the current working directory
                                    for python
        `os.chdir(path)`            Takes a string that represents a directory
                                    (folder),and changes to that directory
        `os.listdir(path)`          Takes a path string and returns a list of the
                                    names of the folders and files at that path

        `os.path.abspath(file)`     Given a filename string, return the
                                    absolute path of the file
        `os.path.exists(path)`      Takes a path or file string and checks if
                                    it exists
        `os.path.isdir(path)`       Takes a path or file string and checks if
                                    it is a directory
        `os.path.isfile(path)`      Takes a path or file string and checks if
                                    it is a file
        =======================     ===================================================

        `os module methods to get started:` .. note:: that os.path methods may not work on PCs(pictures)


Do this in the Python shell of Wing: Using the commands in
table pictures, figure out where Wing IDE starts, by default.
Here's What happened when I did this on my machine:

.. sourcecode:: python

    >>> import os
    >>> os.getcwd()
    '/Users/shoop'


Next, change to the folder/directory where you have saved the
python code file and text files for today and verify that the Wing
Python shell can see that file. This will require you you to know
the path to your directory.

Working with files
------------------

There are special built-in functions and methods for reading (and
writing) to files. The ones you will use first are given in
table filefuncs

        ===================    =================================================
        `function/method`      What is does
        ===================    =================================================
        `open()`               opens a file for reading or writing,
                               returns a 'file handle'

        `handle.read()`        returns a long string of all text that was in the
                               file that the file handle contains.

        `handle.readline()`    returns next line of text that was in the
                               file that the file handle contains.
        ===================    =================================================

    `Built-in file functions to get you started.(filefuncs)`


An Example, also adding Exceptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a function that uses exceptions to avoid crashing when
something goes wrong. It also illustrates the use of the `
tt open` function and the `read` method. Note below that the open
method takes two arguments: a path to a filename, and a character,
which can be either a 'r' for read, or a 'w' for write. We wil
explore reading files for the moment.

.. sourcecode:: python

    def countChars(filename):
        try:
            inFile = open(filename, 'r')
        except:
            print "File could not be opened, quitting!"
            return

        try:
            text = inFile.read()
        except:
            print "Problem reading the file, quitting!"
            return

        inFile.close()
        size = len(text)
        return size



How does the behavior of this function differ from a function that
doesn't catch the exceptions, if you pass in a filename that
doesn't exist?

Letter Frequency
----------------

We're going to work our way by analyzing texts based on the words
within them, but
we're going to start with letters, rather than words.

Create a program whose main function is `letterFreq`. It should
take a filename as input, and should read the text from the file.
We want this program to determine how many times each alphabetic
character occurs in the text, and build a table containing that
frequency information. We will use a dictionary that has the
alphabetic characters as its keys, and the value associated with
each character is the number of times that the character occurs in
the file.

Suppose the text file contained the following:

    Peter Piper picked a peck of pickled peppers.


The table below shows the frequency count for this text:

    === === === === === === === === === === === === ===
      p   e   t   r   i   c   k   d   a   o   f   l   s
    === === === === === === === === === === === === ===
      9   8   1   3   3   3   3   2   1   1   1   1   1
    === === === === === === === === === === === === ===


Try this:
^^^^^^^^^

Work through the following steps to develop this function:


#. Define the function `letterFreq` so that it takes a string, a
   filename, as its input. For the first step, see if you can open the
   file for reading, and read in all the text from the file. You can
   just print the whole thing to the screen if you like (practice on
   small files like `alice.txt`).

#. Next, figure out how to use a `for` loop (or loops) to iterate
   through all the characters that were in the file. Use the string
   methods `lower` and `isalpha` to convert the characters to lower
   case, and to check if the character is an alphabetic character. You
   might try only printing alphabetic characters to the screen, to
   check if you have this right.

#. Before the loop, add in a line to define the frequency
   dictionary, which will be initially empty: ``freq = {}``.

#. Now we add count data to the dictionary. If a given character is
   not alphabetic, then the program should skip it. If it is
   alphabetic, then it should check to see if it is already in the
   dictionary. You can do this by asking: ``c in freq``. If it is,
   then update the value in the dictionary by adding one to the old
   value. If the character is not in the dictionary, then add it to
   the dictionary with an initial value of one.

#. After the loops end, return the dictionary!

*Challenge:* Write a function that figures out the most
frequently-occurring letter in the file, given the dictionary from
the problem above.

Word Frequency
--------------

Try this:
^^^^^^^^^

Change your program from the last section so that it works on words
in the text, rather than letters. You must change the dictionary,
so that its keys are word strings, rather than letter strings. The
hardest part of this is separating words from punctuation: look at
the `split` and `strip` string methods for help with this.

As an example to see how these work, first try running this Python
code from in a file in Wing:

.. sourcecode:: python

        text = 'one fish, two fish, red fish, blue fish'
        words = text.split()
        for word in words:
            print word

.. activecode:: act_text



.. codelens:: act_text1

        text = 'one fish, two fish, red fish, blue fish'
        words = text.split()
        for word in words:
            print word


Then try changing it like this:

.. sourcecode:: python

        import string

        text = 'one fish, two fish, red fish, blue fish'
        words =text.split()
        for word in words:
            print word.strip(string.punctuation) #remove punctuation

Now try changing your counting code so that it uses the dictionary
to hold words and their frequencies, rather than letters. Have your
function return the dictionary. Try it on a short file that you
make yourself so that you know what the result should be. Then try
it on various text files- the zip archive of files that we've
provided contains some books that are available in the public
domain:

macbeth.txt

mobydick.txt

emma.txt

Try to find how often certain words occur by asking for the counts
from the dictionary that your `wordCount` function returns. You
could print the whole dictionary for these files, but it will be
large.

Single Word Occurrences
------------------------

Write a function `search` that takes a filepath and word as a
parameters and returns a count of how many times that word occurs
in the file.

More Challenges
---------------

*Challenge:* Write a function that figures out the most
frequently-occurring word in the file, given one of the above
files.

*Challenge activity for os module:* If you have time, try writing a
program that takes in a file name and searches the current
directory tree, starting in the current directory, to see if it can
find a file of that name. If it finds it, it should return its full
path. If it doesn't, it should return False.

