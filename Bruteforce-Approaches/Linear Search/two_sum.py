def sum_pair(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return (i, j)
    return (-1, -1)
