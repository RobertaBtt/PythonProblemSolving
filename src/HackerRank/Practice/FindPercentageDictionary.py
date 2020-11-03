#!/bin/python3


if __name__ == '__main__':

    n = int(input())
    if 2 <= n<=10:
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        if query_name in student_marks:
            print("%.2f" % (float(sum(student_marks[query_name]))/float(len(student_marks[query_name]))))
'''

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

'''

#Input number 2
'''

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

'''