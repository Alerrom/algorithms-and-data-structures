fin = open("input.txt", "r")
fout = open("output.txt", "w")

n, m = map(int, fin.readline().split())
G = [[] for i in range(n * m)]

input_array = []

for i in range(n):
    input_array.append(fin.readline())
    
for i in range(n):
    for j in range(m):
        if input_array[i][j] != '#':
            if input_array[i][j] == 'S':
                start = m * i + j
            elif input_array[i][j] == 'T':
                finish = m * i + j
            if -1 < i - 1 < n and input_array[i - 1][j] != '#':
                G[m * i + j].append(m * (i - 1) + j)
                G[m * (i - 1) + j].append(m * i + j)
            if -1 < j - 1 < m and input_array[i][j - 1] != '#':
                G[m * i + j].append(m * i + j - 1)
                G[m * i + j - 1].append(m * i + j)

N = m * n
prev = [None for i in range(N)]
Dist = [None for i in range(N)]
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

path = []
path_len = -1
while finish is not None:
    path.append(finish) 
    finish = prev[finish]
    path_len += 1
path = path[::-1]

if path_len > 0:
    print(path_len, file = fout)
    for i in range(1, path_len + 1):
        if path[i] - path[i - 1] == m:
            print('D', end = '', file = fout)
        elif path[i] - path[i - 1] == -m:
            print('U', end = '', file = fout)
        elif path[i] - path[i - 1] == 1:
            print('R', end = '', file = fout)
        elif path[i] - path[i - 1] == -1:
            print('L', end = '', file = fout)
else:
    print(-1, file = fout)

fin.close()
fout.close()
