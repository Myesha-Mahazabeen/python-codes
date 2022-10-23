# def xmodn(x, n):
#     div = int(x/n)
#     mod= x- (div*n)
#     return mod
# #print (xmodn(12,6))

def sumOfDigits(n):
    sum=0
    while(n!=0):
        sum=sum+(n%10)
        n=n//10
    return sum
print(sumOfDigits(347))
    