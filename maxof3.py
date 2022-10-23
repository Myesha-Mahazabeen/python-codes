a= float(input("Enter a: "))
b= float(input("Enter b: "))
c= float(input("Enter c: "))

def max(a,b,c):
    if a >= b and a>=c:
        print("Max: ", a)
    elif b>=a and b>=c:
        print("Max: ", b)
    else:
        print ("Max: ", c)
max(a,b,c)


