def make_an_empty_matrix(width, height):
    #Initializing the resulting matrix
    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(0)
    print result
#^this is an empty function. it needs parameters and a call to run properly

def hello():
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World") 
  return 
  
hello()

def hello_func():
    print('Hello Function!')

#hello_func() or print('Hello Function') will call the function
#DON'T REPEAT YOURSELF

#list_of_numbers = [5, 124, 'fine thanks', -100]

#def get_largest_number(input_list):
#    largest_number = input_list[0]
#    for i in range(1, len(input_list)):
#        if input_list[i] > largest_number:
#            largest_number = input_list[i]
#    return largest_number

#result = get_largest_number(list_of_numbers)