tip_input = raw_input("tip?")
tip = float(tip_input)

bill_input = raw_input("bill?")
bill = float(bill_input)

tip_ratio = tip / bill

if tip_ratio < 0.10:
    print "stingy!"
elif tip_ratio > .20:
    print "generous!"

else:
    print "w/e"