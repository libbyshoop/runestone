Strings, Lists
===============

**COMP 123**

Overview
--------

Here we will learn about the basic operations you can use on
strings and lists. You will learn how to create
them, and operators, functions, and methods for each type.

Note that there is another data type in Python, called a "tuple,"
that is similar to a list. We're not going to spend much time on it
for now. A tuple is made by putting multiple values together,
separated by commas, but *not* inside square brackets. Often, we
put the values inside parentheses.

String basics
-------------

At one level, strings are just pieces of text you can use in a
program. They are useful for printing messages to the screen, and
for allowing a user to work with your program more easily. At
another level, however, strings are a collection data type. That
means a string is made up of smaller pieces of data packaged
together. The smaller pieces are called characters, which represent
single keys you could type on a keyboard. Strings, lists, and
tuples are all "sequence" types, which means that some of the same
operations act in the same ways on them.

Strings in Python are text, surrounded by either quotation marks or
single-quotes (apostrophes). There is a special kind of string
surrounded by three quotation marks. This is called a "docstring,"
and may be more than one line long.

Characters and the ASCII table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Python, characters are represented as strings of length 1. But
characters are actually one of the most basic data types a computer
has. Remember that way down deep, all a computer understands is 1
or 0, or sequences of 1s and 0s. From sequences of 1s and 0s,
computers have circuitry that can represent integers, and do basic
arithmetic with them. In order to represent characters in the
computer, we need to have a way to represent them as integer
numbers. Think of it as an encoding, much like Morse code encodes
characters and words using dots, dashes, and spaces. Note that this
representation has nothing to do with type face, font, sizing,
emphasis, all of which are encoded separately from the identity of
the character itself.

