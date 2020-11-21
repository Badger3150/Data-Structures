# Name: Ruoling Yu
# Student Number: 500976267
# Heap Sort

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
def heapify(arr, length, parent):
    minest = parent
    lson = parent * 2 + 1
    rson = parent * 2 + 2
    if (lson < length and arr[lson] < arr[minest]):
        minest = lson
    if (rson < length and arr[rson] < arr[minest]):
        minest = rson
    if (parent != minest):
        swap(arr, parent, minest)
        heapify(arr, length, minest)
def heapSort(arr):
    length = len(arr)
    # Make the heap
    for i in range(length // 2, -1, -1):
        heapify(arr, length, i)
    # Sort the heap
    for i in range(length - 1, 0, -1):
        swap(arr, i, 0)
        length -= 1
        heapify(arr, length, 0)

a = ['a', 'c', 'x', 'AB', 'Aa', 'Ab', 'Ca', 'aD']
heapSort(a)
print(a)
    