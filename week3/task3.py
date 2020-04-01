#task 3

import random
guesscounter = 0
q = None

num = random.randint(1,100)
print ( " The Random number is: ", num)
print (" Guess the number between 1 and 100!")
while q != 1:
    a = int (input (" Enter your guess:"))
    guesscounter = guesscounter + 1
    if  a > num:
        print (" Too High!")
    elif a < num:
        print (" Too Low!")
    else:
        print (a, "is correct, you win.")
        break
    
print (" You got it in", guesscounter, " guesses.")
 
