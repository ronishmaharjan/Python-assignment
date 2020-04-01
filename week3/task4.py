#task 4

total = 0
fastest = 9999
slowest = 0
laps = int ( input (" Enter laps number: "))
count = 1

for i in range (0, laps):
    print ( " Enter lap time ", count, " of ", laps)
    laptime = float ( input (" Enter lap time: "))
    if laptime < fastest:
       fastest = laptime
    if laptime > slowest:
        slowest = laptime
    count = count + 1
    total = total + laptime
    
average = round (total / laps)
print ( "fastest lap time = ", fastest)
print ( "slowest lap time = ", slowest)
print ( "total lap time = ", total)
print ( "Average lap time = ", average )


'''    
lapTimes = [ ]
laps = int ( input ( " Enter number of laps: "))
sum = 0

for i in range (0, laps):
    time = float ( input ( " Enter lap time: "))
    lapTimes.append ( time )
    print ( "LapTimes =", lapTimes)
    sum = sum + time
    
average = sum / laps
print ( "Minimum item in lapTimes =", min(lapTimes))
print ( "Maximum item in lapTsimes =", max(lapTimes))
print ( "length of lapTimes ="len(lapTimes))
print ( "Sum = ", sum)
print ( "Average =", average)'''
