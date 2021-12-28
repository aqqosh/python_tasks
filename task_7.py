# var 1
nums = [0,1,2,2,3,0,4,2]
val = 2

while val in nums:
    nums.remove(val)
      
# var 2
nums = [0,1,2,2,3,0,4,2]
val = 2

size = len(nums)
others_idx, target_idx = 0, size-1

while others_idx <= target_idx:
    if nums[others_idx] == val:
        nums[others_idx], nums[target_idx] = nums[target_idx], nums[others_idx]
        target_idx -= 1
    else:
        others_idx += 1
        
nums