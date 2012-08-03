


Statements and Expressions
==========================

.. index:: statement

.. video:: expression_vid
    :controls:
    :thumb: ../_static/expressions.png

    http://knuth.luther.edu/~bmiller/thinkcsVideos/Expressions.mov
    http://knuth.luther.edu/~bmiller/thinkcsVideos/Expressions.webm

A **statement** is an instruction that the Python interpreter can execute. We
have only seen the assignment statement so far.  Some other kinds of statements
that we'll see shortly are ``while`` statements, ``for`` statements, ``if``
statements,  and ``import`` statements.  (There are other kinds too!)


.. index:: expression

An **expression** is a combination of values, variables, operators, and calls
to functions. Expressions need to be evaluated.  If you ask Python to ``print`` an expression, the interpreter
**evaluates** the expression and displays the result.

.. activecode:: ch02_13
    :nocanvas:

    print(1 + 1)
    print(len("hello"))


In this example ``len`` is a built-in Python function that returns the number
of characters in a string.  We've previously seen the ``print`` and the
``type`` functions, so this is our third example of a function!

The *evaluation of an expression* produces a value, which is why expressions
can appear on the right hand side of assignment statements. A value all by
itself is a simple expression, and so is a variable.  Evaluating a variable gives the value that the variable refers to.

.. activecode:: ch02_14
    :nocanvas:

    y = 3.14
    x = len("hello")
    print(x)
    print(y)

If we take a look at this same example in the Python shell, we will see one of the distinct differences between statements and expressions.

.. sourcecode:: python

	>>> y = 3.14
	>>> x = len("hello")
	>>> print(x)
	5
	>>> print(y)
	3.14
	>>> y
	3.14
	>>>

Note that when we enter the assignment statement, ``y = 3.14``, only the prompt is returned.  There is no value.  This
is due to the fact that statements, such as the assignment statement, do not return a value.  They are simply executed.

On the other hand, the result of executing the assignment statement is the creation of a reference from a variable, ``y``, to a value, ``3.14``.  When we execute the print function working on ``y``, we see the value that y is referring to.  In fact, evaluating ``y`` by itself results in the same response.


.. index:: operator, operand, expression, integer division

Operators and Operands
----------------------

**Operators** are special tokens that represent computations like addition,
multiplication and division. The values the operator works on are called
**operands**.

The following are all legal Python expressions whose meaning is more or less
clear::

    20 + 32
    hour - 1
    hour * 60 + minute
    minute / 60
    5 ** 2
    (5 + 9) * (15 - 7)

The tokens ``+``, ``-``, and ``*``, and the use of parenthesis for grouping,
mean in Python what they mean in mathematics. The asterisk (``*``) is the
token for multiplication, and ``**`` is the token for exponentiation.
Addition, subtraction, multiplication, and exponentiation all do what you
expect.

.. activecode:: ch02_15
    :nocanvas:

    print(2 + 3)
    print(2 - 3)
    print(2 * 3)
    print(2 ** 3)
    print(3 ** 2)

When a variable name appears in the place of an operand, it is replaced with
the value that it refers to before the operation is performed.
For example, what if we wanted to convert 645 minutes into hours.

.. activecode:: ch02_16
    :nocanvas:

    minutes = 645
    hours = minutes / 60
    print(hours)


In Python 3, the division operator uses the token `/` which always evaluates to a floating point
result.

In the previous example, what we might have wanted to know was how many *whole* hours there
are, and how many minutes remain.  Python gives us two different flavors of
the division operator.  The second, called **integer division**, uses the token
`//`.  It always *truncates* its result down to the next smallest integer (to
the left on the number line).

