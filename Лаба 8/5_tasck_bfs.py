fin = open("pathbge1.in", "r")
fout = open("pathbge1.out", "w")

n, m = map(int, fin.readline().split())

G = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, fin.readline().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

start = 0
prev = [None for i in range(n)]

Dist = [None for i in range(n)]
Dist[start] = 0

Q = [start]
Qstart = 0

while Qstart < len(Q):
    u = Q[Qstart]
    Qstart += 1
    for v in G[u]:
        if Dist[v] is None:
            Dist[v] = Dist[u] + 1
            prev[v] = u
            Q.append(v)

for finish in range(n):
    ans = []
    curr = finish
    while curr is not None:
        ans.append(curr)
        curr = prev[curr]
    print(len(ans) - 1, end = " ", file = fout)

fin.close()
fout.close()  

