fin = open("knapsack.in", "r")
fout = open("knapsack.out", "w")

s, n = map(int, fin.readline().split())
data = list(map(int, fin.readline().split()))

all_w = [1] + [0] * s

for el in data:
    for j in range(s, el - 1, -1):
        if all_w[j - el] == 1:
            all_w[j] = 1

m_w = s
while all_w[m_w] != 1:
    m_w -= 1



print(m_w, file=fout)

fin.close()
fout.close()

