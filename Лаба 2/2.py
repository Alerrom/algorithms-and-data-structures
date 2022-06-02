from collections import defaultdict

fin = open("race.in.txt")
fout = open("race.out.txt", "w")

def merge(Left, Right):
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
Dictionary = defaultdict(list)

for i in range(n):
    country, runner = fin.readline().split(' ')
    Dictionary[country].append(runner)

ListKeys = list(Dictionary.keys())
ListKeys = MergeSort(ListKeys)

for country in ListKeys:
    print('===', country, '===', file = fout)
    for runner in Dictionary[country]:
        print(runner[:len(runner)-1], file = fout)

fout.close()
