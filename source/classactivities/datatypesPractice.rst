Datatypes Practice
===================

**COMP 123**

Overview
--------

Now that you have seen lists and dictionaries, and learned about
operators, functions, and methods on lists, strings, and
dictionaries, it's time to put those ideas into practice.

This activity will ask you to write a series of functions that
operate on strings, lists and dictionaries. This will let you
practice the operations you have seen in the reading.

Functions to Try
----------------


#. Define a function *shout* that has one input parameter, that
   will be a string. The function should create a new string that is
   the same as the input string, but with all letters in uppercase.
   See examples below.

   .. sourcecode:: python

       >>> newS = shout("What are you doing?")
       >>> newS
       WHAT ARE YOU DOING?
       >>> shout("i saw a frog in my bathtub")
       I SAW A FROG IN MY BATHTUB

   .. actex:: act_practice_1

#. Define a function *occursIn* that has two input parameters. When
   called, *occursIn* will be passed two strings, a single word, and a
   piece of text. The function should return *True* if the word
   appears in the string, as a whole word, not as a part of a larger
   word. Use a string method to break the text into words before
   looking for the input word. See examples below.

   .. sourcecode:: python

       >>> occursIn("car", "cardboard box")
       False
       >>> occursIn('box','cardboard box')
       True
       >>> occursIn('car', 'boxcar and train car')
       True

   .. actex:: act_practice_2


#. Define a function *between* that has three parameter variables.
   The first variable will be assigned a list, and the second two
   variables will be assigned values that appear in the list. The
   function should determine the location of the two values in the
   list, and should extract and return the sublist that starts with
   the first value and includes everything up to the second value. If
   either value does not exist in the list, or if the second value
   does not come after the first value, then the function should
   return an empty list: {[]} See the examples below.

   .. sourcecode:: python

       >>> between(['f', 'r', 'o', 'g', 'm', 'a', 'n'], 'o', 'a')
       ['o','g', 'm', 'a']
       >>> between([5, 21, 37, 58, 70, 92], 58, 92)
       [58,70, 92]
       >>> between([6, 2, 15, 12, 3], 15, 6)
       []
       >>> between([6, 2,15, 12, 3], 6, 15)
       [6, 2, 15]

   .. actex:: act_practice_3

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

   .. actex:: act_practice_4


Challenge Functions
-------------------

In case some of you are looking for a harder challenge...


#. Define a function *nameSubst* that takes two inputs. The first
   input is a name, and the second input is a piece of text. The
   function should look for an occurrence of the special string
   *'XXX'* in the text, and it should build a new string that has
   substituted the input name for *'XXX'* in the text. It should
   return this new string.

   .. actex:: act_practice_5

#. Many stores and restaurants ask you to take a number when you
   enter, and then they serve people according to number to ensure
   fairness. You want to write a program so that stores can ask
   customers for a name when they enter the store, and call people by
   name. You will use a list to keep track of the order customers
   entered the store. Write a series of functions to help with this
   program:


   #. Define a function *addCustomer* that takes the list of customers
      and a new customer as its inputs. It should add the new customer's
      name to the end of the list.

   #. Define a function *serveNext* that takes the list of customers
      as its input. If there are no customers waiting, it should return
      the string {'No customers'}. If there are customers in the list, it
      should remove the front customer from the list, and return the
      string.

   #. Define a function *tooManyWaiting* that takes the list of
      customers and a number as its input. If the length of the customer
      list is greater than the input number, then it should return the
      *True*, otherwise it should return *False*.

   #. Define a function *howManyAhead* that takes the list of
      customers and a name as its input. The name should be one that
      appears in the list. The function should determine the location of
      the name in the list, and calculate how many customers are ahead of
      this one in line. It should return the number ahead of this
      customer.

   .. sourcecode:: python

       >>> customers = []
       >>> addCustomer(customers, 'Suzy')
       >>> howManyAhead('Suzy')
       0
       >>> addCustomer(customers, "Frank")
       >>> addCustomer(customers, 'Raja')
       >>> serveNext(customers)
       'Suzy'
       >>> tooManyWaiting(customers, 2)
       False
       >>> addCustomer(customers,'Tigger')
       >>> howManyAhead(customers, 'Raja')
       1
       >>> tooManyWaiting(customers, 2)
       True

   .. actex:: act_practice_6

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

   .. actex:: act_practice_7