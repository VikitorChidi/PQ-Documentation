
def binary_search(numList, numTF):
    left_index = 0
    right_index = len(numList) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_num = numList[mid_index]

        if mid_num == numTF:
            return mid_index
        if mid_num < numTF:
            left_index = mid_index + 1
        else: 
            right_index = mid_index - 1
    return -1


if __name__ == '__main__':
    numList = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 32]
    numTF = 12

    value = binary_search(numList, numTF)
    print(value)