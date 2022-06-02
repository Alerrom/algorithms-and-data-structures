n = int(input())
a = list(map(int, input().split()))


prev = [0] * (n)
d = [0] * (n)

for i in range(n):
    d[i] = 1
    prev[i] = -1
    for j in range(0, i):
        if a[j] < a[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
            prev[i] = j


pos = 0
l = d[0]

for i in range(n):
    if d[i] > l:
        pos = i
        l = d[i]

ans = []
while pos != -1:
    ans.append(a[pos])
    pos = prev[pos]

print(len(ans))
print(*ans[::-1])

