fin = open('aplusb.in')
fout = open('aplusb.out', "w")

a, b = map(int, fin.readline().split())
print(a + b, file=fout)

fout.close()
