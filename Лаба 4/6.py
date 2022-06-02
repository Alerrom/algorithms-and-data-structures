def check(second_height, n):
    global result
    global height
    height[1] = second_height
    for i in range(2, n):
        height[i] = 2 * height[i - 1] - height[i - 2] + 2
        if height[i] < 0:
            return False
    result = height[n - 1]
    return True

def bin_search(left, right, n):
    while right - left > 0.000001:
        mid = (left + right) / 2
        if check(mid, n):
            right = mid
        else:
            left  = mid

fin = open("garland.in", "r")
fout = open("garland.out", "w")

n, A = map(float, fin.readline().split())

n = int(n)

height = [0] * n
height[0] = A
result = 0.0

bin_search(0, A, n)
print(result, file=fout)

fout.close()
