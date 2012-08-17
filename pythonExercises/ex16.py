filename = raw_input(
"Please type the name of the file.")

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncuating the file. Goodbye!"
target.truncate()

print "Now i'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write("%r\n%r\n%r\n"% (line1, line2, line3)) 

print "And finally, we close it."
target.close()
