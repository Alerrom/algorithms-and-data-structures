fin = open("input.txt", "r")
fout = open("output.txt", "w")

n = int(fin.readline())

matrix = []
for i in range(n):
    matrix.append(list(map(int, fin.readline().split())))

flag = 0

for i in range(n):
    for j in range(i, n):
        if (matrix[i][j] != matrix[j][i]) and i != j:
            flag += 1
        elif (matrix[i][j] == matrix[j][i] == 1) and i == j:
            flag += 1

if not flag:
    print("YES", file = fout)
else:
    print("NO", file = fout)
            

fin.close()
fout.close()
