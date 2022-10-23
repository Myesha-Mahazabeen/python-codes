#1
import math
def input():
    x1= int(input("Enter x1: "))
    y1= int(input("Enter x2: "))
    x2= int(input("Enter x3: "))
    y2= int(input("Enter y1: "))
    x3= int(input("Enter y2: "))
    y3= int(input("Enter y3: "))
    return x1,y1,x2,y2,x3,y3

x1,y1,x2,y2,x3,y3=input()

def RightAngle(x1,y1,x2,y2,x3,y3):
     
    A =math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    B =math.sqrt(((x3 - x2)**2) +((y3 - y2)**2))
    C = math.sqrt(((x3 - x1)**2) +((y3 - y1)**2))
    
    if (A**2 == (B**2 + C**2) or B**2 == (A**2 + C**2) or C**2 == (A**2 + B**2)):
        print("True")
    else:
        print ("False")

RightAngle(x1,y1,x2,y2,x3,y3)



     
