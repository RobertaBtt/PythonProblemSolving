import itertools
import dateparser
# The function substrings takes a single parameter x,
# which represents the input string for which we want to generate substrings.
#
# The itertools.combinations function is used to generate all possible combinations of indices
# from 0 to len(x)+1 taken 2 at a time.
# This means it will generate pairs of indices (i, j) such that i is less than j.
#
# The range(len(x)+1) generates a sequence of numbers from 0 to the length of the string x, inclusive.
# This represents all the possible starting indices for a substring.
#
# The for loop iterates over the combinations of indices generated by itertools.combinations.
# Each pair of indices (i, j) represents the starting and ending indices for a substring.
#
# Inside the loop, yield is used to create a generator.
# The yield statement returns a substring from index i to index j (excluding j) using slicing notation x[i:j].
#
# When the function is called,
# it doesn't return a list of substrings immediately. Instead, it returns a generator object
# that can be iterated over to get one substring at a time.
# This is memory-efficient because it avoids creating a large list of substrings upfront.


def substrings(x):
    for i, j in itertools.combinations(range(len(x)+1), 2):
        yield x[i:j]


def are_anagrams(s1, s2):
    # the sorted strings are checked
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


x = ["mom"]

for i in substrings(x):
    print(i, end=" ")