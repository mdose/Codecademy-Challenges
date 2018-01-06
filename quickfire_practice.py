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
