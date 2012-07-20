


# here is the first example from the activity

x = 35

def sillyFn(a):       # defining the function 
    b = x - 10 * a
    return b


print sillyFn(-2)     # calling the function, and printing what it returns




# here is the second example from the activity

#these 3 variables are 'global' in this script
a = 6
b = 15
c = 25

def moreSilly(c, d):   #c, d become local to the function
    print a
    print c
    b = 2 * d
    print b

moreSilly(1, 4)
print b


# here is the third example from the activity

def main():
    x = 5
    ans = helper(x, 10)
    print ans

def helper(a, b):
    return 2 * b + a


# here is the fourth example from the activity

# this is a bit ugly, but bear with it
def carpetEstimate(wid1, len1, price1, wid2, len2, price2, wid3, len3, price3):
    area1 = rectArea(wid1, len1)
    cost1 = roomCost(area1, price1)
    area2 = rectArea(wid2, len2)
    cost2 = roomCost(area2, price2)
    area3 = rectArea(wid3, len3)
    cost3 = roomCost(area3, price3)

    print "Room 1"
    print "  Area =", area1
    print "  Cost =", cost1, "dollars"
    print "Room 2"
    print "  Area =", area2
    print "  Cost =", cost2, "dollars"
    print "Room 3"
    print "  Area =", area3
    print "  Cost =", cost3, "dollars"
    print "------------------"
    print "Total cost =", cost1 + cost2 + cost3, "dollars"

