fin = open("input.txt", "r")
fout = open("output.txt", "w")

n, m = map(int, fin.readline().split())

matrix = [[0 for j in range(n)] for i in range(n)]

for i in range(m):
    u, v = map(int, fin.readline().split())
    matrix[u - 1][v - 1] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ", file = fout)
    print(file = fout)

fin.close()
fout.close()