.. activecode:: ch02_17
    :nocanvas:

    print(7 / 4)
    print(7 // 4)
    minutes = 645
    hours = minutes // 60
    print(hours)


Take care that you choose the correct flavor of the division operator.  If
you're working with expressions where you need floating point values, use the
division operator `/`.  If you want an integer result, use `//`.

.. index:: modulus

The **modulus operator**, sometimes also called the **remainder operator** or **integer remainder operator** works on integers (and integer expressions) and yields
the remainder when the first operand is divided by the second. In Python, the
modulus operator is a percent sign (``%``). The syntax is the same as for other
operators:

.. activecode:: ch02_18
    :nocanvas:

    quotient = 7 // 3     # This is the integer division operator
    print(quotient)
    remainder = 7 % 3
    print(remainder)


So 7 divided by 3 is 2 with a remainder of 1.

The modulus operator turns out to be surprisingly useful. For example, you can
check whether one number is divisible by another---if ``x % y`` is zero, then
``x`` is divisible by ``y``.
Also, you can extract the right-most digit or digits from a number.  For
example, ``x % 10`` yields the right-most digit of ``x`` (in base 10).
Similarly ``x % 100`` yields the last two digits.

Finally, returning to our time example, the remainder operator is extremely useful for doing conversions, say from seconds,
to hours, minutes and seconds.
If we start with a number of seconds, say 7684, the following program uses integer division and remainder to convert to an easier form.  Step through it to be sure you understand how the division and remainder operators are being used to
compute the correct values.

.. codelens:: ch02_19_codelens

    total_secs = 7684
    hours = total_secs // 3600
    secs_still_remaining = total_secs % 3600
    minutes =  secs_still_remaining // 60
    secs_finally_remaining = secs_still_remaining  % 60

    print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

**Check your understanding**

.. mchoicemf:: test_question2_6_1
   :answer_a: 4.5
   :answer_b: 5
   :answer_c: 4
   :answer_d: 2
   :correct: a
   :feedback_a: The / operator does exact division and returns a floating point result.
   :feedback_b: The / operator does exact division and returns a floating point result.
   :feedback_c: The / operator does exact division and returns a floating point result.
   :feedback_d: The / operator does exact division and returns a floating point result.

   What is printed from the following statement?
   <pre>
   print (18 / 4)
   </pre>


.. mchoicemf:: test_question2_6_2
   :answer_a: 4.25
   :answer_b: 5
   :answer_c: 4
   :answer_d: 2
   :correct: c
   :feedback_a: -  The // operator does integer division and returns an integer result
   :feedback_b: - The // operator does integer division and returns an integer result, but it truncates the result of the division.  It does not round.
   :feedback_c: - The // operator does integer division and returns the truncated integer result
   :feedback_d: - The // operator does integer division and returns the result of the division on an integer (not the remainder).

   What is printed from the following statement?
   <pre>
   print (18 // 4)
   </pre>


.. mchoicemf:: test_question2_6_3
   :answer_a: 4.25
   :answer_b: 5
   :answer_c: 4
   :answer_d: 2
   :correct: d
   :feedback_a: The % operator returns the remainder after division.
   :feedback_b: The % operator returns the remainder after division.
   :feedback_c: The % operator returns the remainder after division.
   :feedback_d: The % operator returns the remainder after division.

   What is printed from the following statement?
   <pre>
   print (18 % 4)
   </pre>

.. index:: order of operations, rules of precedence

Order of Operations
-------------------

.. video:: precedencevid
    :controls:
    :thumb: ../_static/precedencethumb.png

    http://knuth.luther.edu/~pythonworks/thinkcsVideos/precedence.mov
    http://knuth.luther.edu/~pythonworks/thinkcsVideos/precedence.webm


.. video:: associativityvid
    :controls:
    :thumb: ../_static/associativitythumb.png

    http://knuth.luther.edu/~pythonworks/thinkcsVideos/associativity.mov
    http://knuth.luther.edu/~pythonworks/thinkcsVideos/associativity.webm



When more than one operator appears in an expression, the order of evaluation
depends on the **rules of precedence**. Python follows the same precedence
rules for its mathematical operators that mathematics does.




.. The acronym PEMDAS
.. is a useful way to remember the order of operations:

#. Parentheses have the highest precedence and can be used to force an
   expression to evaluate in the order you want. Since expressions in
   parentheses are evaluated first, ``2 * (3-1)`` is 4, and ``(1+1)**(5-2)`` is
   8. You can also use parentheses to make an expression easier to read, as in
   ``(minute * 100) / 60``, even though it doesn't change the result.
#. Exponentiation has the next highest precedence, so ``2**1+1`` is 3 and
   not 4, and ``3*1**3`` is 3 and not 27.  Can you explain why?
#. Multiplication and both division operators have the same
   precedence, which is higher than addition and subtraction, which
   also have the same precedence. So ``2*3-1`` yields 5 rather than 4, and
   ``5-2*2`` is 1, not 6.
#. Operators with the *same* precedence are
   evaluated from left-to-right. In algebra we say they are *left-associative*.
   So in the expression ``6-3+2``, the subtraction happens first, yielding 3.
   We then add 2 to get the result 5. If the operations had been evaluated from
   right to left, the result would have been ``6-(3+2)``, which is 1.

.. (The
..   acronym PEDMAS could mislead you to thinking that division has higher
..   precedence than multiplication, and addition is done ahead of subtraction -
..   don't be misled.  Subtraction and addition are at the same precedence, and
..   the left-to-right rule applies.)

.. note::

    Due to some historical quirk, an exception to the left-to-right
    left-associative rule is the exponentiation operator `**`. A useful hint
    is to always use parentheses to force exactly the order you want when
    exponentiation is involved:

    .. activecode:: ch02_23
        :nocanvas:

        print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
        print((2 ** 3) ** 2)   # use parentheses to force the order you want!

.. The immediate mode command prompt of Python is great for exploring and
.. experimenting with expressions like this.

**Check your understanding**

.. mchoicemf:: test_question2_8_1
   :answer_a: 14
   :answer_b: 24
   :answer_c: 3
   :answer_d: 13.667
   :correct: a
   :feedback_a: Using parentheses, the expression is evaluated as (2*5) first, then (10 // 3), then (16-3), and then (13+1).
   :feedback_b: Remember that * has precedence over  -.
   :feedback_c: Remember that // has precedence over -.
   :feedback_d: Remember that // does integer division.

   What is the value of the following expression:
   <pre>
   16 - 2 * 5 // 3 + 1
   </pre>


.. mchoicemf:: test_question2_8_2
   :answer_a: 768
   :answer_b: 128
   :answer_c: 12
   :answer_d: 256
   :correct: a
   :feedback_a: Exponentiation has precedence over multiplication, but its precedence goes from right to left!  So 2 ** 3 is 8, 2 ** 8 is 256 and 256 * 3 is 768.
   :feedback_b: Exponentiation (**) is processed right to left, so take 2 ** 3 first.
   :feedback_c: There are two exponentiations.
   :feedback_d: Remember to multiply by 3.

   What is the value of the following expression:
   <pre>
   2 ** 2 ** 3 * 3
   </pre>

Exercises
---------

1. Evaluate the following numerical expressions in your head, then use
   the active code window to check your results:

    #. ``5 ** 2``
    #. ``9 * 5``
    #. ``15 / 12``
    #. ``12 / 15``
    #. ``15 // 12``
    #. ``12 // 15``
    #. ``5 % 2``
    #. ``9 % 5``
    #. ``15 % 12``
    #. ``12 % 15``
    #. ``6 % 6``
    #. ``0 % 7``

  .. activecode:: ch02_ex1

      print(5**2)

#. Add parenthesis to the expression ``6 * 1 - 2`` to change its value
   from 4 to -6.

   .. actex:: ex_2_6

#. The formula for computing the final amount if one is earning
   compound interest is given on Wikipedia as

   .. image:: Figures/compoundInterest.png
      :alt: formula for compound interest

   Write a Python program that assigns the principal amount of 10000 to
   variable `P`, assign to `n` the value 12, and assign to `r` the interest
   rate of 8% (0.08).  Then have the program prompt the user for the number of years,
   `t`, that the money will be compounded for.  Calculate and print the final
   amount after `t` years.

   .. actex:: ex_2_7