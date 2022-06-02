fin = open("prefix.in", "r")
fout = open("prefix.out", "w")

s = fin.readline().rstrip('\n')

pi = [0] * len(s)

for i in range(1, len(s)):
    j = pi[i - 1]
    
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]

    if s[i] == s[j]:
        pi[i] = j + 1
    else:
        pi[i] = j


print(' '.join([str(i) for i in pi]), file=fout)

fin.close()
fout.close()

