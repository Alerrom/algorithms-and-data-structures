fin = open("kth.in")
fout = open("kth.out", "w")
  
def partition (a, l, r, x):
    i = l
    j = r
    while i < j:
        while a[i] < x:
            i += 1
        while x < a[j]:
            j -= 1
        if i > j:
            break
        a[i], a[j] = a[j], a[i]# тоже, что и swap(a[i], a[j])
        i += 1
        j -= 1
    return j

def quick_select (a, k, l, r):
    if l == r:
        return a[l]
    x = a[(l + r) // 2]
    m = partition (a, l, r, x)
    if k <= m:
        return quick_select (a, k, l, m)
    else:
        return quick_select (a, k, m + 1, r)
    
n, k = map(int, fin.readline().split())
A, B, C, a_1, a_2 = map(int, fin.readline().split())
  
array = [a_1, a_2]
for i in range(2, n):
    array.append((A * array[i-2] + B * array[i-1] + C + 2**31)% 2**32 - 2**31)

print(quick_select(array, k - 1, 0, n - 1), file=fout)

fout.close()
