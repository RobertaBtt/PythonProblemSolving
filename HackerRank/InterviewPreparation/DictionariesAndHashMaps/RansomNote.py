#!/bin/python3

# Complete the checkMagazine function below.
def check_magazine(magazine, note):
    magazine_dictionary = dict()

    for i in magazine:
        magazine_dictionary[i] = magazine_dictionary.get(i, 0) + 1

    for nn in note:
        if nn not in magazine_dictionary:
            return "No"
        else:
            if magazine_dictionary[nn] > 0:
                magazine_dictionary[nn] -= 1
            elif magazine_dictionary[nn] == 0:
                magazine_dictionary.pop(nn)
                return "No"

    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])
    if 1 <= n <= 30000 and 1 <= m <= 30000:
        magazine = input().rstrip().split()

        note = input().rstrip().split()

        print(check_magazine(magazine, note))
