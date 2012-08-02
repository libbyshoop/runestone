Debugging from Chapter 1
========================
What is Debugging?
------------------

Programming is a complex process, and because it is done by human beings, it
often leads to errors. Programming errors are called **bugs** and the process
of tracking them down and correcting them is called **debugging**.  Some claim
that in 1945, a dead moth caused a problem on relay number 70, panel F, of one
of the first computers at Harvard, and the term **bug** has remained in use
since. For more about this historic event, see `first bug <http://en.wikipedia.org/wiki/File:H96566k.jpg>`__.

Three kinds of errors can occur in a program: `syntax errors
<http://en.wikipedia.org/wiki/Syntax_error>`__, `runtime errors
<http://en.wikipedia.org/wiki/Runtime_error>`__, and `semantic errors
<http://en.wikipedia.org/wiki/Logic_error>`__.  It is useful to distinguish
between them in order to track them down more quickly.

**Check your understanding**

.. mchoicemf:: question1_5_1
   :answer_a: Tracking down programming errors and correcting them.
   :answer_b: Removing all the bugs from your house.
   :answer_c: Finding all the bugs in the program.
   :answer_d: Fixing the bugs in the program.
   :correct: a
   :feedback_a: Programming errors are called bugs and the process of finding and removing them from a program is called debugging.
   :feedback_b: Maybe, but that is not what we are talking about in this context.
   :feedback_c: This is partially correct.  Debugging is more than just finding the bugs.
   :feedback_d: This is partially correct.  Debugging is more than just fixing the bugs. What do you need to do before you can fix them?

   Debugging is:

.. index:: syntax, syntax error

Syntax errors
-------------

Python can only execute a program if the program is syntactically correct;
otherwise, the process fails and returns an error message.  **Syntax** refers
to the structure of a program and the rules about that structure. For example,
in English, a sentence must begin with a capital letter and end with a period.
this sentence contains a **syntax error**. So does this one

For most readers, a few syntax errors are not a significant problem, which is
why we can read the poetry of e. e. cummings without problems.
Python is not so forgiving. If there is a single syntax error anywhere in your
program, Python will display an error message and quit, and you will not be able
to run your program. During the first few weeks of your programming career, you
will probably spend a lot of time tracking down syntax errors. As you gain
experience, though, you will make fewer errors and find them faster.


**Check your understanding**

.. mchoicemf:: question1_6_1
   :answer_a: Attempting to divide by 0
   :answer_b: Forgetting a colon at the end of a statement where one is required
   :answer_c: Forgetting to divide by 100 when printing a percentage amount.
   :correct: b
   :feedback_a: A syntax error is an error in the structure of the python code that can be detected before the program is executed.   Python cannot usually tell if you are trying to divide by 0 until it is executing your program (e.g., you might be asking the user for a value and then dividing by that value—you cannot know what value the user will enter before you run the program).
   :feedback_b: This is a problem with the formal structure of the program.  Python knows where colons are required and can detect when one is missing simply by looking at the code without running it.
   :feedback_c: This will produce the wrong answer, but Python will not consider it an error at all.  The programmer is the one who understands that the answer produced is wrong.

   Which of the following is a syntax error?


.. mchoicemf:: question1_6_2
   :answer_a: Programmer
   :answer_b: Compiler / Interpreter
   :answer_c: Computer
   :answer_d: Teacher / Instructor
   :correct: b
   :feedback_a: Programmers rarely find all the syntax errors, we have a program that will do it for us.
   :feedback_b: The compiler and / or interpreter is a computer program that determines if your program is written in a way that can be translated into machine language for execution.
   :feedback_c:  Okay, sort of.  But it is a special thing in the computer that does it.  The stand alone computer without this additional piece can not do it.
   :feedback_d: Maybe.  Your teacher and instructor may be able to find most of your syntax errors, but only because they have experience looking at code and possibly writing code.  With experience syntax errors are easier to find.  But we also have an automated way of finding these types of errors.


   Who or what typically finds syntax errors?

.. index:: runtime error, exception, safe language

Runtime Errors
--------------

The second type of error is a runtime error, so called because the error does
not appear until you run the program. These errors are also called
**exceptions** because they usually indicate that something exceptional (and
bad) has happened.

Runtime errors are rare in the simple programs you will see in the first few
chapters, so it might be a while before you encounter one.

