myName = 'Ben T. Horwood'
myAge = 23 # srs
myHeight = 74 # inches
myWeight = 180 # lbs
myEyes = 'Brown'
myTeeth = 'White'
myHair = 'Brown'

print "Let's talk about %s." % myName
print "He's %d inches tall." % myHeight
print "He's %d pounds heavy." % myWeight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (myEyes, myHair)
print "His teeth are usually %s depending on the coffee." % myTeeth

#This line is tricky, double check it
print "If I add %d, %d and %d I get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight)
