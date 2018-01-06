# return true if a number is even

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False

# -------------------------------------------------------------------
# Define a function is_int that takes a number x as an input.
#
# Have it return True if the number is an integer (as defined above) and False otherwise.
#
# For example:
#
# is_int(7.0)   # True
# is_int(7.5)   # False
# is_int(-1)    # True

import math

def is_int(x):
  if x - math.ceil(x) == 0:
    return True
  else:
    return False

print is_int(7.0)
print is_int(7.5)
print is_int(-1)

# -------------------------------------------------------------------
# Write a function called digit_sum that takes a positive integer n as input
# and returns the sum of all that number's digits.
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
# (Assume that the number you are given will always be positive.)

def digit_sum(n):
  sum = 0

  for num in str(n):
    sum = sum + int(num)
  return sum

print digit_sum(434)

# -------------------------------------------------------------------
# Define a function factorial that takes an integer x as input.
# Calculate and return the factorial of that number.
# factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
# factorial(1) would equal 1.
# factorial(3) would equal 3 * 2 * 1, which is 6.

def factorial(x):
  product = 1
  for num in range (1, x + 1):
    product *= num
  return product

print factorial(4)
print factorial(1)
print factorial(3)

# -------------------------------------------------------------------
# Define a function called is_prime that takes a number x as input.
# If x is a prime number, return True. Otherwise, return False.

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print is_prime(2)
print is_prime(4)
print is_prime(5)
print is_prime(18)
print is_prime(11)
print is_prime(21)
