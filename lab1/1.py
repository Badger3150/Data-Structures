def switchHalf(arr):
    length = len(arr)
    halfPos = length // 2
    preHalf = arr[:halfPos]
    nextHalf = arr[halfPos:]
    print("The average of previous half is {:.2f}".format(average(preHalf)))
    print("The average of previous half is {:.2f}".format(average(nextHalf)))
    return (nextHalf + preHalf)

def average(arr):
    length = len(arr)
    return (sum(arr) / length)

array = []
num = input('Please enter a number: (enter a letter to stop) ')
while num.isdigit():
    array.append(int(num))
    num = input('Please enter a number: (enter a letter to stop) ')
print(switchHalf(array))

# 2
def rearrange(arr):
    even = []
    odd = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd

array = []
num = input('Please enter a number: (enter a letter to stop)')
while num.isdigit():
    array.append(int(num))
    num = input('Please enter a number: (enter a letter to stop)')
print(rearrange(array))

# 3
import sys                                                  # provides getsizeof function
data = [ ]
n = 100
current = sys.getsizeof(data)
for k in range(n):                                          # NOTE: must fix choice of n
    a = len(data)
    insertNext = sys.getsizeof(data)                                 # actual size in bytes
    if insertNext > current:                                           # test the size after the data increase
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a - 1, current))
    data.append(None)                                       # increase length by one                                                   
    current = insertNext
        
    

# 4
import ctypes # provides low-level arrays 3 

class DynamicArray: 
    """A dynamic array class akin to a simplified Python list.""" 
    def __init__(self): 
        """Create an empty array.""" 
        self._n = 0                                             # count actual elements
        self._capacity = 1                                      # default array capacity 
        self._A = self._make_array(self._capacity)              # low-level array  
    
    def __len__(self):
        """return numebr of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """Return element at index k."""
        if 0 <= k < self._n:
            return self._A[k]                                   # retrieve from array
        elif -self._n <= k < 0:                                 # the situation of negative number
            return self._A[self._n + k]
        else:
            raise IndexError('Invalid index')        
    
    def append(self, obj):
        """Add object to end of the arrary"""
        if self._n == self._capacity:                           # not enough room
            self._resize(2 * self._capacity)                    # so double capacity
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):                                       # nonpublic utitity
        """Resize internal array to capacity c """
        B = self._make_array(c)                                 # new (bigger) array
        for k in range (self._n):                               # for each existing value
            B[k] = self._A[k]
        self._A = B                                             # use the bigger array
        self._capacity = c
    
    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()                         # see ctypes documentation

# 5
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:                           # not enough room
            oriCap = self._capacity                             # store the orignal capacity
            B = self._make_array(oriCap * 2)                    
            for i in range(self._n + 1):
                # (if the index smaller than the insert index, copy the same index from the original array)
                # else if the index is greater than the insert index, copy the previous one index from the original array)
                B[i] = self._A[i] if i <= k else self._A[i - 1] 
            self._A = B
            self._capacity = oriCap * 2             

        else:
            for j in range(self._n, k, -1):                        # shift rightmost first
                self._A[j] = self._A[j - 1]
        self._A[k] = value                                         # store newset element
        self._n += 1
