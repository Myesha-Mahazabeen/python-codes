import math

a= float(input("Enter a: "))
b= float(input("Enter b: "))
c= float(input("Enter c: "))

def solve(a,b,c):
    disc= b*b-4*a*c
    try:
        root1= (-b+math.sqrt(b*b-4*a*c))/(2*a)
        root2= (-b-math.sqrt(b*b-4*a*c))/(2*a)
        if root1==root2:
            print("The root is: ", root1)
        else:
            print("The roots are: ", root1, root2)

    except ValueError:
        print("Invalid Inputs.")
solve (a,b,c)
         