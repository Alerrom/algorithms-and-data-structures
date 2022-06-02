fin = open("inversions.in")
fout = open("inversions.out", "w")

def merge(Left, Right):
    global inversions_counter
    Result = []
    left_index = 0
    right_index = 0
    while left_index < len(Left) and right_index < len(Right):
        if Left[left_index] <= Right[right_index]:
            Result.append(Left[left_index]) 
            left_index += 1
        else:
            Result.append(Right[right_index]) 
            right_index += 1
            inversions_counter += len(Left) - left_index
    Result += Left[left_index:] + Right[right_index:] 
    return Result

def MergeSort(Array):
    if len(Array) <= 1:
        return Array 
    else:
        Left = Array[:len(Array) // 2] 
        Right = Array[len(Array) // 2:]
    return merge(MergeSort(Left), MergeSort(Right))

inversions_counter = 0

n = int(fin.readline())
array = list(map(int, fin.readline().split()))
array = MergeSort(array)

print(inversions_counter, file=fout)

fout.close()
