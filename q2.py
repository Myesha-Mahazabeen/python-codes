# Myesha Mahazabeen, EMPLID:24005884

class Answer:
    def swapItems(self, list_1):
        list_2 = []
        for i in range(len(list_1)):
            mx = 0
            for j in range (i+1, len(list_1)):
                mx = max(mx, list_1[j])
            list_2.append(mx)
        
        return list_2

L = [18, 19, 6, 5, 7, 2]
a = Answer()
print(a.swapItems(L))