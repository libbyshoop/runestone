Four Steps for Writing Recursive Functions
===========================================

**COMP 123**


#. **Design the function.**

   Before starting to write any code, or even think through the
   recursive process, you need to be sure you understand what you are
   trying to do. Answer the following questions:


   #. What will you name the function? How many input parameter
      variables should it have? What should their names be? What type of
      data should they be? If there is a value returned, what type should
      it be?

      Write a comment that describes these things, and write the first
      line of the function definition.

      .. sourcecode:: python

          # factorial is a function that takes a single input parameter, n,
          # which should be an integer >= 0. It returns an integer value,
          # the factorial of n: n! = n * n-1 * ... * 2 * 1. 0! = 1, by definition
          def factorial(n):


   #. What is the function supposed to do?

      Write out two or three examples for different inputs, and put those
      calls after the definition, as tests.

      .. sourcecode:: python

          print factorial(3) # should be 6
          print factorial(5) # should be 30
          print factorial(1) # should be 1
          print factorial(0) # should be 0


   #. Think about which input parameter is going to change as the
      program repeats, and which should stay the same. We call this
      parameter (or these parameters if more than one changes) the "loop
      variables."



#. **Determine the *Base Case* input and result.**

   Think about all the possible values the loop variable could take
   on. For which values is the result obvious or easy to calculate?
   This is the *Base Case*.


   #. How could you test the loop variable to see if it is one of
      these really simple cases? Write a boolean expression that performs
      that test.

      .. sourcecode:: python

          def factorial(n):
            if n == 0:


   #. What do you want to do when the loop variable is this simple
      case? Write the code for what to do, to compute the answer or
      produce the right result.

      .. sourcecode:: python

          def factorial(n):
            if n == 0:
                return 1



   To use recursion, you must rephrase the original question in
   terms of a smaller sub-problem of the same kind. In writing a
   recursive function, you then make a leap of faith. You *assume*
   that the function you are writing will work correctly on the
   smaller sub-problem, and build a solution to the full, original
   problem from that. The next two steps take you through this
   process, to create the *Recursive Case*.



#. **Determine the natural recursive sub-problem.**

   Suppose that the loop variables is not one of the simple cases, but
   reflects a larger problem. What could you do to the loop variable
   to make it slightly smaller, and closer to being one of those
   simple cases?

   Add to your program an `else` case that contains a recursive call
   to the procedure, with a value for each input parameter. If the
   parameter is not supposed to change, then simply put the variable
   back in without altering it. But the loop variable should be
   replaced by an expression that simplifies it.

   .. sourcecode:: python

       def factorial(n):
        if n == 0:
            return 1
        else:
            factorial(n-1)




#. **Determine how to modify the sub-problem's result.**

   Apply a bit of faith at this point. Assume that the recursive call
   on the sub-problem does what it is supposed to do. Now, compare what
   the recursion has done for the sub-problem to what the original
   problem needed to do.

   Write expressions and/or statements that add to the result computed
   by the recursive call (for the sub-problem) in order to produce the
   right complete result.

   .. sourcecode:: python

        # factorial is a function that takes a single input parameter, n,
        # which should be an integer >= 0. It returns an integer value,
        # the factorial of n: n! = n * n-1 * ... * 2 * 1. 0! = 1, by definition

        def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

        print factorial(3) # should be 6
        print factorial(5) # should be 30
        print factorial(1) # should be 1
        print factorial(0) # should be 0




