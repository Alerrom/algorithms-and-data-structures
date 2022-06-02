#fin = open("antiqs.in")
#fout = open("antiqs.out", "w")

#n = int(fin.readline())
n = int(input())
anti_qsort_array = [i+1 for i in range(n)]
print(*anti_qsort_array)
for i in range(2, n):
    anti_qsort_array[i], anti_qsort_array[i//2] = anti_qsort_array[i//2], anti_qsort_array[i]
    print(i, i//2)
    print(*anti_qsort_array)
#print(' '.join([str(i) for i in anti_qsort_array]), file=fout)

#fout.close()
