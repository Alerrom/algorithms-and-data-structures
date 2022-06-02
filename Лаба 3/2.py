fin = open("sort.in")
fout = open("sort.out", "w")

def heapify(heap, heap_size, root_index):
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2
    
    if left < heap_size and heap[root_index] < heap[left]:
        largest = left

    if right < heap_size and heap[largest] < heap[right]:
        largest = right

    if largest != root_index:
        heap[root_index], heap[largest] = heap[largest], heap[root_index]
        heapify(heap, heap_size, largest)

def heap_sort(heap):
    n = len(heap)
    for i in range(n, -1, -1):
        heapify(heap, n, i)

    for i in range(n-1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        heapify(heap, i, 0)

n = int(fin.readline())
heap = list(map(int, fin.readline().split()))
heap_sort(heap)

print(' '.join([str(elemet) for elemet in heap]), file=fout)

fout.close()
