def binary_search_recursive(numbers_list,number_to_find,left_index,right_index):
    if right_index < left_index:
        return -1
    mid_index = left_index + (right_index-left_index)//2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    if number_to_find == numbers_list[mid_index]:
        return mid_index
    if number_to_find > numbers_list[mid_index]:
        left_index = mid_index+1
    else:
        right_index = mid_index - 1 
    return binary_search_recursive(numbers_list,number_to_find,left_index,right_index)        




if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 10

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")    