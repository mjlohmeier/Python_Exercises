numbers = ([4, 608, 1, 8, 4 -3 -2, -104])
def myfunc(list):
    largest_number = None
    for i in list:
        if i > largest_number:
            largest_number = i
    return largest_number
print myfunc(numbers)