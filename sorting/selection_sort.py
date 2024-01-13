def selection_sort(arr):
    size = len(arr)
    for i in range(0,size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index],arr[i]

if __name__ == '__main__':
    elements = [89, 78, 61, 53, 23, 21, 10, 17, 12, 9, 7, 6, 2, 1]
    selection_sort(elements)
    print(elements)