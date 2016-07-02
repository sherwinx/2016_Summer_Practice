print "Input: [1,2,2,2,3,3,3,4,4]"
print "Expected Output: [1,2,2,3,3,4,4]"

num = [1,2,2,2,3,3,3,4,4]
maxNum = 2
def removeDuplicateII(num, maxNum):
    index = 0
    counter = 1
    for i in range(1, len(num)):
        if num[index] != num[i]:
            index += 1
            num[index] = num[i]
            # Reset the counter
            counter = 1 
        else:
            counter += 1
            if counter <= maxNum:
                index += 1
                num[index] = num[i]
    length = index + 1
    return num[:length]

print "Output:"
print removeDuplicateII(num, maxNum)
                 
