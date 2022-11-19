__author__ = 'RobertaBtt'
from random import choice
import string

def base_encode(num_of_chars):
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))

print(base_encode(8))
