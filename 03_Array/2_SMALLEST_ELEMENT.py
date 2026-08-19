def minimum(arr):

    smallest = arr[0]

    for i in range(len(arr)):

        if arr[i] < smallest:
            smallest = arr[i]

    return smallest

arr = [12, 5, 8, 21, 3, 17]
result = minimum(arr)
print(result)