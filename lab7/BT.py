# implement of a 2-3-4 tree

class Node(object):
    """
    A node of the B tree.
    """

    def __init__(self, value=None):
        self.keys = [value, None, None]
        self.childs = [None, None, None, None]
        self.parent = None

    def isLeaf(self):
        """
        Check whether the node is a leaf node
        """
        return (self.childs[0] is None and self.childs[1] is None and self.childs[2] is None and self.childs[3] is None)

    def isFull(self):
        """
        Check whether the node is full
        """
        return self.keyCount() == 3
    
    def cutNode(self, childIndex):
        """
            Cut the child of a node
        """
        node = self.childs[childIndex]
        self.childs[childIndex] = None
        return node

    def containKey(self, value):
        """
            return whether the node contains the input key
        """
        for key in self.keys:
            if key == value:
                return True
        return False

    def keyCount(self):
        count = 0
        for key in self.keys:
            if key is not None:
                count += 1
        return count
    
    def deleteAllChilds(self):
        for i in range(len(self.childs)):
            self.childs[i] = None
    
    def findKeyIndex(self, value):
        return self.keys.index(value)
    
    def findChildIndex(self, child):
        return self.childs.index(child)
    
    def getKey(self, keyIndex):
        return self.keys[keyIndex]
    
    def getChild(self, childIndex):
        return self.childs[childIndex]

    def getNextChild(self, value):
        for i in range(len(self.keys)):
            if (self.keys[i] is None or value < self.keys[i]):
                return self.childs[i]
        return self.childs[len(self.childs) - 1] 
    
    def getParent(self):
        return self.parent

    def insertToNode(self, value):
        if self.keyCount() == 3:
            return -1
        for i in range(2, -1, -1):
            if (self.keys[i] is None):
                continue
            else:
                key = self.keys[i]
                if value < key:
                    self.keys[i + 1] = self.keys[i]
                else:
                    self.keys[i + 1] = value
                    return i + 1
        
        self.keys[0] = value
        return 0

    def _connectNode(self, childIndex, node):
        self.childs[childIndex] = node
        if node is not None:
            node.parent = self
    
    def deleteKey(self):
        for i in range(len(self.keys) - 1, -1, -1):
            if self.keys[i] is not None:
                node = self.keys[i]
                self.keys[i] = None
                return node
    
    def lastKeyIndex(self):
        return self.keyCount() - 1
    
    def displayNode(self):
        print("/{}/{}/{}/".format(self.keys[0], self.keys[1], self.keys[2]))
    
    def successor(self, value):
        """
            Find the successor of the value in the node
        """
        child = self.getNextChild(value)
        while not child.isLeaf():
            child = self.getNextChild(value)
        return child, 0

    def predecessor(self, value):
        """
            Find the predecessor of the value in the node
        """
        childIndex = self.findKeyIndex(value)
        child = self.childs[childIndex]
        while not child.isLeaf():
            childIndex = child.keyCount()
            child = self.childs[childIndex]
        return child, child.keyCount() - 1

    def adjust(self):
        """
            Adjust the key, move all element in the front
        """
        # adjust the keys, move all none key at the end
        for i in range(len(self.keys)):
            if self.keys[i] is None:
                j = i + 1
                while j < len(self.keys):
                    if self.keys[j] is not None:
                        self.keys[i] = self.keys[j]
                        self.keys[j] = None
                        break
                    j += 1
        # adjust the childs, move all empty child at the end
        for i in range(len(self.childs)):
            if self.childs[i] is None:
                j = i + 1
                while j < len(self.childs):
                    if self.childs[j] is not None:
                        self.childs[i] = self.childs[j]
                        self.childs[j] = None
                        break
                    j += 1

