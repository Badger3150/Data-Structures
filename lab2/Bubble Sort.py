def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def bubbleSort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if (arr[j] < arr[j + 1]):
                swap(arr, j, j + 1)
    return(arr)


print(bubbleSort(['a', 'c', 'x', 'AB', 'Aa', 'Ab', 'Ca', 'aD']))
