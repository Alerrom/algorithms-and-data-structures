fin = open("kth.in")
fout = open("kth.out", "w")

def quicksort(nums, fst, lst, k):
   if fst >= lst: 
       return 
   i, j = fst, lst
   pivot = nums[(fst + lst) // 2]
   while i <= j:
       while nums[i] < pivot:
           i += 1
       while nums[j] > pivot:
           j -= 1
       if i <= j:
           nums[i], nums[j] = nums[j], nums[i]
           i, j = i + 1, j - 1
   if k <= j:
       lst = j
   else:
       fst = i + 1
   quicksort(nums, fst, j, k)
   quicksort(nums, i, lst, k)
   
n, k = map(int, fin.readline().split())
A, B, C, a_1, a_2 = map(int, fin.readline().split())
   
array = [a_1, a_2]
for i in range(2, n):
    array.append((A * array[-2] + B * array[i - 1] + C +2**31) % 2**32 - 2**31)
    
quicksort(array, 0, n - 1, k - 1)

print(array[k-1], file=fout)

fout.close()


