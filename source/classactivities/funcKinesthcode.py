import math

# Takes in the number of guests, and prints out three
# different options for table sizes
def partyOptions(guests):
    tables4 = calcNumTables(guests, 4)
    print "You would need", tables4, "tables for 4"
    tables8 = calcNumTables(guests, 8)
    print "You would need", tables8, "tables for 8"
    tables10 = calcNumTables(guests, 10)
    print "You would need", tables10, "tables for 10"


def calcNumTables(guests, tableSize):
    # Number of tables is number of guests divided by guests per table
    estTables = guests / float(tableSize)
    # that may be a real number, so round UP
    tables = math.ceil(estTables)
    # return it as an integer
    return tables
    
