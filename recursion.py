def pow_mn(m,n):
    if n==0:
        return 1
    return m*pow_mn(m,n-1)
    
print (pow_mn (3,5))

# def factorial(n):
#     if n==0:
#         return 1
#     return n * factorial(n-1) 
# print (factorial(5))

# def log2n(n):
#     if n>1:
#         return 1+ log2n(n/2)
#     return 0
# print (log2n(8))
