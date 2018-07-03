#Pseudocode:
#"to be, or not to be"
#dictionary = {"to":2, "be":2, "or":1, "not":1}
#["to", "be", "or", "not", "to", "be"]
#last_four_lines ==

words = ["to", "be", "or", "not", "to", "be"]

#result in terminal should print = {"to":2, "be":2, "or":1, "not":1}

wordcount = {}

for word in words:
    if word in wordcount:
        wordcount[word] = wordcount[word] + 1
        #^also written as: wordcount[word] += 1
    else:
        wordcount[word] = 1 

print wordcount

#another method:

#sentence = "to be, or not to be"

#padded_sentence = sentence + ' '

#words = []

#curr_word = ''

#for char in padded_sentence
#   if char == ' ' 
#       words.append(curr_word)
#       curr_word = ''
#   else:
#       curr_word += char 

#words.append(curr_word)