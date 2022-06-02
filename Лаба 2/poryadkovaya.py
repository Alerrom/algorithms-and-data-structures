def Order_Statistics(array, kposition):
    left_index = 0
    right_index = len(array) - 1
	
    while True:
        if left_index + 1 >= right_index:
            if (left_index + 1 == right_index) and (array[left_index] > array[right_index]):
                array[left_index], array[right_index] = array[right_index], array[left_index]
            return array[kposition]
        
        middle = (left_index + right_index) // 2
        array[middle], array[left_index + 1] = array[left_index + 1], array[middle]
        if array[left_index] > array[right_index]:
            array[left_index], array[right_index] = array[right_index], array[left_index]

        if array[left_index + 1] > array[right_index]:
            array[left_index + 1], array[right_index] = array[right_index], array[left_index + 1]

        if array[left_index] > array[left_index + 1]:
            array[left_index], array[left_index + 1] = array[left_index + 1], array[left_index]

        left_flag = left_index + 1
        right_flag = right_index

        value = array[left_flag]

        while True:
            while True:
                left_flag += 1
                if (left_flag == n) or (array[left_flag] < value):
                    break
            while True:
                right_flag -= 1
                if array[right_flag] > value:
                    break
            if left_flag > right_flag:
                break
            array[left_flag], array[right_flag] = array[right_flag], array[left_flag]

        array[left_index + 1] = array[right_flag]
        array[right_flag] = value

        if right_flag >= k:
            right_index = right_flag - 1

        if right_flag <= k:
            left_index = left_flag
        
def convert(x):
    return (x + 2**31) % 2**32 - 2**31

n, k = map(int, input().split())
A, B, C, a_1, a_2 = map(int, input().split())
array = [a_1, a_2]

array = [a_1, a_2]
for i in range(2, n):
    term_1 = convert(A * array[i-2])
    term_2 = convert(B * array[i-1])
    term_3 = convert(term_1 + term_2)
    array.append(convert(term_3 + C))

print(Order_Statistics(array, k - 1))
