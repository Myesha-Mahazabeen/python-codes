# Myesha Mahazabeen, EMPLID: 24005884

def numOfOperation(str1, str2):
    if len(str1)==0:
        return len(str2)
    elif len(str2)==0:
        return len(str1)

    if str1[0]==str2[0]:
        return numOfOperation(str1[1:], str2[1:])
    else:
        return 1+min(numOfOperation(str1[1:], str2), numOfOperation(str1, str2[1:]), numOfOperation(str1[1:], str2[1:]))

s1 = 'foreseen'
s2 = 'see'
print(numOfOperation(s1, s2))
