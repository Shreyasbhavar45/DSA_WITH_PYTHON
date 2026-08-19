def sumOfElement(arr):
     
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]

    return total

arr = [1,2,3,4,5]
result = sumOfElement(arr)
print(result)