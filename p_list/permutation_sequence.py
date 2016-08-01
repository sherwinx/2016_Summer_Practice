import math

def permutationSequence(n, k):
    k -= 1
    nums = range(1, n + 1)
    base = math.factorial(n - 1)
    i = n - 1
    result = ""
    while i > 0:
       index = k / base
       k %= base
       base /= i
       i -= 1
       num = nums[index]
       result += str(num)
       nums.remove(num)
    result += str(nums[0])
    print result 



permutationSequence(4,4)

#1234 0 0  0 0
#1243 0 1  0 1
#1324 0 2  1 0
#1342 0 3  1 1
#1423 0 4  2 0
#1432 0 5  2 1
#2134 1 0
#2143 1 1
#2314 1 2
#2341 1 3
#2413 1 4
#2431 1 5
#3124 2 0
#3142
#3214
#3241
#3412
#3421
#4123
#4132
#4213
#4231
#4312
#4321

