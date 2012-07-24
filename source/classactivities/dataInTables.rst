Data In Tables
================

Overview
---------

Earlier, we studied how to read data from text files.

Now we are going to examine common methods for working with data in
tables or spreadsheets. We will start by looking at how to read in
CSV files.

Note that we will limit our exploration to a single table of data,
and fairly simple uses of the data. More advanced techniques for
designing and managing data in multiple tables are part of Comp
302: Intro to Database Management Systems.

`To prepare:` Create a folder for this activity called
`CSVActivity`. Create a folder insde it called `CSVData`. Copy the
files from moodle in the `CSVData` folder there into your folder
called `CSVData`. In your `CSVActivity` folder, place the file
provided on moodle called `readline\_CSV.py`.

Reading tabular data from text files
------------------------------------

Tabular data can be created by many programs, including Excel.
Excel and other spreadsheet programs typically have proprietary
ways of storing the files, and they are often not plain text. There
is an open-source spreadsheet format called CSV: Comma-Separated
Values. This kind of file is stored as plain text, ASCII. In this
format each line of the file represents a row of the table, and
each value within the row is separated from its neighbors by a
comma. String values can be indicated by single or double quotes.

In the a folder called `CSVData` are three different CSV files
created from real data:


-  `oscars.csv` contains information about who won Best Actor or
   Best Actress Oscar awards since the Academy Awards' inception more
   than eighty years ago. The table indicates the gender of the
   winner, which year it was won (and the number of the award
   ceremony, 1 for the first), the actor's name, the movie's name, and
   then some information about the winner: age when winning,
   birthplace, and birth month, day, and year.

-  `airportdata.csv` contains information from a recent year about
   the number of scheduled and actual flights, number of passengers,
   and "revenue-tons" (a measure used in shipping that combines size
   and weight per value) of freight and mail from that airport.

-  `census.csv` contains information from the US census on
   individual demographics and annual salary. This is a long file, I
   have provided a brief sample from it in a separate file.


You can use the Wing IDE program to open these files and look at
them. You might get some odd errors about encoding, but you likely
should be able to ignore them.

You can read data from a CSV file the same way we have been reading
other text. The file of Python code to illustrate this is called
`readline\_CSV.py`. Open this up and examine it.

There are comments in the function `readOscarFile` in
`readline\_CSV.py` that describe what you should do to complete it.
These comments are an example of 'pseudocode' comments that you can
make as you are working through what you need to do to complete a
task.

Do This:
^^^^^^^^
Finish the `readOscarFile` function.

*Challenge*: There is a bit of a problem with this data: some
actors have won Oscars multiple times. How would you change the
dictionary to handle this? Ask Libby if you are unsure.

There is also a Python module that will makes reading these files
even easier.

The CSV module
--------------

Python includes a `csv` module that provides tools for reading and
writing CSV files. Look at the example below.

.. sourcecode:: python

        import csv
        ifile = open('CSVData/oscars.csv', "rU") reader =
        csv.reader(ifile)
        rownum = 0
        for row in reader:
            # Save header row.
            if rownum == 0:
                header = row
            else:
                print row # note each row is automatically a list

            rownum += 1
        ifile.close()



Try this code. What is the data type of the variable reader above?

Try this:
^^^^^^^^^

Work with the above code as a start, and create a function
`avgAge(gender)` that will take one parameter: a character that is
either 'm' or 'f'. If it is 'm', it will `return` the average age
of male oscar-winning actors. If it is 'f', it will `return` the
average age of female oscar-winning actors. *Note*: The data values
are all text strings as they are read from the file- you will need
to convert the ages to ints.

Try this:
^^^^^^^^^

Experiment with the other data files in the `CSVData` folder. Can
you devise an interesting question to ask such as the average age
question that you tried above?

Challenge question:
^^^^^^^^^^^^^^^^^^^

Can you write a function to print the Oscars data in a nice table
format? It should first collect up the keys for one of the row
dictionaries, and print them as a header. Then it should print a
row of dashes, and then print the data from each row of the table.
Figure out how wide each column of the table needs to be.

