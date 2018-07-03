list_of_numbers = [5, 124, -100]

def get_largest_number(input_list):
    largest_number = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] > largest_number:
            largest_number = input_list[i]
    return largest_number

result = get_largest_number(list_of_numbers)

print result