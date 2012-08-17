from os.path import exists

fromFile = raw_input("Please enter the file to read from:\n ")
toFile = raw_input("Please enter the file to write to:\n ")

print "Copying from %s to %s" % (fromFile, toFile)

inFile = open(fromFile)
inData = inFile.read()

print "The input file is %d bytes long" % len(inData)

print "Does the output file exist? %r" % exists(toFile)

raw_input("Ready, hit RETURN to continue, CTRL-C to abort.")

outFile = open(toFile, 'w')
outFile.write(inData)

print "Alright, all done."

outFile.close()
inFile.close()
