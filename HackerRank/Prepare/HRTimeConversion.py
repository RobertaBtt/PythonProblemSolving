# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import *
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Sample input : 07:05:45PM
# Sample output 19:05:45

format = '%H:%M:%S'

def manually_time_conversion(input_string):
    AM_PM = input_string[-2:]
    hours = input_string[0:2]
    minutes = input_string[3:5]
    seconds = input_string[6:8]

    if AM_PM == "PM":
        if int(hours) == 12:
            new_hours = 12
        else:
            new_hours = 12+int(hours)
        new_time = str(new_hours)+":"+minutes+":"+seconds
    else:
        if int(hours) == 12:
            new_hours = "00"
        else:
            new_hours = hours
        new_time = str(new_hours)+":"+minutes+":"+seconds
    return new_time


def time_conversion(s):
    converted_time = datetime.strptime(s,"%I:%M:%S%p")
    return str(converted_time.time())


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "/tmp/time.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = manually_time_conversion(s)
    result2 = time_conversion(s)

    fptr.write(result + '\n')
    fptr.write(result2 + '\n')

    fptr.close()
