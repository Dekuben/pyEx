def CheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print "You have %d cheeses!" % cheeseCount
    print "You have %d boxes of crackers!\n" % boxesOfCrackers
    
print "I can just give the function numbers directly:"
CheeseAndCrackers(20,30)

print "OR, I can use variables:"
amountOfCheese = 10
amountOfCrackers = 50

CheeseAndCrackers(amountOfCheese, amountOfCrackers)

print "We can even do math inside too:"
CheeseAndCrackers( 10 + 20, 5+ 6)

print "variables and math can also be combined:"
CheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000)
