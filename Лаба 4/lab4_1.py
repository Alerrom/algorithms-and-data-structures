fin = open("binsearch.in")
fout = open("binsearch.out", "w")

def binsearch(key, a, n):
    global ko
    l, r, cont = 0, n, True
    ko += 1
    while (cont and l < r - 1):
        mid = (l + r)//2
        if (a[mid] > key):
            r = mid
        elif (a[mid] < key):
            l = mid
        else:
            cont = False
        ko += 1
    if a[mid] != key:
        print(-1, -1, file = fout)
    else:
        l, r = mid, mid
        while (l >= 0 and a[l] == key):
            l -= 1
            ko += 1
        while (r <= n - 1 and a[r] == key):
            r += 1
            ko += 1
        print(l + 2, r, file = fout)

ko = 0
n = int(fin.readline())
mas = list(map(int, fin.readline().split()))
m = int(fin.readline())
request = list(map(int, fin.readline().split()))
for i in request:
    binsearch(i, mas, n)
print(ko)
fout.close()

    
    
    
