def max_set(curr):
    global used, g

    if used[curr] != -1:
        return used[curr]

    ch_sum = 0;
    gch_sum = 0;

    for ch in g[curr]:
        ch_sum += max_set(ch)

    for ch in g[curr]:
        for gch in g[ch]:
            gch_sum += max_set(gch)

    used[curr] = max(1 + gch_sum, ch_sum)

    return used[curr]

n = int(input())

g = [[] for i in range(n)]
used = [-1] * n 

root = 0
for i in range(n):
    p = int(input())
    p -= 1

    if p == -1:
        root = i
        continue

    g[p].append(i)

print(max_set(root))
