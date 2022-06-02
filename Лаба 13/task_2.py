fin = open("search2.in", "r")
fout = open("search2.out", "w")

p = fin.readline().rstrip('\n')
t = fin.readline().rstrip('\n')
ans = []

n = len(t)
m = len(p)

for i in range(n-m+1):
    flag = True
    for j in range(m):
        if t[i + j] != p[j]:
            flag = False
            break
    if flag:
        ans.append(i + 1)

print(len(ans), file=fout)
print(*ans, file=fout)

fin.close()
fout.close()
