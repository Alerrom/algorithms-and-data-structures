stack = []

fin = open("postfix.in", "r")
fout = open("postfix.out", "w")

n = fin.readline().split()
for command in n:
    if command not in '+-*':
        stack.append(int(command))
        continue
    op2 = stack.pop()
    op1 = stack.pop()
    if command == '-':
        res = op1 - op2
        stack.append(res)
        continue
    if command == '+':
        res = op1 + op2
        stack.append(res)
        continue
    if command == '*':
        res = op1 * op2
        stack.append(res)
        continue
    
print(stack[0], file=fout)
fout.close()
