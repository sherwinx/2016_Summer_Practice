nums = 0

def climbStairs(nums):
    if nums == 0:
        return 0
    a = b = 1
    for i in range(1, nums):
        a, b = b , a + b
    return b
print climbStairs(nums)
