Dictionaries
============

Dictionary basics
-----------------

Strings and lists are both collections of data where we access the
data based on its position, or index, in the collection. A
dictionary is a collection of data where we access the data by a
key value, and there is no explicit position associated with any
set of keys and values. Think of a dictionary as a two-column
table, where the first column is a set of keys, and the second
column is a set of associated values. The term "dictionary" is a
metaphor for this kind of table: words and associated meanings.

Any immutable type (number, strings, or tuples, primarily) can be
used as a key value. For example, you could create a real
dictionary where the key values were the words, as strings, and the
value associated with each key was a string containing the word's
definition. Another use might be to organize information about
students by their ID numbers.

Below is a small dictionary storing information about people. Note
that we use curly braces to mark the start and end of a dictionary,
when we create one. The key values are ID numbers of some sort, and
the information is the person's name, as a string. Type in the
definition of ``dict1``, and see what ``dict1`` looks like after each
of the commands that follow. Note that these are the commands that
are similar to list or string functions. The value in the square
brackets must be a key value. Similarly, when asking if a value is
``in`` a dictionary, one can only ask about the key values.

.. sourcecode:: python

     dict1 = {1002: 'Harkness, Maria', 6639: 'Swallowtail, Renata'}
     dict1[5534] = 'Lessner, Jillian' dict1[6565] = 'Maxwell, Terry'
     dict1[1023] = 'Franklin, Donald'
     len(dict1)
     del dict1[6565]
     len(dict1) dict1[1023] = 'Franklin-Smyth, Donald'
     1002 in dict1
     'Harkness, Maria' in dict1



The examples below show how you can use strings and tuples as key
values.

.. sourcecode:: python

    family = {'mother' : 'Margaret', 'father': 'James', 'children' :
    ['Sam', 'Fern']}

    family['mother']
    family['children']
    grid = {(0,0): 55, (1,0): 23,(2,0): 102, (0,1): 101, (1,1): 87, (2,1): 72}
    grid[0,0]
    grid[(1,1)]


.. actex:: act_dict_1


Dictionaries have few functions that operate on them, but many
methods.

Dictionary methods
-------------------

Below is an incomplete listing of the dictionary methods. I've
written them in terms of the dictionary from earlier, so you can
try them out.

First there are methods that extract copies of the data from the
dictionary, and turn them into a list.

.. sourcecode:: python

    dict1.keys() # returns a list of the keys in the dictionary
    dict1.values() # returns a list of the values in the dictionary
    dict1.items() # returns a list of (key, value) tuples



Next, there is a method for retrieving the value associated with a
key. We could just use the square bracket notation from before, but
compare what happens with the last two examples.

.. sourcecode:: python

    dict1.get(1023)
    dict1.get(6639)
    dict1.get(4004) # an example where the key is not in the dictionary
    dict1[4004] # and what happens here when the key is not there?



Other methods allow copying of a dictionary, or removing all its
values at once.

.. sourcecode:: python

    dict2 = dict1.copy()
    dict2.clear()


.. actex:: act_dict_2

Activities to try
-----------------

#. Suppose we define a dictionary like the following, which has
   names as keys, and ages as the associated value (see below for an
   example). Define a function *hadBirthday* that takes two inputs:
   the first one is one of these dictionaries, and the second one is a
   name, as a string. It should look up the value for the input name,
   and change the dictionary so that the person is listed as one year
   older.

   .. sourcecode:: python

       >>> agesDict = {'Mary': 15, 'Franco': 25, 'Yuki': 30, 'Morris': 12}
       >>> hadBirthday(agesDict, 'Morris')
       >>> agesDict {'Morris': 13,'Mary': 15, 'Yuki': 30, 'Franco': 25}
       >>> hadBirthday(agesDict,'Yuki')
       >>> agesDict {'Morris': 13, 'Mary': 15, 'Yuki': 31, 'Franco': 25}
       >>> hadBirthday(agesDict, 'Alonzo')
       >>> agesDict
       {'Morris': 13, 'Mary': 15, 'Yuki': 31, 'Franco': 25}

   .. actex:: act_dict_3

#. Suppose you use a dictionary to organize your books. The
   dictionary key values are: *'wish-list'*, *'owned'*, *'read'*,
   *'read-over-and-over'*. The value for each key is a list containing
   the titles of books in that category (see example below). Define a
   function *nowRead* that takes the dictionary and a book title as
   input. It should remove the book from the *owned* category, if it
   is there, and add it to the *read* category. Define other functions
   for changing a book from one category to another, or write one
   general function that allows any movement between categories, by
   taking in extra inputs that tell what the relevant categories are.

   .. sourcecode:: python

       >>> books = {'wish-list': ["How Things Work", "The Hunger Games"],
       'owned': ["Vehicles", "Godel, Escher, Bach"], 'read': ["Dune",
       "Swizzler", "Eragon"], 'read-over-and-over': ["The Hobbit"]}
       >>>nowRead(books, "Vehicles")
       >>> books['read'] ["Dune", "Swizzler","Eragon", "Vehicles"]

   .. actex:: act_dict_4