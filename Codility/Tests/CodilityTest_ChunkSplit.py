__author__ = 'RobertaBtt'

import functools

import math

"""You have String S consisting of 'a' and 'b'. You want to split it 
into 3 separate non-empty parts.
The lengths of the parts can differ from one another.

In how many ways can you split S into 3 parts, 
such that each part contains the same number of letters 'a' ?

Return the number of possible ways
of splitting S as described above.
"""

def triangularNumber(n):
    return (n * (n + 1)) / 2

def solution(S):

    lenS = len(S)
    positions = []
    for k,s in enumerate(S):
        if s == 'a':
            positions.append(k)

    total_count_a = len(positions)

    # Corner Case: not enought a to split in a omogeneus way
    if total_count_a%3 !=0:
        return 0

    # Corner Case: not 'a' at all
    if total_count_a == 0:
        return ((lenS-1) * (lenS-2)) // 2

    # General
    # Number of 'a' in each substring
    letter_a_for_chunk = total_count_a // 3

    #Init the chunks
    first_cut, second_cut = 0,0

    # Traversing from the beginning
    count=0
    for i in range(lenS):

        # Incrementing the count
        # if the element is '0'
        if S[i] == 'a':
            count += 1

        if(count == letter_a_for_chunk):
            first_cut +=1

        # Incrementing the ways for the
        # 2nd cut if count is equal to
        # 2*(zeros required in each substring)
        elif (count == 2 * letter_a_for_chunk):
            second_cut += 1

    return first_cut * second_cut
    #
    # intervals = S.split('a')
    # if (len(intervals) % 3 !=1):
    #     return 0
    #
    # splitPoint = (len(intervals) - 1) / 3;
    # pass


print(solution('bbbbb'))
print(solution('babaa'))
print(solution('ababa'))