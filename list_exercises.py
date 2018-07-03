#tote = 0 

#for numbas in [13, 21, 962, 3000, 4, 1]: 
    #tote = numbas + tote
#print tote

input_list = [13, 21, 962, 3000, 4, 1]

def sum_of_numbers(sum_list):
    sum = 0
    for number in sum_list:
        sum += number
    return sum 

sum_total = sum_of_numbers(input_list)

print sum_total