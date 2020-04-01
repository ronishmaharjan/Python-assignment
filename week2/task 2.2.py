s = input ( "enter a string: " )
if s.isalpha(): 
    print ( " the string contain letters only " )
elif  s.isupper():
    print ( " the string is in uppercase " )
elif s.islower():
    print ( " the string are in lower case " )
elif s.isdigit():
    print ( " the string contains numbers only " )

length = len ( s )
print (" the string has ", length, "letters")
