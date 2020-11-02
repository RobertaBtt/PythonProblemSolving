import random
notes = ["C", "D", "E", "F", "G", "A", "B", "C5"]


def bubble_sort(arr):
    """
    Returns a list sorted in ascending order. We are assuming an integer list as input
    """
    length = len(arr)
    for passnum in range(length - 1):
        for i in range(length - 1 - passnum):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp


    return arr

initial = list(range(len(notes)))
initial = [0, 1, 3, 2, 4, 5, 6, 7]  # Comment as needed
random.shuffle(initial)  # Uncomment as needed
print (initial)
print(bubble_sort(initial))