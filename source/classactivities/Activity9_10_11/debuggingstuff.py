# This function takes in three numbers and returns them in a list, in order
def orderNums(num1, num2, num3):
    smallest = min(num1, num2, num3)
    biggest = max(num1, num2, num3)
    if num1 == smallest:
        if num2 == biggest:
            return [smallest, num3, biggest]
        else:
            return [smallest, num3, biggest]
    elif num3 == smallest:
        if num1 == biggest:
            return [smallest, num3, biggest]
        else:
            return [smallest, num2, biggest]
    else:
        if num1 == biggest:
            return [smallest, num2, biggest]
        else:
            return [smallest, num1, biggest]

# Test Cases
print orderNums(1, 8, 3)
""" between
       parameters:  
       lst   is  a list of items of any data type
       item1 is an item in the list
       item2 is anothe item in the list
       
       returns:
       a new list of items that occur in the original list from item1
       to item2, inclusive.
       If either of the items does not occur in the list, or they are
       provided in the correct order, then an empty list is returned.
"""
def between(lst, item1, item2):
    for nextitem in lst:
        if nextitem == item1:
            start = item1
            print "debug between: start is: ", start
        if nextitem == item2:
            end = item2
    if (start == -1 or end == -1):
        return []
    else :
        return lst[start:end+1]   

### Test
#print between(['f', 'r', 'o', 'g', 'm', 'a', 'n'], 'r', 'a')

# ----------------------------------------------------
# This function returns the character at position 5
# in its input string.  Note that is the sixth character.
def getChar5(string):
    return string[5]

#test
print getChar5("tiny")


# ----------------------------------------------------
# This function computes the different in areas between
# two circles specified by their radii

#import math

#def areaDiffs(radiusA, radiusB)
    #"""This function takes two real numbers, radii of circles
#and it computes and returns the difference in the areas of the two
#circles"""
    #area1 = circleArea(radiusA)
    #area2 = circleArea(radiusA)
    #return abs(area2 = area1)


#def circleArea(radius):
    #"""This function takes a circle's radius as a real number,
#and returns the area of the circle"""
#return 2 * pi * (radius ** 2)


#print areaDiffs(10, 20)
