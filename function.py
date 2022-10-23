#def add(a, b):
    #c=a+b
    #return c

#print(add(1.1, 3.2))

#def div(a,b):
    #if b==0:
        #print("Myesha Is bitch")
        #return
    #c=a/b
    #return c
#print(div(5,0))

#def conv(C):
    #F=C*1.8+32.0
    #return F
#print(conv(-40))

#def f(x):
    #while x!=0:
        #print(x%10) 
        #x=int(x/10)
#(f(1532))

#def get_vertex():
    #x = float(input(" Please enter x: ")) 
    #y = float(input(" Please enter y: ")) 
    #return x,y

#def get_triangle():
    #print("First vertex")
    #x1,y1 = get_vertex() 
    #print("Second vertex")
    #x2,y2 = get_vertex() 
    #print("Third vertex")
    #x3,y3 = get_vertex()
    #return x1, y1, x2, y2, x3, y3
       
#get_triangle()





#Celcious to Farenheit
def conv_to_F(C):
    F=C*1.8+32.0
    return F

#Farenheit to Celcious
def conv_to_C(F):
    C=(F-32.0)/1.8
    return C
print(conv_to_F(160), conv_to_C(160))


