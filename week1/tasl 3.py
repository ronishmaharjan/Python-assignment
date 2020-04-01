#to convert fahrenheit into celsius
f=input("enter temperature in fahrenheit:")
c=((float(f) - 32)*5)/9
print(f,"fahrenheit is",float(c),"celsius")

#to convert celsius into fahrenheit
c=input("enter temperature in celsius:")
f=((float(c)*9)/5)+32
print(c,"celsius is",float(f),"fahrenheit")

#to find the area and circumference of circle
import math
r=input("enter radius of circle:")
a=math.pi*float(r)**2
c=2*math.pi*float(r)
print("area of circle is ",float(a),"and circumference is",float(c))

#to calculate body mass index of a human
w=input("enter weight of human in kg:")
h=input("enter height in metres:")
BMI=int(w)/(float(h)**2)
print("BMI=",float(BMI))

#to calculate simple interest
p=input("enter principle:")
t=input("enter time:")
r=input("enter rate:")
SI=(int(p)*int(t)*float(r))/100
print("Simple Interest=",float(SI))




