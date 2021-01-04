#Given two string, write a method to decide
#if one us a permutation of the other

#Solution1: Sort the String
# We compare the characters from two permutations in the same order

#Case insensitive
def isPermutation(stringA, stringB):

    lenA = len(stringA)
    lenB = len(stringB)
    if lenA != lenB:
        return False

    A = ''.join(sorted(str.upper(stringA)))
    B = ''.join(sorted(str.upper(stringB)))
    return A == B

stringA= "dog"
stringB= "odg"
print(isPermutation(stringA, stringB))


stringA= "ciao"
stringB= "Ciao"
print(isPermutation(stringA, stringB))