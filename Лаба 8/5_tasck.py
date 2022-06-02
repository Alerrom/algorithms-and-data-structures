fin = open("pathbge1.in", "r")
fout = open("pathbge1.out", "w")

n, m = map(int, fin.readline().split())
E = []

for i in range(m):
    u, v = map(int, fin.readline().split())
    E.append((u - 1, v - 1))
    E.append((v - 1, u - 1))

W = dict.fromkeys(E)

for key in W:
    W[key] = 1
    
INF = 100
Distant = [INF] * n
start = 0 #Стартовая вершина
Distant[start] = 0
flag = False
k = 1

while k < n and not flag:
    k += 1
    flag = True
    for i, j in W.keys():
        if Distant[j] + W[i, j] < Distant[i]:
            Distant[i] = Distant[j] + W[i, j]
            flag = False

for distant in Distant:
    print(distant, end = " ", file = fout)

fin.close()
fout.close()
