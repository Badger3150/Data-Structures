# Selection Sort
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def findMinIndex(arr, length):
    minNumIndex = 0
    for i in range(1, length):
        if arr[i] < arr[minNumIndex]:
            minNumIndex = i
    return minNumIndex

def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        lastIndex = length - 1 - i
        minNumIndex = findMinIndex(arr, length - i)
        swap(arr, minNumIndex, lastIndex)
    return(arr)

print(selectionSort(['a', 'c', 'x', 'AB', 'Aa', 'Ab', 'Ca', 'aD']))