fin = open("search2.in", "r")
fout = open("search2.out", "w")

def z_func(s):
    n = len(s)
    zf = [0] * n
    l = 0
    r = 0
    for i in range(1, n):
        zf[i] = max(0, min(r - i, zf[i - l]))
        while i + zf[i] < n and s[zf[i]] == s[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > r:
            l = i
            r = i + zf[i]
    return zf

p = fin.readline().rstrip('\n')
t = fin.readline().rstrip('\n')
m = len(p)
n = len(t)

s = p + '#' + t
zf = z_func(s)

ans = []

for i in range(m + 1, n + 2):
    if zf[i] == m:
        ans.append(i - m)

print(len(ans), file=fout)
print(" ".join([str(i) for i in ans]), file=fout)

fin.close()
fout.close()