Below, in table ascii, is a version of the ASCII table. This is a
mapping from integers to characters on a keyboard. This was a
standard adopted by the entire computing community, so that data
files stored on one kind of computer could be transmitted and read
on another kind of computer. It maps 128 characters onto the
numbers from 0 to 127. The characters that appear in parentheses
are either "whitespace" (characters like space, return, tab) or
"control" characters, things you don't normally see but that you
can access using the control or alt keys on your keyboard.

          +------------------+--------------+--------------+------------------+
          | Char   Num       | Char  Num    | Char      Num| Char     Num     |
          +==================+==============+==============+==================+
          | ``(null)``     0 | ``(sp)``  32 | ``@``      64| `````          96|
          +------------------+--------------+--------------+------------------+
          |  ``(soh)``     1 | ``!``   33   |``A``      65 | ``a``       97   |
          +------------------+--------------+--------------+------------------+
          |  ``(stx)``      2| ``"``  34    | ``B``     66 | ``b``      98    |
          +------------------+--------------+--------------+------------------+
          |  ``(etx)``      3| ``#``   35   | ``C``     67 | ``c``      99    |
          +------------------+--------------+--------------+------------------+
          |  ``(eot)``      4| ``$``   36   | ``D``     68 | ``d``      100   |
          +------------------+--------------+--------------+------------------+
          |  ``(enq)``      5| ``%``   37   | ``E``     69 | ``e``      101   |
          +------------------+--------------+--------------+------------------+
          |  ``(ack)``      6| ``&``   38   | ``F``     70 | ``f``      102   |
          +------------------+--------------+--------------+------------------+
          |  ``(bel)``      7| ``'``   39   | ``G``     71 | ``g``       103  |
          +------------------+--------------+--------------+------------------+
          |  ``(bs)``       8| ``(``   40   | ``H``     72 | ``h``       104  |
          +------------------+--------------+--------------+------------------+
          |  ``(ht)``       9| ``)``   41   |``I``      73 | ``i``      105   |
          +------------------+--------------+--------------+------------------+
          |  ``(nl)``      10| ``*``   42   | ``J``     74 | ``j``      106   |
          +------------------+--------------+--------------+------------------+
          |  ``(vt)``      11| ``+``   43   | ``K``     75 | ``k``       107  |
          +------------------+--------------+--------------+------------------+
          |  ``(np)``      12|  ``,``   44  |  ``L``     76| ``l``       108  |
          +------------------+--------------+--------------+------------------+
          |  ``(cr)``      13|  ``-``   45  |``M``      77 |``m``      109    |
          +------------------+--------------+--------------+------------------+
          |  ``(so)``      14|  ``.``    46 |``N``      78 | ``n``    110     |
          +------------------+--------------+--------------+------------------+
          |  ``(si)``      15| ``/``    47  |``O``      79 | ``o``       111  |
          +------------------+--------------+--------------+------------------+
          |  ``(dle)``     16|  ``0``    48 |``P``      80 |``p``        112  |
          +------------------+--------------+--------------+------------------+
          |  ``(dc1)``     17| ``1``     49 |``Q``      81 | ``q``      113   |
          +------------------+--------------+--------------+------------------+
          |  ``(dc2)``     18| ``2``     50 | ``R``      82| ``r``      114   |
          +------------------+--------------+--------------+------------------+
          |  ``(dc3)``     19| ``3``     51 | ``S``     83 | ``s``      115   |
          +------------------+--------------+--------------+------------------+
          |  ``(dc4)``     20| ``4``     52 | ``T``     84 | ``t``   116      |
          +------------------+--------------+--------------+------------------+
          |  ``(nak)``     21| ``5``     53 | ``U``     85 | ``u``   117      |
          +------------------+--------------+--------------+------------------+
          |  ``(syn)``     22| ``6``     54 | ``V``    86  | ``v``   118      |
          +------------------+--------------+--------------+------------------+
          |  ``(etb)``     23| ``7``     55 | ``W``    87  | ``w``   119      |
          +------------------+--------------+--------------+------------------+
          |  ``(can)``     24| ``8``     56 | ``X``     88 | ``x``   120      |
          +------------------+--------------+--------------+------------------+
          |  ``(em)``      25| ``9``   57   |``Y``      89 | ``y``   121      |
          +------------------+--------------+--------------+------------------+
          |  ``(sub)``     26| ``:``   58   |``Z``      90 | ``z``   122      |
          +------------------+--------------+--------------+------------------+
          |  ``(esc)``     27| ``;``    59  |``[``     91  | ``{``   123      |
          +------------------+--------------+--------------+------------------+
          |  ``(fs)``      28| ``<``   60   |``\``     92  | ``|``   124      |
          +------------------+--------------+--------------+------------------+
          |  ``(gs)``      29| ``=``   61   |``]``     93  | ``}``   125      |
          +------------------+--------------+--------------+------------------+
          |  ``(rs)``      30| ``>``   62   |``^``     94  | ``~``   126      |
          +------------------+--------------+--------------+------------------+
          |  ``(us)``      31| ``?``   63   |``_``      95 | ``(del)`` 127    |
          +------------------+--------------+--------------+------------------+


    * The ASCII table with the character described on the left, and the corresponding integer that represents it on the right (ascii)



The built-in functions *ord* and *chr* are used to convert between
ASCII characters and the numbers used to encode them. Try the
following.

.. sourcecode:: python

     chr(66)
     chr(100)
     chr(126)
     ord('8')
     ord('Y')
     ord('?')

.. actex:: act_datatypes_1

     print(chr(66))
     # Try the remaining.



Modern keyboards provide more many more control keys than the
original ASCII table was designed for. There is an extended ASCII
table that includes more characters, and another encoding system
called Unicode is much larger, and is able to encode many other
writing systems, such as Greek, Cyrillic, Japanese, and Chinese.

Programs that we write are written in plain text, using ASCII
characters. When you interact with Python, you are also typing in
ASCII characters. Other kinds of files, even RTF, contain
additional codes to represent the formatting of the text, and
aren't "plain" text. Strings in Python are collections of ASCII
characters.

Accessing the characters in a string
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use chapter 8 in Downey as a reference for string operations.

Each character in a string has a position. Python, like most
computer languages, starts counting at zero (I can explain why, if
you like). So the first character in string ``"Wanda Fishman"``,
the W, is at position zero.

