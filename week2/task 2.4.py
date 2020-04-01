m = float( input ( " enter a marks: " ) )
yn = input ( " did you pass the exam(y/n)?" )


if m >= 80:
    grade = " High Distinction "
    
elif m >= 70:
    grade = " Distinction "
    
elif m >= 60:
    grade = " Credit "
    
elif m >= 50:
    grade = " Pass "
    
else:
    grade = " Fail "

if m >= 50 and yn =='n':
    print ( " your final grade = fail " )
else:
    print ( " your final grade = ", grade )
