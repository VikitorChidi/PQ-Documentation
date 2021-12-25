def bubble_sort(elements):
    size = len(elements)

    # The first for loop repeats the process and the second for loop compares elements in the position
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = ['zain', 'glo', 'mtn', 'chidi', 'victor', 'agbaeze']

    bubble_sort(elements)
    print(elements)
