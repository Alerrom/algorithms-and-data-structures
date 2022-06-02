fout = open("brackets.out", "w")

def is_right(string):
    stack = []
    stack_size = 0
    for i in string:
        if i in '([':
            stack.append(i)
            stack_size += 1
        elif i in ')]':
            if stack_size == 0:
                return False
            compare = stack.pop()
            if compare == '[' and i == ']':
                stack_size -= 1
                continue
            elif compare == '(' and i == ')':
                stack_size -= 1
                continue
            else:
                return False
    if stack_size != 0:
        return False
    return True
    
with open("brackets.in") as f:
    for line in f:
        if line != '\n':
            if is_right(line):
                print('YES', file=fout)
            else:
                print('NO', file=fout)
             
fout.close()
