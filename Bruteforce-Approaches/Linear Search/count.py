def target_count(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count
