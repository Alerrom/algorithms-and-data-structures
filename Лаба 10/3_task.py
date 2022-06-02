fin = open("spantree3.in", "r")
fout = open("spantree3.out", "w")

import heapq

n, m = map(int, fin.readline().split())

ans = 0

Q = []
G = [[] for i in range(n)]
used = [False for i in range(n)]

for i in range(m):
    u, v, w = map(int, fin.readline().split())
    G[u - 1].append((v - 1, w))
    G[v - 1].append((u - 1, w))


heapq.heappush(Q, (0, 0))

while len(Q) != 0:
    temp = heapq.heappop(Q)
    
    dst = temp[0]
    cur = temp[1]

    if used[cur]:
        continue

    used[cur] = True
    ans += dst

    for foll in G[cur]:
        if not used[foll[0]]:
            heapq.heappush(Q, (foll[1], foll[0]))


print(ans, file=fout)
    

fin.close()
fout.close()
