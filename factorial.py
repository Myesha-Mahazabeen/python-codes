def fib(x):
    if(x<2):
        return 1
    return fib(x-1) + fib(x-2)
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

def printNum(n):
    print(n)
    if n==0:
        return
    printNum(n-1)

# printNum(10)
# print(fib(5))
# print(factorial(6))


for j in range(21):
    for k in range(37):
        if j%5==0:
            if k%9==0 or k%9==4 or k%9==8:
                print('^', end="")
            elif k%9==2 or k%9==6:
                print('-', end="")
            else:
                print(" ", end="")
        else:
            if k%9==0:
                print("i", end="")
            else:
                print(" ",end="")
    print()


# ^
# k%9=0 or k%9=4 or k%9=8:
#     print('^')

#  0, 4, 8
#  9, 13, 17
#  18, 22, 26
#  27, 31, 35
#  36 

#  -
#  k%9==2 or k%9==6:
#     print('-')
#  2, 6, 
#  11, 15, 
#  20, 24, 
#  29, 33
