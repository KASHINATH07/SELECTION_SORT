def selection_sort(array):

    for step in range(len(array)):
        min_index = step

        for i in range(step + 1, len(array)):
            if array[i] < array[min_index]:
                min_index = i

        (array[step], array[min_index]) = (array[min_index], array[step])
    return array


array = [19, 23, 46, 1, 7, 6]
print(selection_sort(array))
