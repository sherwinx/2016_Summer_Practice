#jmyList = [4,5,6,7,0,1,2]

#myList = [4,5,6,0,1,2,3]
myList = [4,5,6,7,8,1,2,3]
def searchRotated(num, myList):
    start = 0
    end = len(myList) - 1
    while start != end and end >= 0 and start >= 0:  
        ##whether it's monotonically increse, no matter the whole thing is rotated or not
        mid = (start + end) / 2
        if num == myList[mid]:
            return mid
        if myList[mid] >= myList[start]:
            if myList[mid] >= num and num >= myList[start]:
                end = mid
            else:
                start = mid + 1
        else:
             if myList[mid] < num and num <= myList[end]:
                 start = mid + 1
             else:
                 end = mid
    if myList[start] == num:
        return start 
    else:
        return -1

print searchRotated(8, myList)

