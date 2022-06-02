from bisect import bisect_right

INF = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

d = [INF] * (n+1)
pos = [0] * (n+1)
prev = [0] * (n)

l = 0

pos[0] = -1
d[0] = -INF


for i in range(n):
    j = bisect_right(d, a[i], 0, n)
    if d[j - 1] < a[i] and a[i] < d[j]:
        d[j] = a[i]
        pos[j] = i
        prev[i] = pos[j - 1]
        l = max(l, j)

ans = []
p = pos[l]

while p != -1:
    ans.append(a[p])
    p = prev[p]

print(l)
print(' '.join([str(i) for i in ans[::-1]]))
