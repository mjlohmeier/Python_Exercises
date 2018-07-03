pyramid = []

numsquare = int(raw_input("How big is the square? "))

for x in range(0, numsquare):
  pyramid.append(["*"] * numsquare)

def print_pyramid(pyramid):
  for row in pyramid:
    print " ".join(row)

print_pyramid(pyramid)