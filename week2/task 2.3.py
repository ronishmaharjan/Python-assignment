choice = input (" 1 for Metric to imperial \n 2 for Imperial to Metric\n" )

if choice == '1':
    m = input ( " entert length in metre: " )
    cm = float ( m ) * 100
    print ( m, " metre = ", cm, " centimetre " )

elif choice == '2':
    g = input ( " enter weight in gram: " )
    kg = float ( g ) * 0.001
    print ( g, " grams =", kg, "kilogram" )

else:
    print ( " invalid choice " )
    
