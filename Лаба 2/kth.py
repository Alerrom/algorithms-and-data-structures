fin = open("kth.in")
fout = open("kth.out", "w")
 
def convert(i):
    return int(bin(i+2**32)[-32:], 10)

def partition(array, left, right, x):
    i = left
    j = right
    while i < j:
        while array[i] < x:
            i += 1
        while x < array[j]:
            j -= 1
        if i > j:
            break
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return j

def Quick_Select(array, k, left, right):
    if left == right:
        return array[left]
    x = array[(left + right) // 2]
    m = partition(array, left, right, x)
    if k <= m:
        return Quick_Select(array, k, left, m)
    else:
        return Quick_Select(array, k, m+1, right)

def convert(x):
    return (x + 2**31) % 2**32 - 2**31

n, k = map(int, input().split())
A, B, C, a_1, a_2 = map(int, input().split())
array = [a_1, a_2]

array = [a_1, a_2]
for i in range(2, n):
    term_1 = convert(A * array[i-2])
    term_2 = convert(B * array[i-1])
    term_3 = convert(term_1+term_2)
    array.append(convert(term_3 + C))

print(Quick_Select(array, k-1, 0, n-1))
 
fout.close()
