# list_1=list("Myesha") #list()constructor
# print(list_1)

# list_of_list=[[1,2,3],["Myesha"]]
# print(list_of_list)

#concate
# my_list=["myesha",1,2,3]
# my_list2=["x","y",23,56]
# print(my_list[1:])
# print(my_list2[0:2])
# print(len(my_list2))

# my_list[0]= "mahazabeen"
# print(my_list)


#print([1,"myesha",2,3][1]) #indexing=myesha

# list_4 =[1.3,4.5,7.9,6.5]
# print(min(list_4))
# print(max(list_4))

# list_x =[]
# for i in range (3):
#     name=input("Enter a name:")
#     list_x.append(name)
# print(list_x)
# print(list_x.pop())
# print(list_x)

# list_y=[]
# list_y.append(4)
# list_y.append(8)
# list_y.append(9)
# #print(list_y)
# print(list_y[:1]+list_y[2:])
# #list_z=[list_y[0],list_y[2]]
# list_y.extend([1,2,3])
# list_y.remove(8)

str= "this is a test"
l_1= str.split()
for x in  l_1:
    print(x[::-1],end=' ')
print()


a_list = [1, 2, 3]
b_list = a_list[:]
a_list.append(27)
print(b_list)

