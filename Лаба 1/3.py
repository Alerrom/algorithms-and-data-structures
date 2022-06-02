fin = open("turtle.in")
fout = open("turtle.out", "w")

h, w = map(int, fin.readline().split())
field = []

for i in range(h):
    field.append(list(map(int, fin.readline().split())))

for i in range(h - 1, 0, -1):
    field[i - 1][0] += field[i][0]
for j in range(1, w):
    field[h - 1][j] += field[h - 1][j - 1]
for i in range(h-2, -1, -1):
    for j in range(1, w):
        field[i][j] += max(field[i][j - 1], field[i + 1][j])
    
print(field[0][w - 1], file=fout)

fout.close()
