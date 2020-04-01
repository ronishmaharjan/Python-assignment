#task 3

'''def inputInt(value):
    number = True
    while number:
        numResponse = input(value)
        
        try:
            numResponse = int(numresponse)
            return numResponse
        
        except ValueError:
            print ("invalid input: integer number is required")
            
value = inputInt ("Enter an integer number:")
print ("Integer value is ", value)'''


def inputFloat(value):
    number = True
    while number:
        numResponse = input(value)

        try:
            numResponse = float(numResponse)
            return numResponse

        except ValueError:
            print ("invalid input: float number is required")

value = inputFloat ("Enter an float number:")
print ("Float value is ", value)


        
            
