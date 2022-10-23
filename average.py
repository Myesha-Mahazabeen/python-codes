
# def average (n):
#     sum=0
#     for i in range(n):
#         X= float(input())
#         sum=sum+X
#     avg=sum/n
#     return avg   
# print(average (5))

# sentinal loop
def average ():
    sum=0
    n=0
    avg=0
    while (True):
        X= float(input("Input -1000 to stop."))
        if X==-1000:
            break
        n= n+1
        sum=sum+X
    if n!=0:
        avg=sum/n
    return avg   
print(average ())


def average ():
    sum=0
    n=0
    avg=0
    while (True):
        X= input("press enter to quit: ")

        if X=="":
            break

        X = float(X)
        n= n+1
        sum=sum+X

    if n!=0:
        avg=sum/n
        
    return avg   
print(average ())



#interactive loop
sum = 0.0
count = 0
moredata = "yes"
while moredata == "yes":
    x = float(input("Enter a number >> "))
    sum = sum + x
    count = count + 1
    moredata = input("Do you have more numbers (yes or no)? ")
    
print("\nThe average of the numbers is", sum / count)