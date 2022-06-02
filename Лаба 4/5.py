def bin_search_upper(array, len_mas, element):
    left = -1
    right = len_mas
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] > element:
            right = middle
        else:
            left = middle
    if array[right - 1] == element:
        return right
    else:
        return -1

def bin_search_lower(array, len_mas, element):
    left = -1
    right = len_mas
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] >= element:
            right = middle
        else:
            left = middle
    if -1 < right < len_mas and array[right] == element:
        return right + 1
    else:
        return -1 

fin = open("binsearch.in", "r")
fout = open("binsearch.out", "w")

n = int(fin.readline())
mas = list(map(int, fin.readline().split()))

k = int(fin.readline())
elements = list(map(int, fin.readline().split()))

for i in elements:
    print(bin_search_lower(mas, n, i), bin_search_upper(mas, n, i), file=fout)
    
fout.close()
