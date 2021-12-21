def removeDuplicates(nums):

    i = 0
    j = 1

    while j < len(nums):
        if nums[i] == nums[j]:
            del nums[i]
        else:
            i += 1
            j += 1
            
    return len(nums)

nums = [1, 1, 2, 2, 2, 2, 5, 5, 6, 7, 8, 9, 9, 9]
removeDuplicates(nums)