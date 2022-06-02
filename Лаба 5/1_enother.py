fin = open("height.in")
fout = open("height.out", "w")

def Height(root):
    if L[root] == -1 and R[root] == -1:
        return 1
    l = 0
    r = 0
    if R[root] != -1:
        r = Height(R[root])
    if L[root] != -1:
        l = Height(L[root])
    return max(l + 1, r + 1)
    
n = int(fin.readline())

K = []
L = []
R = []

for i in range(n):
    k, l, r = map(int, fin.readline().split())
    K.append(k)
    L.append(l - 1)
    R.append(r - 1)

if n != 0:
    print(Height(0), file=fout)
else:
    print(0, file=fout)

fin.close()
fout.close()