**Check your understanding**

.. mchoicemf:: question1_7_1
   :answer_a: Attempting to divide by 0
   :answer_b: Forgetting a colon at the end of a statement where one is required
   :answer_c: Forgetting to divide by 100 when printing a percentage amount.
   :correct: a
   :feedback_a: Python cannot reliably tell if you are trying to divide by 0 until it is executing your program (e.g., you might be asking the user for a value and then dividing by that value—you cannot know what value the user will enter before you run the program).
   :feedback_b: This is a problem with the formal structure of the program.  Python knows where colons are required and can detect when one is missing simply by looking at the code without running it.
   :feedback_c: This will produce the wrong answer, but Python will not consider it an error at all.  The programmer is the one who understands that the answer produced is wrong.

   Which of the following is a run-time error?

.. index:: semantics, semantic error

Semantic Errors
---------------

The third type of error is the **semantic error**. If there is a semantic error
in your program, it will run successfully, in the sense that the computer will
not generate any error messages, but it will not do the right thing. It will do
something else. Specifically, it will do what you told it to do.

The problem is that the program you wrote is not the program you wanted to
write. The meaning of the program (its semantics) is wrong.  Identifying
semantic errors can be tricky because it requires you to work backward by
looking at the output of the program and trying to figure out what it is doing.

**Check your understanding**

.. mchoicemf:: question1_8_1
   :answer_a: Attempting to divide by 0
   :answer_b: Forgetting a semi-colon at the end of a statement where one is required
   :answer_c: Forgetting to divide by 100 when printing a percentage amount.
   :correct: c
   :feedback_a: A semantic error is an error in logic. The program does not produce the correct output because the problem is not solved correctly. This would be considered a run-time error.
   :feedback_b: A semantic error is an error in logic. The program does not produce the correct output because the problem is not solved correctly. This would be considered a syntax error.
   :feedback_c: This will produce the wrong answer because the programmer implemented the solution incorrectly.

   Which of the following is a semantic error?


.. index::
    single: Holmes, Sherlock
    single: Doyle, Arthur Conan
    single: Linux

Experimental Debugging
----------------------

One of the most important skills you will acquire is debugging.  Although it
can be frustrating, debugging is one of the most intellectually rich,
challenging, and interesting parts of programming.

In some ways, debugging is like detective work. You are confronted with clues,
and you have to infer the processes and events that led to the results you see.

Debugging is also like an experimental science. Once you have an idea what is
going wrong, you modify your program and try again. If your hypothesis was
correct, then you can predict the result of the modification, and you take a
step closer to a working program. If your hypothesis was wrong, you have to
come up with a new one. As Sherlock Holmes pointed out, When you have
eliminated the impossible, whatever remains, however improbable, must be the
truth. (A. Conan Doyle, *The Sign of Four*)

For some people, programming and debugging are the same thing. That is,
programming is the process of gradually debugging a program until it does what
you want. The idea is that you should start with a program that does
*something* and make small modifications, debugging them as you go, so that you
always have a working program.

For example, Linux is an operating system kernel that contains millions of
lines of code, but it started out as a simple program Linus Torvalds used to
explore the Intel 80386 chip. According to Larry Greenfield, one of Linus's
earlier projects was a program that would switch between displaying AAAA and
BBBB. This later evolved to Linux (*The Linux Users' Guide* Beta Version 1).

Later chapters will make more suggestions about debugging and other programming
practices.

**Check your understanding**

.. mchoicemf:: question1_9_1
   :answer_a: Programming is the process of gradually debugging a program until it does what you want.
   :answer_b: Programming is creative and debugging is routine.
   :answer_c: Programming is fun and debugging is work.
   :answer_d: There is no difference between them.
   :correct: a
   :feedback_a: Programming is the writing of the source code and debugging is the process of finding and correcting all the errors within the program until it is correct.
   :feedback_b: Programming can be creative but it also follows a process and debugging can be creative in how you find the errors.
   :feedback_c: Some people think that debugging is actually more fun than programming (they usually become good software testers).  Debugging is much like solving puzzles, which some people think is fun!
   :feedback_d: You cannot debug without first having a program, meaning that someone had to do the programming first.

   The difference between programming and debugging is:

.. index:: formal language, natural language, parse, token


