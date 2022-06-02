fin = open("pathmgep.in", "r")
fout = open("pathmgep.out", "w")

import heapq

INF = 10 ** 9

n, s, f = map(int, fin.readline().split())

s -= 1
f -= 1

G = []
ans = []

for i in range(n):
    ans.append(INF)
    
    g_i = list(map(int, fin.readline().split()))
    G.append(g_i)

Q = []
heapq.heappush(Q, (0, s))

while len(Q) != 0:
    tmp = heapq.heappop(Q)

    dst = tmp[0]
    cur = tmp[1]

    if ans[cur] < dst:
        continue

    for i in range(n):
        if G[cur][i] == -1:
            continue

        n_dst = dst + G[cur][i]

        if n_dst < ans[i]:
            ans[i] = n_dst
            heapq.heappush(Q, (n_dst, i))

print(-1 if ans[f] == INF else ans[f], file=fout)

fin.close()
fout.close()
