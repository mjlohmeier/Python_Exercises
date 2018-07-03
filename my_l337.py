message = "hi noobs lol"

def leet(message):
    leet = ["a", "e", "g", "i", "o", "s", "t"]
    l337 = ["4", "3", "6", "1", "0", "5", "7"]
    new_string = ""
    for letter in message:
        if letter in leet:
            for j in range(len(leet)): 
                if letter == leet[j]:
                    new_string += l337[j]
                    break
        else:
            new_string += letter
    return new_string

print leet(message)

#====================================================>