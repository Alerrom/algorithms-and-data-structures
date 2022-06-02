fin = open("race.in")
fout = open("race.out", "w")

def merge(Left, Right):
    Result = []
    left_index = 0
    right_index = 0
    while left_index < len(Left) and right_index < len(Right):
        if Left[left_index][0] <= Right[right_index][0]:
            Result.append(Left[left_index]) 
            left_index += 1
        else:
            Result.append(Right[right_index]) 
            right_index += 1
    Result += Left[left_index:] + Right[right_index:] 
    return Result

def MergeSort(Array):
    if len(Array) <= 1:
        return Array 
    else:
        Left = Array[:len(Array) // 2] 
        Right = Array[len(Array) // 2:]
    return merge(MergeSort(Left), MergeSort(Right))

n = int(fin.readline())
array = []
for i in range(n):
    array.append(fin.readline().split())

array = MergeSort(array)

tmp = ''
for i in range(n):
    country = array[i][0]
    runner = array[i][1]
    if tmp != country:
        print('===', array[i][0], '===', file = fout)
        tmp = country
    print(array[i][1], file = fout)
    
fout.close()
