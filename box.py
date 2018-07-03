# Grids 2: a box
iheight = raw_input("Height of box? ")
rows = int(iheight)
iwidth = raw_input("Width of box? ")
cols = int(iwidth)

bumperRow = []
for _ in range(0, cols):
    bumperRow.append("*")

fillRow = ["*"]
for _ in range(0, cols - 2):
    fillRow.append(" ")
fillRow.append("*")

# Draw the box
print " ".join(bumperRow)
for _ in range (0, rows - 2):
    print " ".join(fillRow)
print " ".join(bumperRow)