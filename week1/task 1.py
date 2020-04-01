Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> (1+2)*3
9
>>> print("testing")
testing
>>> print("testing)
      
SyntaxError: EOL while scanning string literal
>>> print(testing)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(testing)
NameError: name 'testing' is not defined
>>> #print("testing")
>>> x=6
>>> x=x+1
>>> print(x)
7
>>> value=input("type something")
type something My name is Ronish Maharjan
>>> print("you typed",value)
you typed  My name is Ronish Maharjan
>>> print("you typed",input("type something:"))
type something:I am from Nepal
you typed I am from Nepal
>>> 