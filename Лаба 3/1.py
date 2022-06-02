fin = open("isheap.in")
fout = open("isheap.out", "w")

n = int(fin.readline())
heap = ['']
tmp = fin.readline().split()
for el in tmp:
    heap.append(int(el))

flag = False
for i in range(n, 2, -1):
    parent = round(i / 2 - 0.49)
    if heap[i] <= heap[parent]:
        flag = True
    else:
        flag = False
        break

if flag:
    print('YES', file=fout)
else:
    print('NO', file=fout)
