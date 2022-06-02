fin = open("check.in")
fout = open("check.out", "w")

def check(i, k, flag):
    F = True
    if L[i] >= 0:
        F1 = (K[L[i]] < k) if flag else (K[L[i]] > k)
        F = F1 and (K[i] > K[L[i]]) and check(L[i], k, flag)
    if R[i] >= 0 and F:
        F1 = (K[R[i]] < k) if flag else (K[R[i]] > k)
        F = F1 and (K[i] < K[R[i]]) and check(R[i], k, flag)
    return F

n = int(fin.readline())

K = []
L = []
R = []

for i in range(n):
    k, l, r = map(int, fin.readline().split())
    K.append(k)
    L.append(l - 1)
    R.append(r - 1)

correct = True
if n > 0:
    top = 0

    if L[top] >= 0:
        if K[L[top]] < K[top]:
            correct = check(L[top], K[top], True)
        else:
            correct = False

    if correct and R[top] >= 0:
        if K[R[top]] > K[top]:
            correct = check(R[top], K[top], False)
        else:
            correct = False

if correct:
    print('YES', file=fout)
else:
    print('NO', file=fout)

fin.close()
fout.close()
