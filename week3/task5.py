#task 5

fastest = 9999
slowest = 0
total = 0
i = 0

while True:
    laptime = input("Enter lap time a (press \"x\" to end):")

    if laptime == "x":
        break

    i = i + 1

    if float(laptime) < float (fastest):
        fastest =  laptime
    if float(laptime) > float(slowest):
        slowest =    laptime
    total = total + float(laptime)

avg = round(total / i)
print ("Fastest lap time: ", fastest)
print ("Slowest lap time: ", slowest)
print ("Average lap time: ", avg)
            
            
                     
