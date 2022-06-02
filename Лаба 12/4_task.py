fin = open("knight2.in", "r")
fout = open("knight2.out", "w")

n, m = map(int, fin.readline().split())

f = [[0 for j in range(m + 3)] for i in range(n + 3)]

f[2][2] = 1
s_i, s_j = 2, 2

while s_i < n + 1 or s_j < m + 1:
    if s_j == m + 1:
        s_i += 1
    else:
        s_j += 1

    i, j = s_i, s_j
    while i <= n + 1 and j >= 2:
        f[i][j] = f[i + 1][j - 2] + f[i - 1][j - 2] + f[i - 2][j - 1] + f[i - 2][j + 1]
        i += 1
        j -= 1

print(f[n + 1][m + 1], file=fout)

fin.close()
fout.close()
