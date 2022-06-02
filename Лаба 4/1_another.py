stack = [0 for i in range(1000000)]
stack_top = 0
last_ind = 0

fin = open("stack.in", "r")
fout = open("stack.out", "w")

n = int(fin.readline())
for i in range(n):
    command = fin.readline().split()
    if command[0] == '+':
        stack[stack_top] = command[1]
        stack_top += 1
        continue
    if command[0] == '-':
        stack_top -= 1
        print(stack[stack_top], file=fout)
        continue

fout.close()
