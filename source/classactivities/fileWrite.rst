Writing Data to Files
=====================

Overview
--------

This lab will explore the commands for reading data from files and
writing data to files. We will then use these commands to play
around with data in the form of words stored in a file.

File reading and writing
------------------------

We have stored programs in files, and learned how to load them into
Python's interactive shell in Wing. We have learned the normal
Python commands for reading data from files. We have and will work
primarily with text files, encoded using the ASCII encoding (Google
it if you don't remember what that is). In ASCII, each character is
encoded using 8 bits, one byte. That allows us to represent 256
different characters, which is enough for many languages.

The URL below is a link to the section of the online Python
documentation that talks about reading and writing files.

http://docs.python.org/tutorial/inputoutput.html#reading-and-writing-files

`Opening files for reading and writing is normal python; you do not
need to include any libraries in order to do it, and it should work
in any Python system.`

Recall:
^^^^^^^

To access a file, we ask Python to `open` the file, and we get back
a file object. We then use methods belonging to the file object to
read or write the file.

Reading from a file, processing using split and strip functions, and re module
------------------------------------------------------------------------------

Remember:
^^^^^^^^^

You have been opening and reading files of text, some of which came
from Project Gutenberg. In one activity you have or will read
comma-separated values after opening the files.

.. note::   You may need to specify the whole path to the file, OR
            put the file in the same place as your current code file. It may
            also work to place the file in your 'Documents' directory on your
            own machine, or in the Documents directory of the macalester user
            on the Macs in room 245 and 256. If you are unsure of what we mean
            by the path to the file, please ask (it is specified differently on
            Macs and PCs). You might also want try using the 'os' python module
            to set the directory before you read the file- please see the
            Activity for text processing, which showed you how to do this.

In the examples you have tried, you have been learning to use the
following staples of text processing- make sure that you become
very familiar with how to use them:


-  *split()* function to break up text on whitespace or commas or
   tabs into individual words or phrases

-  *strip()* function to remove characters such as punctuation from
   the front or back of phrases

-  import the *string* module and use `string.punctuation` as a
   string of possible punctuation characters

-  import the *re* module and create patterns using regular
   expression syntax, then match those patterns to text using methods
   such as `re.findall()` and `re.split()`

-  the *format()* method on strings to print results in a readable
   manner


Writing to a file
-----------------

As you may have experienced when counting words on larger text
files, it is often convenient and simply necessary to write the
results of our text and data file processing back out onto files
that we can refer to later and peruse through using a tool
available on our computer. This turns out to be far easier than
printing inside our python code and trying to decipher what is
inside a large dictionary or list.

To write to a file, we open it as before, except we use the code
`'w'` to tell Python we want to write to the file instead of
reading. BE CAREFUL! If the file exists, opening it to write to it
will throw away the old file!! The `write` method takes a string
and writes it to the file. Note that you have to explicitly write
newline characters to break up the lines.

Try this:
^^^^^^^^^

Put the following simple function into the Wing editor and save it
into a file called `textWriteEx.py`. Then add lines to test it out.
As with reading, you will need to use a proper path for the
filename, so that you know where to find the file that has been
written. As mentioned before, you can also use the `os` module
functions to set the path where you want all files to be written.

.. sourcecode:: python

    def writeReps(filename, string, num):
        fileOut = open(filename, 'w')
        for i in range(num):
            fileOut.write(string + '\n')
        fileOut.close()



It is important to remember to close a file when you are done with
it, especially for writing to a file. The computer's operating
system is lazy! When Python says:
"Here, write this data to the file," the OS says,
"Oh, yeah, I'll get to that at some point," and puts it in a
buffer. When the buffer is full, it writes to the file. When you
tell the OS to close the file, then the OS is forced to write the
data, whether the buffer is full or not. If you don't close the
file, and then you quit the program, then the data may never be
written!

Try this:
^^^^^^^^^

Improve your word counting work so far by writing the words and
their counts back out to a file. Remember when we used the `format`
method on strings to print results so that they looked nicely
aligned? Use this now to write well-formatted strings back out to a
file. As we have been doing for some time now, make a separate
function called `writeWordCount` that will take a filename and the
dictionary that held the words and their counts. Check your work by
opening the file you write using Wing or another text editor.

Challenge:
^^^^^^^^^^

Try reading the lines from `ladlerat.txt` and writing the lines in
reverse order to a new file:

`tareldal.txt`.

Challenge section: Word Play
----------------------------

Most of this activity is a "case study." It looks at one
application of reading from a file. It uses a file to store a big
list of words, one word per line. On Moodle you can find the
complete file of legal crossword puzzle words, called
`crosswords.txt`, and a shortened version of it called
`shortcross.txt`. These are in a folder on moodle called TextFiles
from an earlier activity.

If you are interested in exploring other file of words, below is a
link to the web page where you can download some other word files,
Beware- they are fairly large!

http://icon.shef.ac.uk/Moby/

Try this:
^^^^^^^^^

The file `wordplay.py` contains some simple examples that show how
you might read the data from this file. They are examples of
different ways to achieve the same task.

Try out each example to see how they work, then try to do the
following:


-  Define a function `littleWords` that writes all the words of
   length less than three that are in the crosswords file to a new
   file.

-  Define a function `noEs` that makes a list of all the words in
   the file that do not contain the letter e. Then write that list to
   a file.

-  Define a function `noVowels` that makes a list of all the words
   in the file that do not contain any "normal" vowels (a, e, i, o, or
   u). Then write that list to a file.

-  Define a function `firstNZWords` that takes in a number, n, and
   returns a list of the first n words in the list that contain the
   letter z (or Z). Then write that list to a file.



