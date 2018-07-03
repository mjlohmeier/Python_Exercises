#====================================================>

max_num = 1000
list_of_nums = range(1, max_num)

multiple1 = 3
multiple2 = 5

final_list = []

for num in list_of_nums:
    if num % multiple1 == 0 or num % multiple2 == 0:
        final_list.append(num)

sum = 0
for num in final_list:
    sum += num

print sum

#====================================================>

max_num = 400

fib_array = [1, 2]
evens = []
num_to_add = fib_array[0] + fib_array[1]

while num_to_add < max_num:
    fib_array.append(num_to_add)
    num_to_add = fib_array[-1] + fib_array[-2]
        
        
for num in fib_array:
    if num % 2 == 0:
        evens.append(num)

sum = 0
for num in evens:
    sum += num

print sum

#====================================================>

