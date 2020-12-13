# Name: Ruoling Yu
# Student Number: 500976267
# implement of a hash table


# case 1: Separate Chaining
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
            
class LinkedList(object):
    """
    implement of a linked list to help build the linked list  
    """
    def __init__(self):
        self.head = None
        self.tail = None 

    def is_empty(self):
        """
        check whether the linked list is empty  
        """
        return self.head is None

    def append(self, data):
        # append a node at the end of the linked list
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def search(self, value):
        """
        search weather the value exist 
        """
        current = self.head
        index = 0
        while current is not None:
            # continuous search the next node
            if  (current.data == value):
                return True
            current = current.next
            index += 1
        return False
    
    def display(self):
        count = 0
        current = self.head
        string = ''
        while current is not None:
            string += str(current.data) + ' '
            current = current.next
            count += 1
        if string != '':
            return string
        else:
            return None
        
class HashTable_1(object):
    def __init__(self, size):
        self.elems = [LinkedList() for i in range(size)] 
        self.size = size  # The length of the hash table

    def hash(self, elem):
        return (3 * elem + 5) % self.size
    
    def insert(self, elem):
        address = self.hash(elem)
        # check whether the address has value already
        if self.exist(elem, address):
            return "The value is already exist."
        else:
            self.elems[address].append(elem)
        
    def exist(self, elem, add):
        return self.elems[add].search(elem)
    
    def displayHash(self):
        for i in range(len(self.elems)):
            print("In index {}, it has following elements: {}".format(i, self.elems[i].display()))

# Case 2: Linear Probing
class HashTable_2(object):
    def __init__(self, size):
        self.elems = [None for i in range(size)] 
        self.size = size  # The length of the hash table

    def hash(self, elem):
        return (3 * elem + 5) % self.size
    
    def insert(self, elem):
        address = self.hash(elem)
        while not self.is_empty(address):
            # check whether the index is empty, if not, find the next index
            address += 1
            if address >= len(self.elems):
                address = 0
        self.elems[address] = elem

    def is_empty(self, address):
        return self.elems[address] is None
    
    def displayHash(self):
        for i in range(len(self.elems)):
            print("In index {}, the value is {}".format(i, self.elems[i]))

# Case 3: Double Hashing
class HashTable_3(object):
    def __init__(self, size):
        self.elems = [None for i in range(size)] 
        self.size = size  # The length of the hash table

    def primary_hash(self, elem):
        # the first equation
        return (3 * elem + 5) % self.size
    
    def secondary_hash(self, elem):
        # the second equation
        return 7 - (elem % 7)
    
    def insert(self, elem):
        hash1 = self.primary_hash(elem)
        address = hash1
        if not self.is_empty(address):
            # check whether the index is empty, if not, use the second function to find the next
            hash2 = self.secondary_hash(elem)
            count = 0
            while (count < self.size or not self.is_empty(address)):
                address = (hash1 + hash2 * count) % self.size
                count += 1
        self.elems[address] = elem

    def is_empty(self, address):
        return self.elems[address] is None    
    
    def displayHash(self):
        for i in range(len(self.elems)):
            print("In index {}, the value is {}".format(i, self.elems[i]))

if __name__ == '__main__':
    print("Case 1: Separate Chaining")
    ht1 = HashTable_1(11)
    ht1.insert(12)
    ht1.insert(44)
    ht1.insert(13)
    ht1.insert(88)
    ht1.insert(23)
    ht1.insert(94)
    ht1.insert(11)
    ht1.insert(39)
    ht1.insert(20)
    ht1.insert(16)
    ht1.insert(5)
    ht1.displayHash()
    print("Case 2: Linear Probing")
    ht2 = HashTable_2(11)
    ht2.insert(12)
    ht2.insert(44)
    ht2.insert(13)
    ht2.insert(88)
    ht2.insert(23)
    ht2.insert(94)
    ht2.insert(11)
    ht2.insert(39)
    ht2.insert(20)
    ht2.insert(16)
    ht2.insert(5)
    ht2.displayHash()
    print("Case 3: Double Hashing")
    ht3 = HashTable_3(11)
    ht3.insert(12)
    ht3.insert(44)
    ht3.insert(13)
    ht3.insert(88)
    ht3.insert(23)
    ht3.insert(94)
    ht3.insert(11)
    ht3.insert(39)
    ht3.insert(20)
    ht3.insert(16)
    ht3.insert(5)
    ht3.displayHash()