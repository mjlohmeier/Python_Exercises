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

