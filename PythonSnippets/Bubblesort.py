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

def bubble_sort2(items):
    for i in range(len(items)): # Iterate through whole list
        already_sorted = True # Set break condition
        for j in range(len(items) - i - 1): # Maintain a growing section of the list that is sorted
            if items[j] > items[j + 1]: # Swap all out of place items.
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False # Set sorted to false if we needed to swap
        if already_sorted:
            break
    return items

# initial = list(range(len(notes)))
# initial = [0, 1, 3, 2, 4, 5, 6, 7]  # Comment as needed
# random.shuffle(initial)  # Uncomment as needed
# print(initial)
# print(bubble_sort(initial))

items = [random.randint (1,6) for _ in range(1,6)]
reordered = bubble_sort2(items)