shift_num = 13
message = raw_input("this is a SECRET Message. destroy immediately ;)")
lowercase = ["a", "b", "c"]
uppercase = ["A", "B", "C"]
output = ""
for char in message: 
    if char in lowercase:
        for i in range(len(lowercase)):
            if char == lowercase[i]:
                newindex = i + shift_num
                newcharacter = lowercase(newindex)
                output += newcharacter
    elif character in uppercase:
        if char in uppercase:
            for i in range(len(uppercase)):
                newindex = i + shift_num
                newcharacter = uppercase(newindex)
                output += newcharacter
    else:
        output += char 
print output