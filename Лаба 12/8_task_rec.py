n = int(input())
tmp = input()
s = ''
for i in tmp:
    if i != ' ':
        s += i

dp = [[-1 for j in range(n)] for i in range(n)]

def f(i, j):
    global dp, s
    
    if i > j:
        return 0

    if i == j:
        dp[i][j] = 1
        return

    if dp[i][j] != -1:
        return dp[i][j]

    if s[i] == s[j]:
        dp[i][j] = f(i + 1, j) + f(i, j - 1) + 1
    else:
        dp[i][j] = f(i + 1, j) + f(i, j - 1) - f(i + 1, j - 1)

    return dp[i][j]


print(f(0, n - 1))