To access a single character, we use square brackets, and put the
position of the character in the brackets (see below). To find out
the length of the string, we use the *len* function.

Python also provides a notation for use inside the square brackets,
for selecting sections of a string. This is called "slicing." With
slicing, you specify the position to start at, the index one past
the last character you want, and you can choose to also specify a
step size. Try out each of the statements below in the editor to get a sense for
how it works.

.. sourcecode:: python

    str1 = "throckmorton"
    print str1[5]
    print str1[2:6]
    print str1[2:]
    print str1[:6]
    print str1[2:10:3]
    print str1[2::3]
    print str1[:]
    len(str1)
    len(str1[2:6])

.. actex:: act_datatypes_2


One thing Downey doesn't mention is the use of negative indices.
Try *str1[-2]* and other negative numbers. How do negative indices
work? What is the value of *str1[5:1:-1]*?

Asking questions about strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You've already seen that we can compare strings using the
double-equals operator: ``str1 == "throck"``. What happens if you
use operators like ``<`` on strings?

There is a membership operator for strings, that lets us ask
whether a character or string appears in another string:

.. sourcecode:: python

    str1="throck"
    'a' in str1
    'x' in 'alexis'
    'foo' in 'afoodable'

.. actex:: act_datatypes_3

   str1="throck"
   print('a' in str1)
   print('x' in 'alexis')
   print('foo' in 'afoodable')


Concatenating strings
^^^^^^^^^^^^^^^^^^^^^

Concatenation is when we stick two or more strings together to make
a bigger string. In Python, we use the plus operator to mean
concatenation, when its values are strings. We also make use of the
multiplication operator, given a string and a positive integer, to
concatenate a string with itself. This is useful for creating blank
strings, among other uses. Try out the examples below

.. sourcecode:: python

    s = "HI"
    t = 'BYE'
    s + t + s + t
    s * 3
    '-' * 10

.. actex:: act_datatypes_4

    s = "HI"
    t = 'BYE'
    print(s + t + s + t)
    print(s * 3)
    print('-' * 10)


List basics
-----------

See chapter 10 in Downey for more information about lists.

A list is just a collection of data. It is linear, the data is
order from first to last. It is changeable, you can add or remove
elements, or alter a value in a list. We write lists in Python
using square brackets, with the elements inside separated by
commas.

While often the values of a list are all the same type, they may be
any type. Try the following examples building lists.

.. sourcecode:: python

    lst1 = ['a', 'b', 'g']
    lst2 = [5, -1, 9, 2, 12]
    lst3 = ['Fox','Susan', 'OLRI', 230, 6553]



Operations on lists are *very* similar to operations on strings.
Try the following in the editor.

.. sourcecode:: python

     len(lst1)
     len(lst3)
     lst2[0] lst3[4]
     lst1[1:3]
     lst2[::-1]
     newlst =lst1 + lst2
     newnew = lst2 \* 3
     3 in lst2

.. actex:: act_datatypes_5

    lst1 = ['a', 'b', 'g']
    print(lst1)
    # try the rest



Functions that apply to all sequences
-------------------------------------

You've already seen the ``len`` function, which applies to all
"sequences" (lists, strings, and tuples). Here are a few others to
try out.

.. sourcecode:: python

    max(lst2)
    max(lst1)
    max(["apple", "fish", "dog"])
    max("apple")
    max(3, 5, 2)

    min(lst2)
    min("apple")
    min(5, 1, 2, 8)
    min("hah", "eeh", "blah")
    lst2[0:2] == [5, -1]


.. activecode:: act_datatypes_6


Comparing lists for equality is okay, but using inequalities should
not be done.

Mutating lists
^^^^^^^^^^^^^^

Strings are immutable, meaning that once created, they cannot be
modified. Instead, we have to build a new string if we want
something different. Lists are different, they are mutable. That
means that we can add new values, remove old values, and change
existing values in a list, without rebuilding it.

Removing elements from a list may be done in a number of ways, but
one main option is the ``del`` operator

.. sourcecode:: python

    del lst1[3] # removes the value at position 3



