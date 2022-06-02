fin = open("radixsort.in")

def phase_radix_sort(array, n, m, k):
    for i in range(k):
        array = MergeSort(array, m)
        m -= 1
    return array

def merge(Left, Right, m):
    Result = []
    left_index = 0
    right_index = 0
    while left_index < len(Left) and right_index < len(Right):
        if Left[left_index][m - 1] <= Right[right_index][m - 1]:
            Result.append(Left[left_index]) 
            left_index += 1
        else:
            Result.append(Right[right_index]) 
            right_index += 1
    Result += Left[left_index:] + Right[right_index:] 
    return Result

def MergeSort(Array, m):
    if len(Array) <= 1:
        return Array 
    else:
        Left = Array[:len(Array) // 2] 
        Right = Array[len(Array) // 2:]
    return merge(MergeSort(Left, m), MergeSort(Right, m), m)

n, m, k = map(int, fin.readline().split())

array = []
for i in range(n):
    array.append(fin.readline())

array = phase_radix_sort(array, n, m, k)

with open("radixsort.out", "w") as fout:
    for element in array:
        fout.write(element+"")

