#Myesha Mahazabeen EMPLID: 24005884

#Question 1

import random

def writeRand(myfile):
    num = random.randint(10, 100)
    for i in range(num):
        rand = random.randint(0, 1000)
        print(rand, file=myfile)

def readRand():
    r_file = open('1_randNums.txt', 'r')
    cnt = 0
    sum = 0
    for num in r_file:
        if num == '': break
        cnt += 1
        sum += int(num)
    r_file.close()
    return sum/cnt

myfile = open('1_randNums.txt', 'w+')
writeRand(myfile)
myfile.close()
print(readRand())

#Question 2

def round_float():
    try:
        mon_file = open('Months.txt', 'r+')
        writer = ''
        for line in mon_file:
            if line!='\n':
                month, num = line.split(' ')
                num = float(num)
                if(num-int(num)>=0.5):
                    num = int(num)+1
                else:
                    num = int(num)
                writer += month+' '+str(num)+'\n'
        mon_file.close()
        wri_file = open('Months.txt', 'w+')
        print(writer, file=wri_file, end="")
        wri_file.close()
            

    except FileNotFoundError:
        print("Please make sure 'Months.txt' is present in correct folder and run again")
        
round_float()


#Question 3

import random

def fib(j, i):
    if i==1 and j<=2:
        return 1
    elif i==1:
        return fib(j-1, i)+fib(j-2, i)
    elif i==2:
        return fib(j-1, i-1)
    
    return fib(j-1, i-1)+fib(j-2, i-2)

file = open('3_fib_triangle.txt', 'w+')

try:
    res = input("Do you want to continue (yes/no): ")
    while(res == 'yes' and res != 'no'):
        n = random.randint(10, 30)
        s = ''
        for i in range(1, n+1):
            for j in range(1, i+1):
                s += str(fib(i, j))+' '
            s+='\n'
        print(s, file=file, end="")
        res = input("Do you want to continue (yes/no): ")

except:
    print("Invalid response")

file.close()

#Question 4

def printSum(num):
    sm = 0
    if num.isdigit() == False:
        print("Invalid input, please enter an integer number")
        return
    for n in num:
        sm += int(n)
            
    print("Sum:", sm)

str = input("enter a number (press 'q' to quit): ")
while(str != 'q'):
    printSum(str)
    str = input("enter a number (press 'q' to quit): ")


#Question 5
str = "Greetings"

def truncate(str):
    for i in range (len(str)):
        print(str[0: len(str)-i])
        input()
truncate(str)
