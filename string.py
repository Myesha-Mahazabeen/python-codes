# str=input("Roll, Name: ")
# print(str[5:])

# str= "saad sakib"
# str= "r"+ str[1:5]+"r"+str[6:7]+"g"+str[8:10]
# str= str[:1].upper()+ str[1:5]+str[5:6].upper()+str[6:7]+"g"+str[8:10]
# print (str)
# ...
# s = input("roll, name:")
# x = s.find(' ')
# print(s[x+1:])


# clg = input("must have 2 'c's:")

# x = clg.find('c')
# # cacny
# clg = clg[x+1 : ]
# # acny
# print(clg.find('c')+x+1)

# or

# clg = input("must contant 2 'c's: ")
# x = clg.find('c')
# print(clg.find('c', x+1))


# .....
# clg = input("enter string:")

# x = clg.find('c')
# while(x!=-1):
#     print(x)
#     x = clg.find('c', x+1)

str = 'greetings'
for i in range(len(str)-2):
    print(str[0 : len(str)-i])