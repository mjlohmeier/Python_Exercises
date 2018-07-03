# box = []

numheight = int(raw_input("Height? "))
numwidth = int(raw_input("Width? "))
num = 0

# for range[0] in range(0, numheight):
#   box.append(["*"] * numwidth)
# for range [1]

# def print_box(box):
#   for row in box:
#     print " ".join(row)

# print_box(box)

while num < numheight:
    if num == 0 or num == numheight - 1:
        print "*" * numwidth
    else:
        print "*" + " " * (numwidth-2) + "*"
    num += 1
    
     