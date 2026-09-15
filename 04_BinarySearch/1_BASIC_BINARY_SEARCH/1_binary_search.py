# #binary Search :- always in sorted manner

# def binarySearch(nums,target):

#     n = len(nums)

#     left = 0
#     right = n - 1

#     while left <= right:

#         mid = left + (right - left)//2

#         if nums[mid] == target:
#             return mid
        
#         elif nums[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

    
#     return -1

# nums = [1,2,3,4,5,8]
# target = 1
# result = binarySearch(nums,target)
# print(result)



##by using recursive method

def binarySearch(nums,target,left,right):

    #edge case
    if left > right:
        return -1
    
    mid = left + (right - left)//2

    if nums[mid] == target:

        return mid
    
    elif nums[mid] < target:
        
        return binarySearch(nums,target,mid+1,right)
    
    else:

        return binarySearch(nums,target,left,mid-1)
    

nums = [1,2,3,4,5,8]
left = 0
right = len(nums) - 1
target = 1
result = binarySearch(nums,target,left,right)
print(result)    