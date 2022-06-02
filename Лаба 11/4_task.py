fin = open("path.in", "r")
fout = open("path.out", "w")

def dfs(v):
    global used
    global G
    global dist

    if not used[v]:
        used[v] = True
        dist[v][1] = '-'
        for i in G[v]:
            dfs(i[0])

    
INF = 8 * 10**18
n, m, s = map(int, fin.readline().split())
s -= 1

G = [[] for i in range(n)]

for i in range(m):
    l, r, w = map(int, fin.readline().split())

    G[l - 1].append((r - 1, w))

used = [False] * n
dist = [[INF, ''] for i in range(n)]
dist[s][0] = 0

prev = [-1] * n

for i in range(n - 1):
    for u in range(n):
        for E in G[u]:
            v = E[0]
            w = E[1]
            
            if dist[u][0] < INF and dist[v][0] > dist[u][0] + w:
                dist[v][0] = max(dist[u][0] + w, -INF)


for u in range(n):
    for E in G[u]:
        v = E[0]
        w = E[1]
        
        if dist[u][0] < INF and dist[v][0] > dist[u][0] + w:
            dfs(v)
    

for i in range(n):
    if dist[i][1] == '-':
        print('-', file=fout)
    elif dist[i][0] == INF:
        print('*', file=fout)
    else:
        print(dist[i][0], file=fout)
        
fin.close()
fout.close()
