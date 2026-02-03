def indices(arr, target):
    first_index = -1
    last_index = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first_index == -1:
                first_index = i
            last_index = i

    return (first_index, last_index)
