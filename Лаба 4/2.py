queue = []

fin = open("queue.in", "r")
fout = open("queue.out", "w")

n = int(fin.readline())
for i in range(n):
    command = fin.readline().split()
    if command[0] == '+':
        queue.append(command[1])
        continue
    if command[0] == '-':
        print(queue.pop(0), file=fout)
        continue

fout.close()
