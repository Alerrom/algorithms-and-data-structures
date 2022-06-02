n, m = map(int, input().split())
G = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)

visited = [False for i in range(n)]
ans = []
