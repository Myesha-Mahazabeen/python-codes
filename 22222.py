import random

def writeRand(myfile):
    num = random.randint(10, 100)
    for i in range(num):
        rand = random.randint(0, 1000)
        print(rand, file=myfile)

def readRand():
    r_file = open('1_randNums.txt', 'r')
    cnt = 0
    sum = 0
    for num in r_file:
        if num == '': break
        cnt += 1
        sum += int(num)
    r_file.close()
    return sum/cnt


myfile = open('1_randNums.txt', 'w+')
writeRand(myfile)
myfile.close()
print(readRand())