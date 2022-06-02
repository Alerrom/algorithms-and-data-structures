'''def decrease_key(heap, key, x):
    i = 0
    i = binary_search(heap, 0, len(heap) - 1, key)
    heap[i][0] = x
    heap_sort(heap)

def binary_search(arr, low, high, x): 
    mid = (high + low) // 2
    if arr[mid][1] == x: 
        return mid 
    elif arr[mid][1] > x: 
        return binary_search(arr, low, mid - 1, x)  
    else: 
        return binary_search(arr, mid + 1, high, x)   


def push(heap, x, key):
    heap.append([x, key])
    heap_sort(heap)
    
def extract_min(heap):
    if len(heap) < 1:
        return '*'
    return heap.pop(0)[0]
        
def heapify(heap, heap_size, root_index):
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2
    
    if left < heap_size and heap[root_index][0] < heap[left][0]:
        largest = left

    if right < heap_size and heap[largest][0] < heap[right][0]:
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
        heapify(heap, i, 0)'''

def push(heap, x):
    global size
    heap.append(x)
    size += 1

def decrease_key(heap, key, x):
    heap[key - 1] = x

def extract_min(heap):
    global flag
    global size
    if flag == size:
        return '*'
    else:
        flag += 1
        i_tmp = 0
        tmp = heap[i_tmp]
        for i in range(size):
            if tmp > heap[i]:
                tmp = heap[i]
                i_tmp = i
        heap[i_tmp] = 10**9 + 5
        return tmp

fout = open("priorityqueue.out", "w")
heap = []
#key = 1
flag = 0
size = 0

with open("priorityqueue.in") as f:
    for line in f:
        if line == '\n':
            continue
        command = line.split()
        if line == '\n':
            continue
        if command[0] == 'push':
            x = int(command[1])
            push(heap, x)
            '''push(heap, x, key)
            key += 1'''
            continue
        if command[0] == 'extract-min':
            print(extract_min(heap), file=fout)
            continue
        if command[0] == 'decrease-key':
            key = int(command[1])
            x = int(command[2])
            decrease_key(heap, key, x)
        
fout.close()
