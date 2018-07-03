list_of_numbers = [5, 124, -100]

def get_smallest_number(input_list):
    smallest_number = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] < smallest_number:
            smallest_number = input_list[i]
    return smallest_number

result = get_smallest_number(list_of_numbers)

print result