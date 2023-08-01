import random

def create_random_array(n):
    value_arr = []
    arr = []
    for value in range(0, n*n):
        value_arr.append(value)
    for rows in range(0, n):
        row_arr = []
        for columns in range (0, n):
            random.shuffle(value_arr)
            row_arr.append(value_arr.pop())
        arr.append(row_arr)
    return arr

def rotate_array(array):
    n = len(array)
    n_offset = 0
    range_offset = 1
    while n_offset < n:
        for i in range(0, n-range_offset-n_offset): 
            dec_val = (n - i)
            inc_val = (i + 1)
            set = array[n - n + n_offset][n - dec_val + n_offset]
            temp = array[n - dec_val + n_offset][n - 1 - n_offset]
            array[n - dec_val + n_offset][n - 1 - n_offset] = set
            
            set = temp
            temp = array[n - 1 - n_offset][n - inc_val - n_offset]
            array[n - 1 - n_offset][n - inc_val - n_offset] = set
            
            set = temp
            temp = array[n - inc_val - n_offset][n - n + n_offset]
            array[n - inc_val - n_offset][n - n + n_offset] = set

            array[n - n + n_offset][n - dec_val + n_offset] = temp
        range_offset = range_offset + 1
        n_offset = n_offset + 1
    return arr

n = 7
arr = create_random_array(n)
print("Array prior to rotation")
for value in arr:
    print(value)
arr = rotate_array(arr)
print("\n" + "Array after to rotation")
for value in arr:
    print(value)
print("Test")