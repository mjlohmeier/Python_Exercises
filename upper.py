message = "you shall NOT pass"

upcased = ''

lowercase = ["a", "b", "c"]
uppercase = ["A", "B", "C"]

for char in message:
    letter = char
    #Search through list of lowercase letters 
    for i in range(len(lowercase)):
        lowerletter == lowercase[i]
        if lowerletter == char:
            letter = uppercase[i]
            break

    upcased = upcased + char

for char in message:
    letter = char
    if char == "a":
        letter ="A"
    upcased = upcased + char

print upcased

