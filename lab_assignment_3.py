# Myesha Mahazabeen, EMPLID: 24005884

#Question 1

def substract(matrix_a, matrix_b):
    # assuming both matrix are of same dimension
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            matrix_a[i][j] = matrix_a[i][j]-matrix_b[i][j]

    return matrix_a

A = [[8, 9, 12], [12, 6, 7], [15, 21, 9]]
B = [[2, 3, 3], [1, 17, 4], [11, 9, 1]]
C = substract(A, B)
print('A-B=')
for x in C:
    print(x)


#Question 2

def initialize_dc():
    dc = dict()
    for i in range(65, 127):
        dc[i] = chr(i)
    return dc

print(initialize_dc())


#Question 3

class RaceCar(object):
    def __init__(self, type, accl_val, top_spd, nitro, color, yr, doors, spd=0):
        if type not in ['sports', 'street', 'muscle', 'super', 'hyper']:
            raise Exception('invalid vehicle type. valid types are: sports, street, muscle, super, hyper')
        self.type = type

        if accl_val<1000.0 or accl_val>10000.0:
            raise Exception('invalid acceleration value. it must be between 1000.0 and 10000.0')
        self.acceleration_value = accl_val

        if top_spd<1000.0 or top_spd>10000.0:
            raise Exception('invalid top speed. it must be between 1000.0 and 10000.0')
        self.top_speed = top_spd

        if nitro<1000.0 or nitro>10000.0:
            raise Exception('invalid nitro. it must be between 1000.0 and 10000.0')
        self.nitro = nitro

        self.color = color
        self.year = yr

        if doors<2 or doors>4:
            raise Exception('invalid number of doors. it must be between 2 and 4')
        self.number_of_doors = doors

        if spd>top_spd:
            raise Exception('invalid speed. it must be less than top speed')
        self.speed = spd

    def accelerate(self):
        if self.speed == self.top_speed:
            raise Exception('Speed already maximum')
        if self.speed+10<self.top_speed:
            self.speed = self.speed+10
        else:
            self.speed = self.top_speed

    def brake(self):
        if self.speed==0:
            raise Exception('Speed already 0')
        if self.speed-10>0:
            self.speed = self.speed-10
        else:
            self.speed = 0
    
    def turnLeft(self):
        print('Turning left...')

    def turnRight(self):
        print('Turning right...')

    def turnReverse(self):
        print('Turning reverse...')

    
mustang = RaceCar('muscle', 5000.0, 1900.0, 6000.0, 'green', 2018, 2)
a8 = RaceCar('sports', 3000.0, 2200.0, 7000.0, 'white', 2021, 2, 120)