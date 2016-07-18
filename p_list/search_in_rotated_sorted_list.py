myList = [4,5,6,7,0,1,2]

def searchRotated(num, myList):
    start = 0
    end = len(myList) - 1
    while start != end:  
        mid = (start + end) / 2
        if num == myList[mid]:
            return mid
        elif num < myList[mid] and num >= myList[start]:
            end = mid - 1
        else:
            start = mid + 1
    if myList[start] == num:
        return start 
    else:
        return -1

print searchRotated(0, myList)

