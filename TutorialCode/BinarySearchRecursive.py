def bsr(numList, numTF, lft_index, rgt_index):
    if rgt_index < lft_index:
        return -1

    mid_index = (lft_index + rgt_index) // 2

    if mid_index >= len(numList) or mid_index < 0:
        return -1

    mid_num = numList[mid_index]

    if mid_num == numTF:
        return mid_index

    if mid_num < numTF:
        lft_index = mid_index + 1
    else:
        rgt_index = mid_index - 1

    return bsr(numList, numTF, lft_index, rgt_index)


if __name__ == '__main__':
    numList = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 32]
    numTF = 21

    value = bsr(numList, numTF, 0, len(numList))
    print(value)