class two_four_BT(object):
    """
    The 2-3-4 tree
    """
    def __init__(self):
        """
        Initialization of an 2-3-4 tree
        """
        self.root = None
    
    def isEmpty(self):
        """
        Check whether the tree is empty
        """
        return self.root is None
    
    def search(self, value):
        if self.isEmpty():
            return None
        else:
            return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return None
        elif node.containKey(value):
            return node
        else:
            child = node.getNextChild(value)
            return self._search(child, value)

    def exchangeKey(self, node1, index1, node2, index2):
        node1.keys[index1], node2.keys[index2] = node2.keys[index2], node1.keys[index1]
    
    def rightRotate(self, deleteNode, childIndex):
        parent = deleteNode.getParent()
        parent.childs[childIndex] = deleteNode
        parentKeyIndex = childIndex - 1
        siblingNode = parent.getChild(childIndex - 1)
        deleteNodeKeyIndex = 0
        self.exchangeKey(deleteNode, deleteNodeKeyIndex, parent, parentKeyIndex)
        self.exchangeKey(parent, parentKeyIndex, siblingNode, siblingNode.lastKeyIndex())
        parent.adjust()
        siblingNode.adjust()
    
    def leftRotate(self, deleteNode, childIndex):
        parent = deleteNode.getParent()
        parent.childs[childIndex] = deleteNode
        parentKeyIndex = childIndex
        siblingNode = parent.getChild(childIndex + 1)
        deleteNodeKeyIndex = 0
        self.exchangeKey(deleteNode, deleteNodeKeyIndex, parent, parentKeyIndex)
        self.exchangeKey(parent, parentKeyIndex, siblingNode, 0)
        parent.adjust()
        siblingNode.adjust()

    def mergeLeft(self, node, childIndex):
        parent = node.getParent()
        parentKey = parent.getKey(childIndex - 1)
        parent.keys[childIndex - 1] = None
        siblingNode = parent.getChild(childIndex - 1)
        siblingNode.insertToNode(parentKey)
        parent.adjust()

    def mergeRight(self, node, childIndex):
        parent = node.getParent()
        parentKey = parent.getKey(childIndex)
        parent.keys[childIndex] = None
        siblingNode = parent.getChild(childIndex + 1)
        siblingNode.insertToNode(parentKey)
        parent.adjust()

    def insert(self, value):
        if self.isEmpty():
            self.root = Node(value)
        else:
            self._insert(value)

    def _insert(self, value):
        current = self.root
        while True:
            if (current.isFull()):
                # if the current node is full, split the current node and then move to its child node
                self.split(current)
                current = current.getParent()
                current = current.getNextChild(value)
            elif (current.isLeaf()):
                # if the current node is a leaf node, break the while loop and add the value
                break
            else:
                # if not full and not leaf, continue to find the suitable value
                current = current.getNextChild(value)
        
        # insert the value into the suitable node
        current.insertToNode(value)
    
    def split(self, node):
        keyR = node.deleteKey()
        keyM = node.deleteKey()
        childM2 = node.cutNode(2)
        childR = node.cutNode(3)
        newR = Node(keyR)
        newR._connectNode(0, childM2)
        newR._connectNode(1, childR)

        if (node == self.root):
            self.root = Node()
            parent = self.root
            self.root._connectNode(0, node)
        else:
            parent = node.getParent()
        
        dataIndex = parent.insertToNode(keyM)
        keyNum = parent.keyCount()
        index = keyNum - 1
        while (index > dataIndex):
            temp = parent.cutNode(index)
            parent._connectNode(index + 1, temp)
            index -= 1
        parent._connectNode(dataIndex + 1, newR)

    def delete(self, value):
        node = self.search(value)
        if node is None: 
            return False
        else:
            index = node.findKeyIndex(value)
            return self._delete(node, index)
        
    def _delete(self, node, index):
        if node.isLeaf():
            if node.keyCount() > 1:
                # the situation that the leaf node contains more than one key, so we could delete it directly
                node.keys[index] = None
                node.adjust()
            else:
                # the situation that the leaf node contains only one key
                # delete the node first
                parent = node.getParent()
                childIndex = parent.findChildIndex(node)
                parent.cutNode(childIndex)
                node.keys[0] = None
                while True:
                    # find the sibling node
                    if childIndex == 0:
                        preNode = None
                        nextNode = parent.getChild(childIndex + 1)
                    elif childIndex == parent.keyCount():
                        preNode = parent.getChild(childIndex - 1)
                        nextNode = None
                    else:
                        preNode = parent.getChild(childIndex - 1)
                        nextNode = parent.getChild(childIndex + 1)

                    if preNode is not None and preNode.keyCount() > 1 or nextNode is not None and nextNode.keyCount() > 1:
                        # when the sibling node is not a 2 node
                        if preNode is not None and preNode.keyCount() > 1:
                            self.rightRotate(node, childIndex)
                        else:
                            self.leftRotate(node, childIndex)
                        break
                    else:
                        # when the sibling node is 2 node
                        if parent.keyCount() != 1:
                            # when the parent node is not a 2 node
                            if preNode is not None:
                                self.mergeLeft(node, childIndex)
                            else:
                                self.mergeRight(node, childIndex)
                            break
                        else:
                            if preNode is not None:
                                siblingKey = preNode.keys[preNode.lastKeyIndex()]
                                parent.insertToNode(siblingKey)
                                for i in range(preNode.keyCount() + 1):
                                    parent.childs[i] = preNode.childs[i]
                                if node.keys[0] == None:
                                    parent.childs[parent.keyCount()] = None
                                else:
                                    parent.childs[parent.keyCount()] = node
                            else:
                                siblingKey = nextNode.keys[nextNode.lastKeyIndex()]
                                parent.insertToNode(siblingKey)
                                for i in range(1, nextNode.keyCount() + 2):
                                    parent.childs[i] = nextNode.childs[i - 1]
                                if node.keys[0] == None:
                                    parent.childs[0] = None
                                else:
                                    parent.childs[0] = node
                            node = parent
                            # find the parent node
                            if node != self.root:
                                parent = node.getParent()
                                childIndex = parent.findChildIndex(node)
                            else:
                                break

        else:
            key = node.keys[index]
            if node.childs[index].keyCount() > 1:
                predecessorNode, predecessorIndex = node.predecessor(key)
                self.exchangeKey(predecessorNode, predecessorIndex, node, index)
                self._delete(predecessorNode, predecessorNode.findKeyIndex(key))
            else:
                successorNode, successorIndex = node.successor(key)
                self.exchangeKey(successorNode, successorIndex, node, index)
                self._delete(successorNode, successorNode.findKeyIndex(key))

    def recDisplayTree(self, node, level, childNum):
        print("Level = {} Child = {}".format(level, childNum))
        node.displayNode()
        keyNum = node.keyCount()
        for i in range(0, keyNum + 1):
            nextNode = node.getChild(i)
            if (nextNode is not None):
                self.recDisplayTree(nextNode, level + 1, i)
            else:
                return
    
    def displayTree(self):
        self.recDisplayTree(self.root, 0, 0)

    def InOrderTraverse(self, node, sortedKeys, nodeNum):
        if node is not None:
            nodeNum.append(node)
            for i in range(len(node.childs)):
                self.InOrderTraverse(node.childs[i], sortedKeys, nodeNum)
                if (i < node.keyCount()):
                    sortedKeys.append(str(node.keys[i]))

    def __str__(self):
        keyList = []
        nodeList = []
        self.InOrderTraverse(self.root, keyList, nodeList)
        traversal =  ' '.join(keyList)
        size = len(nodeList)
        return ("The size of the tree is {}\nThe InOrder Traversal of the tree is {}".format(size, traversal))

# Create a Tree
tree = two_four_BT()
# Insert the node
tree.insert(5)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(10)
tree.insert(11)
tree.insert(12)
tree.displayTree()
print(tree)
# Delete a value from a non 2 node leaf
tree.delete(12)
tree.displayTree()
print(tree)
# Delete a value from a 2 node leaf
tree.delete(11)
tree.displayTree()
print(tree)
# Delete a value from a non leaf node
tree.delete(7)
tree.displayTree()
# Delete a value from a have 2 node parent and 2 node sibling node
tree.delete(6)
tree.displayTree()
# Print the tree
print(tree)

