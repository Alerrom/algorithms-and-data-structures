fin = open("selectw.in", "r")
fout = open("selectw.out", "w")

INF = 10**9

def max_set(curr):
    global used, g

    if used[curr] != -INF:
        return used[curr]

    ch_sum = 0;
    gch_sum = 0;

    for ch in g[curr][1]:
        ch_sum += max_set(ch)

    for ch in g[curr][1]:
        for gch in g[ch][1]:
            gch_sum += max_set(gch)

    used[curr] = max(max(g[curr][0], 0) + gch_sum, ch_sum)

    return used[curr]

n = int(fin.readline())

g = [[0, []] for i in range(n)]
used = [-INF] * n 

root = 0
for i in range(n):
    p, q = map(int, fin.readline().split())
    p -= 1

    g[i][0] = q
    
    if p == -1:
        root = i
        continue

    g[p][1].append(i)

print(max_set(root), file=fout)

fin.close()
fout.close()
