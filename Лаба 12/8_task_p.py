def f(i, j):
    global dp, s
    if (i > j):
        return 0
 
    if (i == j):
        dp[i][j] = 1
 
    if dp[i][j] == -1:
        if s[i] == s[j]:
            dp[i][j] = f(i + 1, j) + f(i, j - 1) + 1
        else:
            dp[i][j] = f(i + 1, j) + f(i, j - 1) - f(i + 1, j - 1)
    return (dp[i][j] + 1000000000) % 1000000000
 

N = int(input())
dp = [[-1 for i in range(N)] for j in range(N)]
s = input().split()

print(f(0, N - 1))