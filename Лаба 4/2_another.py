queue = [0 for i in range(1000000)]
head_element = 0
quque_size = 0

fin = open("queue.in", "r")
fout = open("queue.out", "w")

n = int(fin.readline())
for i in range(n):
    command = fin.readline().split()
    if command[0] == '+':
        queue[quque_size] = command[1]
        quque_size += 1
        continue
    if command[0] == '-':
        print(queue[head_element], file=fout)
        head_element += 1
        continue

fout.close()
