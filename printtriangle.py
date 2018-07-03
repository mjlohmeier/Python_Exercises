# while num < numheight:
#     if num == 0 or num == numheight - 1:
#         print "*" * numwidth
#     else:
#         print "*" + " " * (numwidth-2) + "*"
#     num += 1
    

pyramidheight = 4
num = 0
pyramidastericks = pyramidheight - 1
while num < pyramidheight:  
    print pyramidastericks * " " + "*" * (2*num+1)+ pyramidastericks * " "
    pyramidastericks -= 1
    num += 1
  

# 1st row:
#    *  
#   ***
#  *****
# *******
