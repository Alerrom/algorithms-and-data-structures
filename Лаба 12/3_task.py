MAX_N = 10**4

dp = [[0 for j in range(MAX_N)] for i in range(MAX_N)]

x = ' ' + input()
y = ' ' + input()

n, m = len(x) - 1, len(y) - 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if x[i] == y[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


i, j = n, m
res = ''

while i >= 1 and j >= 1:
    if x[i] == y[j]:
        res += x[i]
        i -= 1
        j -= 1
    else:
        if dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

print(res[::-1])
