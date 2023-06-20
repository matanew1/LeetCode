def binary_search(arr, start, end, target):
    median = (start + end ) // 2
    check = arr[median]

    if check == target:
        return median
    elif check > target:
        return binary_search(arr,start,median, target)
    else:
        return binary_search(arr,median+1, end, target)


arr = [1, 2, 3, 4, 5]
target = 4
print('index at',binary_search(arr,0, len(arr) - 1, target))