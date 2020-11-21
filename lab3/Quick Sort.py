# Name: Ruoling Yu
# Student Number: 500976267
# Quick Sort
def quickSort(arr, i, j):
    if i >= j: return ''
    # find the first mid number
    mid = split(arr, i, j)
    # continue search the left side and right side, and the  program will continue to recursively look for the left and right parts until the sorting is complete
    quickSort(arr, i, mid - 1)
    quickSort(arr, mid + 1, j)

def split(arr, i, j):
    # choose the first element as the pivot
    pivot = arr[i]
    # if i smaller than j, continue change the large number to te left, small number to the right
    while i < j:
        # if j is samller than pivot, it means its position is correct, so we move j to the left
        while i < j and arr[j] <= pivot:
            j -= 1
        # when it leaves the while loop, we change the element in j index to the left (go to the larger part)
        arr[i] = arr[j]
        # if i is greater than pivot, it means its position is correct, so we move i to the right
        while i < j and arr[i] >= pivot:
            i += 1
        # when it leaves the while loop, we change the element in i index to the right (go to the smaller part)
        arr[j] = arr[i]
    # because finally the j and i in the same position, so we change the element to the pivot
    arr[i] = pivot
    return j
a = ['a', 'c', 'x', 'AB', 'Aa', 'Ab', 'Ca', 'aD']
quickSort(a, 0, len(a) - 1)
print(a)