def Sort(array, length):
    for x in range(length):
        min_index = x
        for y in range(x+1, length):
            if array[y] < array[min_index]:
                min_index = y
        array[x], array[min_index] = array[min_index], array[x]
    return array