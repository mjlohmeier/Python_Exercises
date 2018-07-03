bill_input = raw_input("bill?")
bill = float(bill_input)

servicelevel_input = raw_input("service level?\n")

tip_percent = 0

if servicelevel_input == 'good': 
    tip_percent = 0.2

tip_amount = bill * tip_percent

total = bill + tip_amount
print "the total is " , total

#totalbill_input = int(raw_input('WHAT IS TOTAL BILL?\n')) 

#split_input = int(raw_input('HOW MANY WAYS TO SPLIT?\n'))

#priceper = totalbill_input/split_input

#print priceper