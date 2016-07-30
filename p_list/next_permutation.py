nums = [3,2,1]


def nextPermutation(nums):
    i = -1
    firstNum, firstIndex, secondIndex = -1, -1, -1
    # find first num from right to left
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            firstIndex = i - 1
            break
    # if nums is the largest permutation
    if firstIndex == -1:
        #reverse the list
        start = 0
        end = len(nums) - 1
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return 
    
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[firstIndex]:
            secondIndex = i
            break

    temp = nums[firstIndex]
    nums[firstIndex] = nums[secondIndex]
    nums[secondIndex] = temp
    
    start = firstIndex + 1
    end = len(nums) - 1
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1
    return

nextPermutation(nums)
print nums
