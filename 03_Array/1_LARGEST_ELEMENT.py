def largest_num(arr):
    
    #to find the len of arr
    n = len(arr)#6

    #declare the largest elemnt by assuming
    largest = arr[0]

    #for travesing the array we have using the loop so we can compare each and every element
    for i in range(0,n):#0,5

        #now we put a condition to get largest element by comparing
        if arr[i] > largest:
            largest = arr[i]

    return largest






#function Definition
arr = [12, 5, 8, 21, 3, 17]

#function calling
result = (largest_num(arr))
print(result)