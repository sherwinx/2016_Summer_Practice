print "Input : [1,2,2,3,3,4]"
print "Expected output: [1,2,3,4]"

inputArr = [1,2,2,3,3,4]

index = 0

for i in range(1, len(inputArr)):
    if inputArr[index] != inputArr[i]:
        index += 1
        inputArr[index] = inputArr[i]
    length = index + 1
           
print "Output:" 
print inputArr[:length]
