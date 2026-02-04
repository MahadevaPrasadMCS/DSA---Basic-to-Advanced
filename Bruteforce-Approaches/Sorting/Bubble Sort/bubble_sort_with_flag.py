def bubble_sort_with_flag(arr):
    swaps = False
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps = True
        if swaps == False:
                return arr
        swaps = False
            
print(bubble_sort_with_flag([3, 1, 2]))
