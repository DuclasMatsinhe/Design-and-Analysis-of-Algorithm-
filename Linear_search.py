def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [2, 3, 4, 10, 40]
target = 10
print("Linear Search result:", linear_search(arr, target))
