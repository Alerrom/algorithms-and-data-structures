from bisect import bisect_left

INF = 10**9 + 1

n = int(input())
v = list(map(int, input().split()))
 
tail = [-INF for i in range(n + 1)]
length = 1  
 
tail[0] = v[0]
 
for i in range(1, n):
    if v[i] > tail[length - 1]:
        tail[length] = v[i]
        length += 1
 
    else:
        tail[bisect_left(tail, v[i], 0, length - 1)] = v[i]


print(length)
print(' '.join([str(i) for i in tail[:length]]))

