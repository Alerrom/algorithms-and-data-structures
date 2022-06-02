fin = open("kth.in")
fout = open("kth.out", "w")

def k_staticstic(array, left, right, k):
    if right == 0:
        return
    if right == 1:
        return
    if left >= right:
        return
    flag = 0
    for i in range(left + 1, right + 1):
        if array[i] != array[i - 1]:
            flag = 1
            break
    if flag == 0:
        return
    pivot = array[right]
    j = left
    for i in range(left, right):
        if array[i] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
    array[right] = array[j]
    array[j] = pivot
    pivot_index = j
    j += 1
    while j <= right and array[j] == array[j - 1]:
        j += 1
    if k >= pivot_index and k <= j - 1:
        return
    if k < pivot_index:
        k_staticstic(array, left, pivot_index - 1, k)
    else:
        k_staticstic(array, j, right, k)
		    
n, k = map(int, fin.readline().split())
A, B, C, a_1, a_2 = map(int, fin.readline().split())
  
array = [a_1, a_2]
for i in range(2, n):
    array.append((A * array[i-2] + B * array[i-1] + C + 2**31)% 2**32 - 2**31)

k_staticstic(array, 0, n - 1, k - 1)

print(array[k-1], file=fout)

fout.close()
