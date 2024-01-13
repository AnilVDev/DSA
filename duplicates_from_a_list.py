def repeat(arr):
    size = len(arr)
    repeat = []
    for i in range(size):
        for j in range(i+1,size):
            if arr[i] == arr[j] and arr[i] not in repeat:
                repeat.append(arr[i])
    return repeat

list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print (repeat(list1))
     