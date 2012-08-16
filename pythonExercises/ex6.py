#An integer inside a string inside a variable
x = "There are %d types of people." % 10
#string inside a variable
binary = "binary"
#sting inside a variable
doNot = "don't"
#two strings inside a string inside a variable
y = "Those who know %s and those who %s." % (binary, doNot)

#print variable
print x
print y

#print string with a string in it which is being printed as debug variable
print "I said: %r." % x
#same as above but printed as a string instead of a debug variable
print "I also said: '%s'." % y

#bool value saved as a variable
hilarious = False
#string saved as a variable with an empty format specifier in it
jokeEvaluation = "Isn't that joke so funny?! %r"

#printing string with its empty format specifier being filled by an additional variable
print jokeEvaluation % hilarious

#self explanatory
w = "This is the left side of..."
e = "a string with a right side."

print w + e
