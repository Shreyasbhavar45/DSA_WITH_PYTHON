#UpperBound :- smallest index such that nums[i] > target:


def UpperBound(nums,target):

    n = len(nums)

    low = 0

    high = n - 1

    while low < high:

        mid = low + (high - low)//2

        if nums[mid] > target:

            high = mid

        else:

            low = mid + 1

    return low


nums = [1,1,1,2,2,3,3,4,5,6]

target = 2

result = UpperBound(nums,target)

print('The Upper Bound is :-',result)