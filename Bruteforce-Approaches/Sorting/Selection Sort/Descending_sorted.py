# Selection Sort for descending order

arr = [11, 25, 22, 12, 64]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] < arr[j]:
            min_index = j
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
print(arr)
