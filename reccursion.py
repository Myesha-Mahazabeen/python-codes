def adder(n):
    if n==0:
        return 0
    return n + adder(n-1)

print (adder(4))

# def Multi(n):
#     if(n==1):
#         return 1
#     if (n==2):
#         return 2
#     return Multi(n-1) * Multi(n-2)

# print (Multi(5))