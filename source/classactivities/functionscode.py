""" --------------------------------------------
File:  functionscode.py
Author:  Susan Fox

This file contains the example functions from the in-class
activity on Wednesday, February 11.  Students should add
to this file while working on the example"""

# First example from in-class activity
def foo(x, y, z):
    q = max(x, y)
    r = max(y, z)
    s = max(x, z)
    return min(q, r, s)


# Second example from in-class activity: comparing print and return
def poly1(x):
    return 3 * (x ** 2) - 1

def poly2(x):
    print 3 * (x ** 2)  - 1


# Song example from in-class activity:  functions that call each
# other...

def song(name):
    h()
    h()
    hb()
    d(name)
    h()


def h():
    hb()
    ty()



def hb():
    print "Happy birthday",

def ty():
    print "to you"

def d(n):
    print "dear", n



