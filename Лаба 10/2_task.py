fin = open("spantree.in", "r")
fout = open("spantree.out", "w")

def dist(i, j):
    global x, y
    return ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5

n = int(fin.readline())

ans = 0
x = []
y = []
mn = [30000] * n
prev = [-1] * n
used = [False] * n

for i in range(n):
    x_i, y_i = map(int, fin.readline().split())
    x.append(x_i)
    y.append(y_i)
    

for i in range(n):
    v = -1

    for j in range(n):
        if not used[j] and (v == -1 or mn[j] < mn[v]):
            v = j

    if prev[v] != -1:
        ans += dist(v, prev[v])

    used[v] = True

    for j in range(n):
        if dist(v, j) < mn[j]:
            prev[j] = v
            mn[j] = dist(v, j)

print(ans, file = fout)


fin.close()
fout.close()
