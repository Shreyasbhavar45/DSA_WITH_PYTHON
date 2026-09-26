# ## lower Bound :- Smallest index such that nums[i] >= target


# def LowerBound(nums,target):

#     n = len(nums)

#     lowerBound = n

#     low = 0

#     high = n - 1

#     while low <= high:

#         mid = low + (high - low)//2

#         if nums[mid] >= target:
            
#             lowerBound = mid

#             high = mid - 1

#         else:

#             low = mid + 1

#     return lowerBound


# nums = [1,1,1,2,2,3,3,4,5,6]

# target = 1

# result = LowerBound(nums,target)

# print('The Lower Bound is :-',result)



### 

def LowerBound(nums,target):

    n = len(nums)

    lowerb = n

    left = 0
    right = n - 1

    while left <= right:

        mid = left + (right - left)//2

        if nums[mid] >= target:
            lowerb = mid

            right = mid - 1

        else:
            left = mid + 1

    
    return lowerb


nums = [1,2,2,3,4,4]
target = 2
result = LowerBound(nums,target)
print(result)