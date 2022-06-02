fin = open("sortland.in.txt")
fout = open("sortland.out.txt", "w")

n = int(fin.readline())
M = list(map(float, fin.readline().split()))

for i in range(n):
    M[i] = [M[i], i + 1]

for j in range(1, n):
    current = M[j]
    key = M[j][0]
    i = j - 1
    while i > -1 and M[i][0] > key:
        M[i + 1] = M[i]
        i -= 1
    M[i + 1] = current

print(M[0][1], M[n // 2][1], M[n - 1][1], file=fout)

fout.close()
