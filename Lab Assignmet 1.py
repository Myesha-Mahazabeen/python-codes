#Myesha Mahazabeen EMPLID: 24005884
#question 1
def sec_to_week(n):
    sec_in_week=60*60*24*7
    return n/sec_in_week

print (sec_to_week(1000000))

#question 2
import math
from math import sqrt,pow
def quadroot(a,b,c):
    x= (-b+sqrt(pow(b,2)-4*a*c))/(2*a)
    y= (-b-sqrt(pow(b,2)-4*a*c))/(2*a)
    return x,y
print(quadroot(4,8,4))

#question 3
def concate_2(s1,s2):
    return s1+s2
s1= input("s1: ")
s2=input(" s2: ")
s3=input(" s3: ")
print(concate_2(s1,concate_2(s2,s3)))

#question 4
def nth_root(num,n):
    return num**(n**-1)

print(nth_root(8,3))

#question 5
def xmodn(x, n):
    div = int(x/n)
    mod = x - div*n
    return mod

print(xmodn(6, 4))


