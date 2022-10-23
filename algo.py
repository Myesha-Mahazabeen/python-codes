from random import randint
from time import time_ns
import csv
import sys

def insertionSort(arr, s, e):
    for i in range(s+1, e):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def mergeSort(arr, s, e):
    if s<e-1:
        m = int((s+e)/2)
        mergeSort(arr, s, m)
        mergeSort(arr, m, e)
        merge(arr, s, m, e)

def merge(arr, s, m, e):
    if s>=e:
        return
    left, right = arr[s:m], arr[m:e]
    left.append(9999999)
    right.append(9999999)
    l, r = 0, 0
    for i in range(s, e):
        if left[l]<=right[r]:
            arr[i] = left[l]
            l+=1
        else:
            arr[i] = right[r]
            r+=1
        i+=1
    

def quickSort(arr, s, e):
    if(s<e):
        p = divide(arr, s, e)
        quickSort(arr, s, p)
        quickSort(arr, p+1, e)

def rand_quickSort(arr, s, e):
    if(s<e):
        x = randint(s, e-1)
        arr[x], arr[e-1] = arr[e-1], arr[x]
        p = divide(arr, s, e)
        rand_quickSort(arr, s, p)
        rand_quickSort(arr, p+1, e)

def divide(arr, s, e):
    piv = arr[e-1]
    i = s
    j = s-1

    while i<e-1:
        if arr[i] <= piv:
            j+=1
            arr[i], arr[j] = arr[j], arr[i]
        i+=1

    arr[e-1], arr[j+1] = arr[j+1], arr[e-1]
    return j+1

def heapSort(arr, s, e):
    build_heap(arr, s, e)
    for i in range(s, e):
        arr[e-i-1], arr[0] = arr[0], arr[e-i-1]
        heapify(arr, 0, s, e-i-1)

def build_heap(arr, s, e):
    i = int(e/2)
    while i>=s:
        heapify(arr, i, s, e)
        i-=1

def heapify(arr, i, s, e):
    k = arr[i]
    l = -1
    if 2*i+1<e and arr[i]<arr[2*i+1]:
        l = 1
        k = arr[2*i+1]
    if 2*i+2<e and k<arr[2*i+2]:
        l = 0

    if l==1:
        arr[i], arr[2*i+1] = arr[2*i+1], arr[i]
        i = 2*i+1
    elif l==0:
        arr[i], arr[2*i+2] = arr[2*i+2], arr[i]
        i = 2*i+2

    if l!=-1:
        heapify(arr, i, s, e)

def radixSort(arr, s, e):
    p = max(arr)
    digits = 0
    while p!=0:
        p=int(p/10)
        digits+=1
    div = 1
    for i in range(digits):
        c = [[] for i in range(10)]
        for x in arr:
            tmp = int(x/div)
            c[tmp%10].append(x)
        arr = []
        for j in range(10):
            for k in c[j]:
                arr.append(k)
        div*=10

def sortTimer(arr, func):
    t = time_ns()
    func(arr, 0, len(arr))
    return time_ns()-t


def main():
    n = 10
    k = 31921
    header = ['N', 'Insertion Sort', 'Merge Sort', 'Heap Sort','Quick Sort', 'Quick Sort (Random)', 'Radix Sort']
    f = open('SortingTime.csv', 'w+', encoding='UTF8', newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    print(header)
    while n<1000006:
        rand_arr = [randint(0, k) for i in range(n)]
        times = []
        times.append(n)
        arr = rand_arr[:]
        if n!=1000000 : times.append(sortTimer(arr, func=insertionSort)/1000000)
        else : times.append('N/A')
        arr = rand_arr[:]
        times.append(sortTimer(arr, func=mergeSort)/1000000)
        arr = rand_arr[:]
        times.append(sortTimer(arr, func=heapSort)/1000000)
        arr = rand_arr[:]
        times.append(sortTimer(arr, func=quickSort)/1000000)
        arr = rand_arr[:]
        times.append(sortTimer(arr, func=rand_quickSort)/1000000)
        arr = rand_arr[:]
        times.append(sortTimer(arr, func=radixSort)/1000000)
        writer.writerow(times)
        print(times)
        n*=10
    f.close()

sys.setrecursionlimit(50000)
main()


