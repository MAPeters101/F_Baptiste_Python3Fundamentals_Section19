'''
Question 1
Write some code that generates a file containing rows containing
the following data:

i, fibonacci_i, factorial_i, gcd_fibonacci_i_factorial_i
where:

i: integer values from 0 to 100
fibonacci_i: the ith Fibonacci number
factorial_i: the factorial of i (i!)
gcd_fib_i_fact_i: the greatest common denominator of the ith Fibonacci number
and i!
Hint: look at the math.factorial and math.gcd functions in the Python docs

Also make sure to include a header row in your file.

For example, the first few rows in your file should contain this data:

i,fib,fact,gcd
0,1,1,1
1,1,1,1
2,2,2,2
3,3,6,3
4,5,24,1
5,8,120,8
Question 2
Using the file you just generated, write three functions:

fib
fact
gcd_fib_fact
that perform the same calculations as our original fib function, the math
module's factorial and the gcd of the corresponding fibonacci and factorial
numbers, but uses the data that was saved in the file as a cache/lookup
mechanism - i.e. just use the numbers in the file if they are available,
otherwise make the calculation.
'''