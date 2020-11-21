# Singly link list
import queue
class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None 

    def is_empty(self):
        return self.head is None

    def get_data(self, index):
        count = 0
        current = self.head
        while current is not None:
            if (count == index):
                return (current.data)
            current = current.next
            count += 1
        raise Exception('The index is over')

    def append(self, data):
        # append a node at the end of the linked list
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def insert(self, index, value):
        # insert a node into the linked list
        # if want to insert at the beginning, input 0 as the index
        # otherwise input a specify index numebr
        prePointer = self.head
        count = 0
        insertNode = Node(value)
        while (count < index - 1):
            if prePointer.next is None:
                raise Exception("The index is over.")
            else:
                prePointer = prePointer.next
                count += 1
        if (index == 0):
            insertNode.next = self.head
            self.head = insertNode
        else:
            insertNode.next = prePointer.next
            prePointer.next = insertNode
        if insertNode.next is None:
            self.tail = insertNode

    def remove(self, index):
        # remove a node from the linked list
        # input the index to delete the node
        prePointer = self.head
        count = 0
        while (count < index - 1):
            if prePointer.next is None:
                raise Exception("The index is over.")
            else:
                prePointer = prePointer.next
                count += 1
        if (count == 0):
            self.head = prePointer.next
            prePointer.next = None
        else:
            rmvPointer = prePointer.next
            prePointer.next = rmvPointer.next
            if prePointer.next is None:
                self.tail = prePointer
            rmvPointer.next = None
    
    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if  (current.data == value):
                print("The value {0} is found, its index is {1}.".format(value, index))
                return True
            current = current.next
            index += 1
        return False

    def reverse(self):
        stack = queue.LifoQueue()
        current = self.head
        while current is not None:
            stack.put(current.data)
            current = current.next
            self.remove(0)
        while not stack.empty():
            self.append(stack.get())

    def showDatas(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("")


linkedlist = LinkedList()
for i in range(10, 100, 10):
    linkedlist.append(i)

# a. Search a specific itemin the linked list and return trueif the item is foundand display the node positionotherwise return false.

#1) search for the first node
print(linkedlist.search(10))
#2) search for the last node
print(linkedlist.search(90))
#3) search for a middle node
print(linkedlist.search(40))
#4) search for a node that doesn't exist
print(linkedlist.search(100))

# b. Reverse the link list.
print("Before reversing the linked list:")
linkedlist.showDatas()
print("After reversing the linked list:")
linkedlist.reverse()
linkedlist.showDatas()
