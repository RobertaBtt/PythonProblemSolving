#!/bin/python3



def countApplesAndOranges(houseBegin, houseEnd, positionTreeApple, positionTreeOrange, m, apples, n, oranges):

    inHouseApples = 0
    inHouseOranges = 0

    if positionTreeApple < houseBegin < houseEnd < positionTreeOrange:
        if 1 <= houseBegin <= 100000 and 1 <= houseEnd <= 100000 and 1 <= positionTreeApple <= 100000 and 1<= positionTreeOrange <= 100000 \
            and 1 <= m <=100000 and 1 <= n <=100000:

            for apple in apples:
                if -100000 <= apple <= 100000:
                    if apple > 0:
                        if houseBegin <= (positionTreeApple + apple) <= houseEnd:
                            inHouseApples += 1


            for orange in oranges:
                if -100000 <= orange <= 100000:
                    if orange < 0:
                        if houseBegin <= (positionTreeOrange - abs(orange) )  <= houseEnd:
                            inHouseOranges += 1

    return [inHouseApples, inHouseOranges]

if __name__ == '__main__':
    st = input().split()

    houseBegin = int(st[0])
    houseEnd = int(st[1])
    ab = input().split()
    positionTreeApple = int(ab[0])
    positionTreeOrange = int(ab[1])

    mn = input().split()

    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    result = countApplesAndOranges(houseBegin, houseEnd, positionTreeApple, positionTreeOrange, m, apples, n, oranges)
    print(*result, sep='\n')
