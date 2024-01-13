def binary_search(number_list,number_to_find):
    left_index = 0
    right_index = len(number_list)-1
    mid =0

    while right_index >= left_index:
        mid = left_index + (right_index-left_index)//2
        # mid = (left_index + right_index) // 2

        if number_list[mid] == number_to_find:
            return mid
        if number_to_find > number_list[mid]:
            left_index = mid+1

        else:
            right_index= mid-1
    return -1

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 12 

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")        
