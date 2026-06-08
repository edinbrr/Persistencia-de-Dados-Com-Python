def bubble_sort(array):

    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:

                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


numeros = [45, 12, 78, 3, 90, 22, 1, 65, 34, 8, 50, 99, 17, 27, 5]

bubble_sort(numeros)

print(numeros)