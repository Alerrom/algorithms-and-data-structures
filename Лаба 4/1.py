stack = []

fin = open("stack.in", "r")
fout = open("stack.out", "w")

n = int(fin.readline())
for i in range(n):
    command = fin.readline().split()
    if command[0] == '+':
        stack.append(command[1])
        continue
    if command[0] == '-':
        print(stack.pop(), file=fout)
        continue

fout.close()
