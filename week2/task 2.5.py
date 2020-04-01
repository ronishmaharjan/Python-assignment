#task 5

i = int ( input ( " enter income of a person in AUD: " ))

if ( int ( i ) <= 18200 ):
    print ( " you do not need to pay tax.")
elif ( int( i ) <= 37000 ):
    t = 0.19 * ( i - 18200 )
    print ( " your tax is ",float(t))
elif ( int ( i ) <= 80000 ):
    t = 3572 + ( 0.325 * ( i - 37000 ))
    print ( " your tax is ", float(t) )
elif ( int ( i ) <= 180000 ):
    t = 17547 + (0.37 * (i - 80000))
    print ( " your tax is ", float(t) )
else:
    t = 54547 + ( 0.45 * ( i - 180000 ))
    print ("your tax is ", float(t) )

