def countodd(arr): 


    count = 0

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            count = count + 1
        
    return count


arr = [12,5,8,21,3,27]
result = countodd(arr)
print(result)
