fin = open("radixsort.in")
 
def merge(l, r, k):
    i = 0
    j = 0
    newMas = list()
    while (j < len(r)) and (i < len(l)):
        if l[i][k] <= r[j][k]:
            newMas.append(l[i])
            i += 1
        else:
            newMas.append(r[j])
            j += 1
    newMas += l[i:] + r[j:]
    return newMas
 
def mergeSort(mas, k):
    lenth = len(mas)
    if lenth > 1:
        l = mas[:lenth // 2]
        r = mas[lenth // 2:]
        return merge(mergeSort(l, k), mergeSort(r, k), k)
    else:
        return mas
    
n, m, k = map(int, fin.readline().split())
mas = []

for i in range(n):
    mas.append(fin.readline())
    
for i in range(m - 1, m - k - 1, -1):  
    mas = mergeSort(mas, i)
    
with open("radixsort.out", "w") as fout:
    print('\n'.join([str(i) for i in mas]), file = fout)
    

fout.close()
'''n = int(fin.readline())
m = int(fin.readline())
k = int(fin.readline())
mas = list(map(str, fin.readline().split()))
for i in range(m - 1, m - k - 1, -1):  
    mas = mergeSort(mas, i)
print('\n'.join([str(i) for i in mas]), file = fout)
fout.close()'''
