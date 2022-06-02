fin = open("pathsg.in", "r")
fout = open("pathsg.out", "w")

n, m = map(int, fin.readline().split())
INF = 99999

W = [[INF if i != j else 0 for i in range(n)] for j in range(n)]

for i in range(m):
    u, v, w = map(int, fin.readline().split())
    W[u - 1][v - 1] = w


for k in range(n):
    for i in range(n):
        for j in range(n):
            W[i][j] = min(W[i][j], W[i][k] + W[k][j])


for line in W:
    print(" ".join(map(str, line)), file=fout)


fin.close()
fout.close()
