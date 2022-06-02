def h(x):
    return abs(int(x) % 100043)

l = [None for i in range(100043)]

fin = open('set.in')
fout = open('set.out', "w")

command = fin.readline().split()
while command:
    if command[0] == 'insert':
        if l[h(command[1])] == None:
            l[h(command[1])] = []
        if command[1] not in l[h(command[1])]:
            l[h(command[1])].append(command[1])
    elif command[0] == 'delete':
        if l[h(command[1])] != None and command[1] in l[h(command[1])]:
            #l[h(command[1])].pop(l[h(command[1])].index(command[1]))
            del l[h(command[1])][l[h(command[1])].index(command[1])]
    elif command[0] == 'exists':
        if l[h(command[1])] == None or command[1] not in l[h(command[1])]:
            print('false', file = fout)
        else:
            print('true', file = fout)
    command = fin.readline().split()

fin.close()
fout.close()



