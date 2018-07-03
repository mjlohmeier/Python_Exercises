number = 600851475143

remainder = number

factor = 2

factors = []

while remainder != 1:
    if remainder % factor == 0:
        remainder = remainder / factor
    else: 
        factor += 1

print factor

#====================================================>

