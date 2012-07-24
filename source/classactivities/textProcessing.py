ageList = [3, 17, 65, 22, 41, 18, 82]
tot = 0
sumAges = 0.0
for age in ageList:
    tot = tot + 1 
    sumAges = sumAges + age
avgAge = sumAges/tot

print "Before formatting, the avgAge floating point number prints like this:"
print avgAge

print "After formatting, we can print a nice satement like this:"

templateString = '{0:d} people have an average age of {1:4.2f}'
strToPrint = templateString.format(tot, avgAge)
print strToPrint

"""
formatOut(aDictionary):
  an example of how to format the printing of numbers and text
  in some simple dictionary data.
parameter:
  aDictionary is a dictionary containing names as the 'keys' and
  ages as the data
"""
def formatOut(aDictionary):
    for name in aDictionary:
        templateString = 'Name: {0}\t\t Age: {1:d}'
        printableString = templateString.format(name, aDictionary[name])
        print printableString
#Test        
ages = {'Jenny': 18, 'Tom': 49, 'Nancy': 29, 'Jim': 79, 'Henry':6, 'Grandma':102}
print "\nExample from formatOut:"
formatOut(ages)



"""
formatColumns(aDictionary):
  an example of how to format the printing of numbers and text
  in some simple dictionary data, using a header for the columns.
parameter:
  aDictionary is a dictionary containing names as the 'keys' and
  ages as the data
"""
def formatColumns(aDictionary):
    headerString = 'Name\t\tAge\n====\t\t==='
    print headerString
    for name in aDictionary:
        templateString = '{0}\t\t{1:3d}'
        printableString = templateString.format(name, aDictionary[name])
        print printableString
#Test
ages = {'Jenny': 18, 'Tom': 49, 'Nancy': 29, 'Jim': 79, 'Henry':6, 'Grandma':102}
print "\nExample from formatColumns:"
formatColumns(ages)

"""
If you have a string as data that you would like to format, you might want
to 'justify' it to the left or right.  Here we right justify some names
from a dictionary containng identifiers and names for people.
"""
def formatColumns2(aDictionary):
    headerString = 'Id\t\t\tName\n====\t\t\t===='
    print headerString
    for ident in aDictionary:
        templateString = '{0}\t\t\t{1:>20}'
        printableString = templateString.format(ident, aDictionary[ident])
        print printableString
#Test
names = {1075108:'Laura Jeffrey', 228673:'John Q. Adams', 993750:'Grace Hopper', 77263: 'George Washington'}
print "\nExample from formatColumns2:"
formatColumns2(names)

def longestName(aDictionary):
    longestLen = 0
    longestName = ''
    #you complete this

"""
A final "best" example where we can use the same template to format both the 
header and the data itself.
"""
def formatColumns3(aDictionary):
    #Note:  <10 means use 10 characters total and left justify them
    #       >20 means use 20 characters total and righ justify them
    
    #use this template for header and data
    templateString = '{0:<10}{1:>20}'  

    headerString1 = 'Id'
    headerString2 = 'Name'
    line1 = 9*'-'
    line2 = 20*'-'
    headerString = templateString.format(headerString1,headerString2)
    print headerString
    lineString = templateString.format(line1, line2)
    print lineString
    
    for ident in aDictionary:
        #created template above now and use it here
        printableString = templateString.format(ident, aDictionary[ident])
        print printableString
#Test
names = {1075108:'Laura Jeffrey', 228673:'John Q. Adams', 993750:'Grace Hopper', 77263: 'George Washington'}
print "\nExample from formatColumns3:"
formatColumns3(names)



############################################## File access

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

print 'alice.txt contains', countChars('alice.txt'), 'characters.'