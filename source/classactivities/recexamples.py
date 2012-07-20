
# -----------------------------------------
# Example 0 -- factorial, the classic

def fact(n):
    """takes a non-negative integer n and returns n!  It prints a
warning message and returns False if given bad input"""
    if (type(n) != int) or (n < 0):
        print "Bad input!"
        return False
    elif n == 0:
        return 1
    else:
        factNMinus1 = fact(n-1)
        return n * factNMinus1

# Here is a recursive trace of a call to fact(3)
# fact(3)
#   => fact(2)
#       => fact(1)
#           => fact(0)   base case here
#               => 1
#           => n * factNMinus1 = 1 * 1 = 1
#       => n * factNMinus1 = 2 * 1 = 2
#   => n * factNMinus1 = 3 * 2 = 6
# => 6



# -----------------------------------------
# Example 1 -- a simple number recursion

def sumOfEvens(m):
    """takes a non-negative integer m as input, and returns the sum
of the even numbers from zero to m"""
    if m < 0:
        print "ERROR OCCURRED: input", m, "is less than zero"
        return 0
    elif m == 0:
        return 0
    elif m % 2 == 0:  # If the number is even...
        recAns = sumOfEvens(m-2)
        return recAns + m
    else:  # If the number is odd...
        recAns = sumOfEvens(m-1)
        return recAns


# sample calls to sumOfEvens
print "Call to sumOfEvens(7) =", sumOfEvens(7) # ****
print "Call to sumOfEvenss(0) =", sumOfEvens(0)


# -----------------------------------------
# Example 2  -- A recursion that counts upward

def printRange(lowNum, highNum):
    """printRange takes in two numbers, lowNum and highNum, and it prints
the numbers between lowNum and highNum, one per line.  It prints "Done"
at the end.  Note that lowNum and highNum are assumed to be integers,
the behavior is a bit odd with real numbers"""
    if lowNum > highNum:
        print "Done"
    else:
        print lowNum
        printRange(lowNum+1, highNum)

        

# sample calls to printRange
print "printRange(3,5):"
printRange(3, 5)  # ****
print "printRange(1, 100):"
printRange(1, 100)


# -----------------------------------------
# Example 3  -- A recursion that counts the number of
# multiples of n in the range from zero to m

def countMultsOfN(n, m):
    """takes in a positive integer, n, and a positive integer, m,
and counts and returns the number of multiples of n that are in the
range from 0 to m"""
    if m == 0:
        # there are no more multiples of n in an empty range
        return 0
    elif (m % n) == 0:
        # if m is a multiple of n, then count the rest of the range
        # and add one for this value of m
        rest = countMultsOfN(n, m-1)
        return rest + 1
    else:
        # current m is not a multiple of n, the count is just the
        # count for the range from 0 to m-1
        return countMultsOfN(n, m-1)


print "countMultsOfN(3, 25) =", countMultsOfN(3, 25) # ****
print "countMultsOfN(12, 5) =", countMultsOfN(12, 5)
print "countMultsOfN(2, 100) =", countMultsOfN(2, 100)


# -----------------------------------------
# Example 4  multiway recursion

def fib(m):
    """takes an input number, m, which must be >= to zero.
It returns the mth number in the fibonacci sequence.  For our purposes
the zeroth fibonacci number is 0, the one-th fibonacci number
is 1, and every number after that is the sum of the previous two:
m:       0   1   2   3   4   5   6   7 ...
fib(m):  0   1   1   2   3   5   8  18 ..."""
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        prev1 = fib(m-1)
        prev2 = fib(m-2)
        return prev1 + prev2


# sample calls to fib
print "fib(3) =", fib(3)  # ****
print "fib(4) =", fib(4)












