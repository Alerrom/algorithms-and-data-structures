fin = open("components.in", "r")
fout = open("components.out", "w")

def dfs(start, visited, prev, V):
    visited[start] = True
    for v in V[start]:
        if not visited[v]:
            prev[v] = start
            dfs(v, visited, prev, V)


n, m = map(int, fin.readline().split())


V = [[] for i in range(n)]
for i in range(m):
    b_i, e_i = map(int, fin.readline().split())
    V[b_i - 1].append(e_i - 1)
    V[e_i - 1].append(b_i - 1)


visited = [False for i in range(n)]
ans = [None for i in range(n)]

ncomp = 0
for i in range(n):
    prev = [None for i in range(n)]
    if not visited[i]:
        ncomp += 1
        dfs(i, visited, prev, V)

    for j in range(n):
        if visited[j] and (prev[j] != None):
            ans[j] = ncomp

k = ncomp
for i in range(n - 1, -1, -1):
    if ans[i] == None:
        ans[i] = k
        k -= 1


print(ncomp, file=fout)
for i in range(n):
    print(ans[i], end = " ", file=fout)
#print(' '.join([str(i) for i in ans]), file=fout)

fin.close()
fout.close()
