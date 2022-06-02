fin = open("aplusbb.in.txt")
fout = open("aplusbb.out.txt", "w")

a, b = map(int, fin.readline().split())
print(a + b * b, file=fout)

fout.close()
