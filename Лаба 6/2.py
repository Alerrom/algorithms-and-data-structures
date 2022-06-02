'''def h(x):
    res = 0
    for i in range(len(x)):
        res += ((ord(x[i]) - ord('A') + 1))*(i+1)
    return res % 100000'''

def h(x):
    p = 37
    res = 0
    p_pow = 1
    for pos in x:
        res += (ord(pos) - ord('a')) * p_pow % 20000003
        res %= 20000003
        p_pow *= p
        p_pow %= 20000003
    return res

'''def h(x):
    res = 0
    for i in x:
        res = res * 53 + ord(i)
        res %= 100003
    return res'''

m = [None] * 20000003

fin = open('map.in')
fout = open('map.out', "w")

command = fin.readline().split()
while command:
    if command[0] == 'put':
        index = h(command[1])
        if m[index] == None:
            m[index] = []
        m[index].append(command[2])
        
    elif command[0] == 'delete':
        index = h(command[1])
        m[h(command[1])] = None
        
    elif command[0] == 'get':
        index = h(command[1])
        if m[index] != None and command[1]:
            print('none', file = fout)
        else:
            print(m[h(command[1])], file = fout)
    command = fin.readline().split()

fin.close()
fout.close()



