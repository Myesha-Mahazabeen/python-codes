# from math import*

# radius_str = input("Enter radius: " )
# radius_int= int(radius_str)

# circumference= 2*pi*radius_int
# area= pi*(radius_int**2)

# print("circumference is: ", circumference, "and area is: ", area)


# import datetime

# now= datetime.datetime.now()
# print("Current date and time: ")
# print((now.strftime("%Y-%m-%d %H:%M:%S")))

# values = input("Input some comma separated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

# def factorial(n,m):
#     if n==0:
#         return 1
#     return (n * factorial(n-1,m))%m

# print (factorial(3,5))

# def fib(n,m):
#     if n==0:
#         return 1
#     if n==1:
#         return 2
#     else:
#         return (fib(n-1,m)*fib(n-2,m))%m
# print (fib(4,5))

# from math import*
# def Rms():
#     str= input("Press negative number to exit.")
#     num= int(str)
#     sum=0
#     count=0
#     while num>0:
#         count+=1
#         sum+=num**2
#         str= input("Press negative number to exit.")
#         num= int(str)
#     avg= sum/count
#     return sqrt(avg)
# print (Rms())

#hh:mm:ss

# def time_passed(time):
#     hour= int(time[0:2])
#     min= int(time[3:5])
#     sec= int(time[6:])
#     return hour*60*60+min*60+sec
# print (time_passed("00:00:10"))

# def mod(n,m):
#     res= int(n/m)
#     tot= m*res
#     return n-tot
# print (mod(15,6))

# from math import*
# def find_root(a,b,c):
#     if b**2-4*a*c>=0:
#         root1= (-b+ sqrt(b**2-4*a*c))/2*a
#         root2= (-b- sqrt(b**2-4*a*c))/2*a
#         return root1,root2
#     else:
#         print("Invalid Input")
# print(find_root(1,2,1))

# def check_palindrom(str):
#     if len(str)<=1:
#          return True
#     if str[0]==str[-1]:
#         return check_palindrom(str[1:-1])
#     else:
#         return False
# str=input("Enter a string: ")
# print(check_palindrom(str))
        

# def reverse (str):
#     if len(str)==0:
#         return str
#     else:
#         return reverse(str[1:])+str[0]
# print(reverse("Myesha"))

# def binaryToDecimal(n):
#     return int(n,2)

# print(binaryToDecimal("101"))
        
# def logmn(m,n):
#     if n>1:
#         return 1+ logmn(n/m,m)
#     return 0
# print (logmn(2,8))

# def f():
#    global a
#    a=1
#    print (a)
# a=0
# f()
# print(a)

def printNum(n):
    print(n)
    if n==0:
        return
    printNum(n-1)
printNum (10)



    