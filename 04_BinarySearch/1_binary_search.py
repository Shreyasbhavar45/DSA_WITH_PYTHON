def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Input
nums = [1,2,3,4,5,6]
target = 4

result = binary_search(nums, target)

print(result)