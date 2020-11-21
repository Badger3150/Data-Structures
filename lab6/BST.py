# implement of a basic BST

class BSTNode(object):
    def __init__(self, data):
            self.data = data
            self.lChild = None
            self.rChild = None
    
class createBST(object):
    def __init__(self):
        self.root = None
        self.size = 0
    
    def isEmpty(self):
        return not self.root

    def search(self, data):
        node = self.root
        parent = None
        while node is not None:
            if node.data == data:
                return True, node, parent
            elif data < node.data:
                parent = node
                node = node.lChild
            elif data > node.data:
                parent = node
                node = node.rChild
        return False, node, parent
    
    def getMax(self):
        if not self.isEmpty():
            maximum = self.root.data
            parent = self.root
            while parent.rChild:
                maximum = parent.rChild.data
                parent = parent.rChild
            return maximum
        else:
            raise Exception('The BST is empty')
    
    def getMin(self):
        if not self.isEmpty():
            minimum = self.root.data
            parent = self.root
            while parent.lChild:
                minimum = parent.lChild.data
                parent = parent.lChild
            return minimum
        else:
            raise Exception('The BST is empty')

    def getHeight(self, node):
        if node is None:
            return 0
        lHeight = self.getHeight(node.lChild)
        rHeight = self.getHeight(node.rChild)
        return max(lHeight, rHeight) + 1

    def insert(self, data):
        '''Insert a node into the tree'''
        node = BSTNode(data)
        if self.isEmpty():
            self.root = node
            self.size += 1
            return
        else:
            parent = self.root
            while True:
                if node.data < parent.data:
                    if parent.lChild:
                        parent = parent.lChild
                    else:
                        parent.lChild = node
                        self.size += 1
                        break
                elif node.data > parent.data:
                    if parent.rChild:
                        parent = parent.rChild
                    else:
                        parent.rChild = node
                        self.size += 1
                        break
                else:
                    break
    
    def delete(self, data):
        '''Delete a node from the tree'''
        existed, node, parent = self.search(data)
        if existed:
            if node.lChild is None:
                if parent.lChild == node:
                    parent.lChild = node.rChild
                else:
                    parent.rChild = node.rChild
                del node
                self.size -= 1
            elif node.rChild is None:
                if parent.rChild == node:
                    parent.rChild = node.lChild
                else:
                    parent.lChild = node.lChild
                del node
                self.size -= 1
            else:
                minNode = node.rChild
                parent = node
                while minNode.lChild:
                    parent = minNode
                    minNode = minNode.lChild
                node.data = minNode.data
                if parent.lChild == minNode:
                    parent.lChild = minNode.rChild
                else:
                    parent.rChild = minNode.rChild
                del minNode
                self.size -= 1
        else:
            raise Exception('The value is not in the BST.')
    
    def __str__(self):
        return "For this tree:\nSize: {}\nInOrder Traversal: {}\nHeight: {}\nMinimum value: {}\nMaximum value: {}".format(self.size, self.InOrderTraverse(self.root), self.getHeight(self.root), self.getMin(), self.getMax())

    def InOrderTraverse(self, node):
        '''Use a non recursive version for easy record output'''
        stack = []
        string = ''
        position = node
        while position or len(stack) > 0:
            if position:
                stack.append(position)
                position = position.lChild
            else:
                position = stack.pop()
                string += str(position.data) + ' '
                position = position.rChild
        return string
        # Recursive version
        # if node is None:
        #     return
        # self.InOrderTraverse(node.lChild)
        # print(node.data, end = " ")
        # self.InOrderTraverse(node.rChild)
    

bst = createBST()
# Insert a node into the BST:
bst.insert(5)
bst.insert(2)
bst.insert(9)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(7)
bst.insert(8)
bst.insert(10)
print(bst.InOrderTraverse(bst.root))

# Delete a node from the BST
# the node to be removed is a leaf
bst.delete(10)
print("After deleting node 10: {}". format(bst.InOrderTraverse(bst.root)))
# the node to be removed has one child
bst.delete(3)
print("After deleting node 3: {}". format(bst.InOrderTraverse(bst.root)))
# the node to be removed has two children
bst.delete(5)
print("After deleting node 5: {}". format(bst.InOrderTraverse(bst.root)))

# Print
print(bst)







