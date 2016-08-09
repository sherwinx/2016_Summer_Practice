nums = [1]

def singleNumber(nums):
    x = 0
    for i in range(len(nums)):
        x ^= nums[i]
    return x
print singleNumber(nums)
