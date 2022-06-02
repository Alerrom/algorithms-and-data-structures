from collections import deque

def jump(label):
    for i in range(l):
        if labels[i][0] == label:
            return labels[i][1]

commands = []
registers = [0] * 26
labels = []
quack = deque()

mod = 65536
run = True
n = 0
l = 0
reg = ''
        
fin = open('quack.in')
fout = open('quack.out', "w")

line = fin.readline()
while line:
    commands.append(line)
    line = fin.readline()
    n += 1

for i in range(n):
    if commands[i][0] == ':':
        labels.append([commands[i][1:], i])
        l += 1
        
i = 0
while i < n:
    com = commands[i]
    
    if com[0] == '+':
        a = quack.popleft()
        b = quack.popleft()
        x = (a + b) & (mod - 1)
        quack.append(x)
        
    elif com[0] == '-':
        a = quack.popleft()
        b = quack.popleft()
        x = (a - b) & (mod - 1)
        quack.append(x)
        
    elif com[0] == '*':
        a = quack.popleft()
        b = quack.popleft()
        x = (a * b) & (mod - 1)
        quack.append(x)
        
    elif com[0] == '/':
        a = quack.popleft()
        b = quack.popleft()
        if not b:
            x = 0
        else:
            x = (a // b) & (mod - 1)
        quack.append(x)
        
    elif com[0] == '%':
        a = quack.popleft()
        b = quack.popleft()
        if not b:
            x = 0
        else:
            x = (a % b) & (mod - 1)
        quack.append(x)
        
    elif com[0] == '>':
        reg = com[1]
        x = quack.popleft()
        registers[ord(reg) - ord('a')] = x
        
    elif com[0] == '<':
        reg = com[1]
        x = registers[ord(reg) - ord('a')]
        quack.append(x)
        
    elif com == 'P':
        if len(com) == 1:
            x = quack.popleft()
        else:
            reg = com[1]
            x = registers[ord(reg) - ord('a')]
        print(x, file = fout)
        
    elif com[0] == 'C':
        if len(com) == 1:
            x = quack.popleft()
        else:
            reg = com[1]
            x = registers[ord(reg) - ord('a')]
        print(str(x % 256), file = fout)
        
    elif com[0] == ':':
        None
        
    elif com[0] == 'J':
        label = commands[i][1:]
        i = jump(label)

    elif com[0] == 'Z':
        reg = com[1]
        label = commands[i][2:]
        if not registers[ord(reg) - ord('a')]:
            i = jump(label)
            
    elif com[0] == 'E':
        label = commands[i][3:]
        if registers[ord(com[1]) - ord('a')] == registers[ord(com[2]) - ord('a')]:
            i = jump(label)

    elif com[0] == 'G':
        label = commands[i][3:]
        if registers[ord(com[1]) - ord('a')] > registers[ord(com[2]) - ord('a')]:
            i = jump(label)
            
    elif com[0] == 'Q':
        run = False

    else:
        if com[:-1].isdigit():
            x = int(com[:-1])
            quack.append(x)
    if i == None:
        print(i)
    print(i)
    i += 1
    if not run:
        break

fin.close()
fout.close()
