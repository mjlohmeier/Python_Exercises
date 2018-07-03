m1 = [
    [8, 42]
    [-6, 439]
]

m2 = [
    [9, 1]
    [11, 8000]
]

r = []
for row in m1:
    for col in row:
        wip.append(0)
    r.append(wip)

width = len(r[0])
height = len(r)

for i in range(len(r)):
    for j in range(width):
        sum = m1[i][j] + m2 [i][j]

