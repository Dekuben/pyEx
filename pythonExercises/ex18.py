# introducing functions
#this first fucntion is similiar to using system.args
def PrintTwo(*args):
    arg1, arg2 = args
    print "arg1: %r. arg2: %r" % (arg1, arg2)
    
#instead of *args seperate variables can be used as arguments
def PrintTwoAgain(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
#fucntion with one argument
def PrintOne(arg1):
    print "arg1: %r" % arg1
    
#function with no arguments
def PrintNone():
    print "Nothing."

PrintTwo("Ben","Horwood")
PrintTwoAgain("Ben","Horwood")
PrintOne("First!")
PrintNone()
