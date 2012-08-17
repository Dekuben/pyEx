inputFile = raw_input("Please enter the file to read from:\n ")

def PrintAll(f):
    print f.read()
    
def Rewind(f):
    f.seek(0)
    
def PrintLine(lineCount, f):
    print lineCount, f.readline()
    
currentFile = open(inputFile)

print "Printing whole file:\n"

PrintAll(currentFile)

print "Rewinding file."

Rewind(currentFile)

print "Printing three lines:"

i = 1
PrintLine(i, currentFile)
i += 1
PrintLine(i, currentFile)
i += 1
PrintLine(i, currentFile)
