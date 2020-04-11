# Example of possible lack of Memory if the file is Big
# Ref https://realpython.com/introduction-to-python-generators/
# In this case, open() returns a generator object that you can lazily iterate through line by line.
# However, file.read().split() loads everything into memory at once, causing the MemoryError.

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


# Refactoring CSV Reader
# This method is now a Generator Function
def csv_reader_yield(file_name):
    for row in open(file_name, "r"):
        yield row

# with yield you return a generator object

###############################
# Generator Expression
##########################
file_name = "config.csv"
csv_gen = (row for row in open(file_name))

####### Infinite Loops ########
# Instead, the state of the function is remembered.
# when next() is called on a generator object
# (either explicitly or implicitly within a for loop),
# the previously yielded variable num is incremented, and then yielded again.
# When the Python yield statement is hit, the program suspends function execution
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
# First way of using a generator
#for i in infinite_sequence():
    #print(i, end=" ")

# Second way to use a generator, using the word "next"
gen = infinite_sequence()
next(gen)