Another way to modify a list is to use the assignment operations.
The most simple assignment sets a single slot in the list to a
single new value. You can also set a slice of a list to be a new
set of values. Slice assignment can also be used to add or remove
values from the list. See below:

.. sourcecode:: python

     lst4 = ['fresh', 'start']
     lst5 = [6, 2, 3, 7]

     lst4[1] = 'flowers'
     lst5[1:3] = [-1, -2]
     lst5[:2] = [9, 8, 7]





Functions and methods
---------------------

In Python, each data value is an "object." Object has a technical
meaning here, as opposed to the normal English meaning. Objects, in
computer science, can contain both information and algorithms, and
are viewed as active entities. The code is organized into
"methods," which we can call to ask the object to do something. You
can think of methods as being special functions that are attached
to the data object itself.

Here is an analogy to clarify the difference between a function and
a method. Imagine that you have a list, and picture it as a happy,
squirming poodle. A function that operates on the lists is like the
dog groomer, or the veterinarian. You hand the dog over to this
person, and the person washes the dog, or checks the dog for
illness, and then hands the dog back to you. In all of this, the
dog is passive (we hope). This is how a function works on a list:
you hand the list to it, it does something to the list, and hands
back the result to you.

Calling a method is different. Calling a method removes the third
party from the equation. When you call an object's method, you are
asking *the object* to do something. This is like giving commands
to the dog: sit, stay, come here.

As the semester goes along, you will learn more about objects. For
now, just remember that strings and lists have methods that you can
call to do additional things with them.

When you call a method, you use a slightly different syntax than
when calling a function. It is the same kind of notation you use
when calling a function that belongs to a module you've imported.
You first put the object, typically the name of the variable
holding the object, and then a period. After that the syntax is the
same as a function call: you give the method's name, and then the
arguments to the method in parentheses. For example:
*object.methodname(arguments)*.

You will see concrete examples below.

String methods
^^^^^^^^^^^^^^

Go to {http://docs.python.org/lib/string-methods.html}, the Python
documentation for string methods, and you will see a long list of
methods that operate on strings. These methods allow you to do a
great many things to strings.

Since strings are immutable, many of these methods build new
strings. Below are a few of my favorite string methods; try them
out in the editor.

.. sourcecode:: python

    sentence = "The quick brown fox jumps over the lazy dog."
    sentence.lower() # return a copy all in lowercase
    sentence.upper() # similar, but all in uppercase
    sentence.split() # make sub strings splitting at whitespace
    sentence.strip('.!?,;') # remove leading and following matching chars

.. actex:: act_datatypes_8

    sentence = "The quick brown fox jumps over the lazy dog."
    print(sentence.lower()) # return a copy all in lowercase
    print(sentence.upper()) # similar, but all in uppercase
    print(sentence.split()) # make sub strings splitting at whitespace
    print(sentence.strip('.!?,;')) # remove leading and following matching chars



List methods
^^^^^^^^^^^^

Lists are mutable, which means you can change their values without
building a new list. This means there are a bunch of different
methods for lists that strings and don't support.

Besides using the split notation, several methods add values to a
list. You can also remove values from a list with a method. Try out
the examples below to see their effects.

.. sourcecode:: python

    lst2.append(15) # add a new value at the end of the list
    lst3.append("Math/CS")
    lst2.extend([51, 2, -10]) # tack whole list at end
    lst1.extend("Hello there")
    lst3.insert(2, "Professor") # add new value before given position
    lst3.pop() # remove first value
    lst1.pop(1) # remove value at given position

.. actex:: act_datatypes_9



Other list methods return the index position of a particular value,
count occurrences, sort the values in a list, or reverse a list.

.. sourcecode:: python

    lst3.index(230) # return position of given value lst1.index('g')
    lst6 = [5, 2, 5, 7, 6, 2, 5]
    lst6.count(5) # count occurrences of argument in list
    lst6.count(2)
    lst6.count(10)
    lst2.sort() # sort the values in the list
    lst3.sort()
    lst1.reverse() # reverse the values in the list

.. actex:: act_datatypes_10





