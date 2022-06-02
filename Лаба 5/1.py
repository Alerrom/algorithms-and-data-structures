fin = open("height.in")
fout = open("height.out", "w")
 
def Height(i, h):
    if L[i] == -1 and R[i] == -1:
        return h
    if L[i] > -1 and R[i] > -1:
        V[L[i]] = 1
        V[R[i]] = 1
        return max(Height(L[i], h + 1), Height(R[i], h + 1))
    elif L[i] > 0:
        V[L[i]] = 1
        return Height(L[i], h + 1)
    else:
        V[R[i]] = 1
        return Height(R[i], h + 1)
 
n = int(fin.readline())
K = []
L = []
R = []
V = []
h = 0
max_h = 0

for i in range(n):
    k, l, r = map(int, fin.readline().split())
    K.append(k)
    L.append(l - 1)
    R.append(r - 1)
    V.append(0)

for i in range(n):
    if not V[i]:
        max_h = max(max_h, Height(i, 1))
 
print(max_h, file = fout)
fout.close()

