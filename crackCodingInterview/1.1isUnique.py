#Implement an algorithm to determine
#if a string has all unique character without using additional data structure.

def hasUniqueChars(S):
    dictionary_s = {}
    for s in S:
        if s.upper() not in dictionary_s:

            dictionary_s[s.upper()] = 1
        else:
            return False
    return True

print(hasUniqueChars('ghjkoiuytT'))