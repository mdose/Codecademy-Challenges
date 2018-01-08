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

# -------------------------------------------------------------------
# Define a function called reverse that takes a string textand returns
# that string in reverse. For example: reverse("abcd") should return "dcba".
# You may not use reversed or [::-1] to help you with this.

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

print reverse("Python!")

# -------------------------------------------------------------------
# Define a function called anti_vowel that takes one string, text,
# as input and returns the text with all of the vowels removed.
# For example: anti_vowel("Hey You!") should return "Hy Y!".
# Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.

def anti_vowel(text):
	vowels = set(["a", "e","i","o","u", "A","E","I","O","U"])
	new_text = ""
	for char in text:
 		if char not in vowels:
			new_text = new_text + char
	return new_text

print anti_vowel("hello world")

# -------------------------------------------------------------------
# Define a function scrabble_score that takes a string word as input and
# returns the equivalent scrabble score for that word.
# Assume your input is only one word containing no spaces or punctuation.
# As mentioned, no need to worry about score multipliers!
# Your function should work even if the letters you get are uppercase, lowercase, or a mix.
# Assume that you're only given non-empty strings.

score_dict = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
	score = 0
	for char in word.lower():
		score = score + score_dict[char]
	return score

print scrabble_score("hello")

# -------------------------------------------------------------------
# Write a function called censor that takes two strings, text and word, as input.
# It should return the text with the word you chose replaced with asterisks.
# For example:
#     censor("this hack is wack hack", "hack")
# should return:
#     "this **** is wack ****"
# Assume your input strings won't contain punctuation or upper case letters.
# The number of asterisks you put should correspond to the number of letters
# in the censored word.

def censor(text, word):
	return text.replace(word, "*" * len(word))

print censor("this hack is wack hack", "hack")

# -------------------------------------------------------------------
# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.
# For example: count([1, 2, 1, 1], 1) should return 3
# (because 1 appears 3 times in the list).
# The item you input may be an integer, string, float, or even another list!

def count(sequence, item):
	counter = 0
	for thing in sequence:
		if thing == item:
			counter += 1
	return counter

print count([1,2,1,1], 1)
