# Myesha Mahazabeen, EMPLID: 24005884

def check(tup):
    # expected tuple format (x,y,z)
    if len(tup) == 3:
        if tup[0]**2 == tup[1]**2 + tup[2]**2:
            return True
    return False
        
usr_inp = input('Enter a tuple(x,y,z):')
usr_inp_list = usr_inp.split(',')
tup = tuple(float(i) for i in usr_inp_list)
print(check(tup))