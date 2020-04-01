#task4

def inputInt ( Message_error = "Error", minValue = None, maxValue = None):
    Message_error = str (input ("Enter meassage error"))
    minValue = int (input ( "Enter Minimum value:"))
    maxValue = int (input ( "Enter Maximum value:"))

    while True:
        result = int (input("result:"))

    try:
        value = int(result)

    except ValueError :
        print ("Syntax Error!!")

    if result <= minValue:
        print ("It is below minimum.", Message_error)
        continue
    if result >= maxValue:
        print ("It is below maximum", Message_error)
        continue
    return result
inputInt()

    
