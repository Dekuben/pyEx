tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."

fatCat = """
I'll do a list:
\t* Cat food
\t* Fish
\t* Catnip\n\t* Grass
"""

print tabbyCat
print persianCat
print backslashCat
print fatCat

#escape sequences
#\\ 	Backslash ()
#\' 	Single quote (')
#\" 	Double quote (")
#\a 	ASCII Bell (BEL)
#\b 	ASCII Backspace (BS)
#\f 	ASCII Formfeed (FF)
#\n 	ASCII Linefeed (LF)
#\N{name} 	Character named name in the Unicode database (Unicode only)
#\r ASCII 	Carriage Return (CR)
#\t ASCII 	Horizontal Tab (TAB)
#\uxxxx 	Character with 16-bit hex value xxxx (Unicode only)
#\Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx (Unicode only)
#\v 	ASCII Vertical Tab (VT)
#\ooo 	Character with octal value ooo
#\xhh 	Character with hex value hh

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
