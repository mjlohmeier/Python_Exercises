pyramidheight = int(raw_input("how tall do you want the pyramid to be? "))
num = 0
pyramidastericks = pyramidheight - 1
while num < pyramidheight:  
    print pyramidastericks * " " + "*" * (2*num+1)+ pyramidastericks * " "
    pyramidastericks -= 1
    num += 1
  