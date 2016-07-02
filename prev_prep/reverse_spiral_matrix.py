

def reverse_spiral(num):
    arr = []
    for i in range(1, num ** 2 + 1):
        arr.append(i)

    mat = [[0 for i in range(num)] for j in range(num)] 
    
    up, right = 0, 0
    left, down = num, num
    direction = 0
    index = 0 
    while True:
        if direction == 0: #going right
            for i in range(right, left):
                mat[up][i] = arr[index] 
                index += 1
            up += 1
        if direction == 1: #going down
            for i in range(up, down):
                mat[i][left - 1] = arr[index] 
                index += 1
            left -= 1
        if direction == 2: #going left
            for i in range(left - 1, right - 1, -1):
                mat[down - 1][i] = arr[index]
                index += 1
            down -= 1
        if direction == 3: #going up
            for i in range(down - 1, up - 1, -1):
                mat[i][right] = arr[index]
                index += 1
            right += 1
        if index ==  len(arr):
            break
        else:
            direction = (direction + 1) % 4

    for i in range(num):
        string = ""
        for j in range(num):
            string += str(mat[i][j])
        print string

reverse_spiral(5)

