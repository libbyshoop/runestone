Function Kinesthetic
=====================
**COMP 123**

Overview
---------

Read over the code below, and its translation into English
instructions. Then be prepared to act out the execution of this
program, taking on the role of a Happy Robot.

    .. sourcecode:: python

        import math

        # Takes in the number of guests, and prints out three different options for table sizes
        def partyOptions(numGuests):
            tables4 =calcNumTables(numGuests, 4)
            print "You would need", tables4,"tables for 4"
            tables8 = calcNumTables(numGuests, 8)
            print "You would need", tables8, "tables for 8"
            tables10 = calcNumTables(numGuests, 10)
            print "You would need", tables10,"tables for 10"

        def calcNumTables(guests, tableSize):    # Number of tables is number of guests divided by guests per table
            estTables = guests /float(tableSize) # that may be a real number, so round UP
            tables =math.ceil(estTables)         # return it as an integer return tables
            return tables


partyOptions
------------

You will receive the "ball of control" with an envelope attached.
Stand up. Take out the first piece of paper in the envelope. On
that paper is your function name and your input value: ``numGuests``,
the number of guests for this party. Save that paper.

Take the next, blank, piece of paper from the envelope. Write a
call to the ``calcNumTables`` function. Copy down your ``numGuests``
value, and write down 4 for the second parameter. Put the paper
inside the envelope.

Choose a new "Happy Robot" from the class, and throw the
"ball of control" to that person (gently!). The person must be
someone who is sitting.

Wait, standing, until that person throws the ball back to you.

When you get the ball back, you must use the value returned to you:
get the piece of paper out of the envelope. Go to the whiteboard
and write the following sentences.
