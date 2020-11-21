# Name: Ruoling Yu
# Student Number: 500976267
# Insertion Sort
def insertionSort(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return(arr)

print(insertionSort(['a', 'c', 'x', 'AB', 'Aa', 'Ab', 'Ca', 'aD']))
        
