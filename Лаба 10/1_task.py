fin = open("input.txt", "r")
fout = open("output.txt", "w")

n, m = map(int, fin.readline().split())

ans = [0 for j in range(n)]

for i in range(m):
    u, v = map(int, fin.readline().split())
    ans[u - 1] += 1
    ans[v - 1] += 1

for i in range(n):
    print(ans[i], end = " ", file = fout)

fin.close()
fout.close()
