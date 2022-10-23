# Myesha Mahazabeen, EMPLID: 24005884
def extractStr(str):
    l = str.split(',')
    strOutput = l[1] + ' ' + l[3] + ' ' + l[0]
    return strOutput

str = "Johnson,1234,3.26,Ronald"
strOutput = extractStr(str)
print(strOutput)
