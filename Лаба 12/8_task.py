n = int(input())
s = list(map(int, input().split()))

dp = [[-1 for j in range(n)] for i in range(n)]

'''
for l in range(1, n):
    for i in range(n):
        j = i + l

        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1
        else:
            dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
'''

def f(n, i, j, arr):
    global s
    
    if i > j:
        return 0

    if i == j:
        arr[i][j] = 1
        return

    if arr[i][j] == -1:
        if s[i] == s[j]:
            arr[i][j] = f(n, i + 1, j, arr) + f(n, i, j - 1, arr) + 1
        else:
            arr[i][j] = f(n, i + 1, j, arr) + f(n, i, j - 1, arr) - f(n, i + 1, j - 1, arr)

    return arr[i][j]


print(f(n, 0, n - 1, dp))
