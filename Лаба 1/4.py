fin = open("smallsort.in")
fout = open("smallsort.out", "w")

n = int(fin.readline())
l = list(map(int, fin.readline().split()))

for j in range(1, n):
    key = l[j]
    i = j - 1
    while i > -1 and l[i] > key:
        l[i + 1] = l[i]
        i -= 1
    l[i + 1] = key

print(*l, file=fout)

fout.close()
