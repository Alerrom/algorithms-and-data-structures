fin = open("input.txt", "r")
fout = open("output.txt", "w")

n, m = map(int, fin.readline().split())

matrix = [[0 for j in range(n)] for i in range(n)]

for i in range(m):
    u, v = map(int, fin.readline().split())
    matrix[u - 1][v - 1] += 1

flag = 0

for i in range(n):
    for j in range(i, n):
        if (matrix[i][j] + matrix[j][i]) >= 2:
            flag += 1

if flag:
    print("YES", file = fout)
else:
    print("NO", file = fout)

fin.close()
fout.close()
