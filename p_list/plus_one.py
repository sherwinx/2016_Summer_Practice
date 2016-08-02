nums = []



def plusOne(nums):
    if len(nums) == 0:
        return [1]
    origiLength = len(nums)
    numLength = len(nums) - 1
    while True:
        nums[numLength] += 1
        if nums[numLength] != 10:
            break
        nums[numLength] = 0
        numLength -= 1
        if numLength < 0:
            newList = [1]
            return newList + [0] * origiLength
    return nums


print plusOne(nums)
