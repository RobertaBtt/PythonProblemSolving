#!/bin/python3
import os
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.


def gradingStudents(grades):

    manipolated_grades = []
    for grade in grades:
        if 0 <= grade <= 100:
            if grade in range (38,40+1):
                manipolated_grades.append(40)
            elif grade < 38:
                manipolated_grades.append(grade)
            else:
                if (grade % 5) == 0:
                    manipolated_grades.append(grade)
                elif (grade +1) % 5 == 0:
                        manipolated_grades.append(grade+1)
                elif (grade +2) %5 == 0:
                        manipolated_grades.append(grade + 2)

                else: manipolated_grades.append(grade)


    return manipolated_grades
    # Write your code here

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/gradingStudents.txt"



    grades_count = int(input().strip())

    grades = []

    if 1 <= grades_count <= 60:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        for _ in range(grades_count):
            grades_item = int(input().strip())
            grades.append(grades_item)

        result = gradingStudents(grades)

        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

        fptr.close()
