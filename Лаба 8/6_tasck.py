fin = open("input.txt", "r")
fout = open("output.txt", "w")

n, m = map(int, fin.readline().split())
a = []
A = []
w = [[] for i in range(n*m)]

for i in range(n):
    a.append(fin.readline())
    
for i in range(n):
    for j in range(m):
        if a[i][j] != '#':
            if a[i][j] == 'S':
                start = m*i+j
            elif a[i][j] == 'T':
                end = m*i+j
            if -1 < i - 1 < n and a[i-1][j] != '#':
                A.append((m*i+j, m*(i-1)+j))
                A.append((m*(i-1)+j, m*i+j))
                w[m*i+j].append(m*(i-1)+j)
                w[m*(i-1)+j].append(m*i+j)
            if -1 < j - 1 < m and a[i][j-1] != '#':
                A.append((m*i+j, m*i+j-1))
                A.append((m*i+j-1, m*i+j))
                w[m*i+j].append(m*i+j-1)
                w[m*i+j-1].append(m*i+j)


weight = dict.fromkeys(A)

for key in weight:
    weight[key] = 1

N = n*m

INF = 100
dist = [INF] * N
dist[start] = 0
prev = [None] * N
used = [False] * N

min_dist = 0
min_vertex = start

while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in w[i]:
        if dist[i] + weight[i, j] < dist[j]:
            dist[j] = weight[i, j] + dist[i]
            prev[j] = i
    min_dist = INF
    for i in range(N):
        if not used[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_vertex = i

path = []
path_len = -1
j = end
while j is not None:
    path.append(j) 
    j = prev[j]
    path_len += 1
path = path[::-1]

if path_len > 0:
    print(path_len, file=fout)
    for i in range(1, path_len + 1):
        if path[i] - path[i - 1] == m:
            print('D', end = '', file=fout)
        elif path[i] - path[i - 1] == -m:
            print('U', end = '', file=fout)
        elif path[i] - path[i - 1] == 1:
            print('R', end = '', file=fout)
        elif path[i] - path[i - 1] == -1:
            print('L', end = '', file=fout)
else:
    print(-1, file=fout)

fin.close()
fout.close()

