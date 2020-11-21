# implement of an AVL tree

class Node(object):
    def __init__(self, value):
        """
        Initialization of a node in an AVL tree
        """
        self.value = value
        self.height = 0
        self.lChild = None
        self.rChild = None

class AVLTree(object):
    def __init__(self):
        """
        Initialization of an AVL tree
        """
        self.root = None

    def isEmpty(self):
        return self.root is None

    def getHeight(self, node):
        if node == None:
            return -1
        else:
            return node.height

    def __calHeight(self, node):
        return max(self.getHeight(node.lChild), self.getHeight(node.rChild)) + 1

    def __findMin(self, tree):
        """
        Find the minimum node in the tree
        """
        if tree.lChild:
            return self.__findMin(tree.lChild)
        else:
            return tree

    def __findMax(self, tree):
        """
        Find the maximum node in the tree
        """
        if tree.rChild:
            return self.__findMax(tree.rChild)
        else:
            return tree

    def InOrderTraverse(self, node):
        '''
        Use a non recursive version for easy record output
        '''
        stack = []
        string = ''
        position = node
        while position or len(stack) > 0:
            if position:
                stack.append(position)
                position = position.lChild
            else:
                position = stack.pop()
                string += str(position.value) + ' '
                position = position.rChild
        return string

    def leftLeftRotate(self, node):
        """
        LL situation
        """
        temp = node.lChild
        node.lChild = temp.rChild
        temp.rChild = node
        node.height = self.__calHeight(node)
        temp.height = max(self.getHeight(temp.lChild), node.height) + 1
        return temp

    def rightRightRotate(self, node):
        """
        RR situation
        """
        temp = node.rChild
        node.rChild = temp.lChild
        temp.lChild = node
        node.height = self.__calHeight(node)
        temp.height = max(self.getHeight(temp.rChild), node.height) + 1
        return temp

    def leftRightRotate(self, node):
        """
        LR situation
        """
        node.lChild = self.rightRightRotate(node.lChild)
        return self.leftLeftRotate(node)

    def rightLeftRotate(self, node):
        """
        RL situation
        """
        node.rChild = self.leftLeftRotate(node.rChild)
        return self.rightRightRotate(node)

    def insert(self, value):
        """
        Insert a node into a AVL tree
        """
        self.root = self.__insert(self.root, value)
    
    def __insert(self, node, value):
        if (node == None):
            insertNode = Node(value)
            return insertNode
        else:
            if (value < node.value):
                node.lChild = self.__insert(node.lChild, value)
                node_BF = self.getHeight(node.lChild) - self.getHeight(node.rChild)
                if (node_BF == 2):
                    # When the left side need to be balanced
                    if (value < node.lChild.value):
                        node = self.leftLeftRotate(node)
                    else:
                        node = self.leftRightRotate(node)

            elif (value > node.value):
                node.rChild = self.__insert(node.rChild, value)
                node_BF = self.getHeight(node.lChild) - self.getHeight(node.rChild)
                if (node_BF == -2):
                    # When the right side need to be balanced
                    if value > node.rChild.value:
                        node = self.rightRightRotate(node)
                    else:
                        node = self.rightLeftRotate(node)
            
            else:
                return node
            
            node.height = self.__calHeight(node)
            return node

    def delete(self, value):
        """
        Delete a node from a AVL tree
        """
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        if node is None:
            raise Exception('This node is not in the AVL tree.')

        elif value < node.value:
            node.lChild = self.__delete(node.lChild, value)
            node_BF = self.getHeight(node.lChild) - self.getHeight(node.rChild)
            if node_BF == -2:
                if self.getHeight(node.rChild.right) >= self.getHeight(node.rChild.left):
                    node = self.rightRightRotate(node)
                else:
                    node = self.rightLeftRotate(node)
            node.height = self.__calHeight(node)

        elif value > node.value:
            node.rChild = self.__delete(node.rChild, value)
            node_BF = self.getHeight(node.lChild) - self.getHeight(node.rChild)
            if node_BF == 2:
                if self.getHeight(node.lChild.left) >= self.getHeight(node.lChild.right):
                    node = self.leftLeftRotate(node)
                else:
                    node = self.leftRightRotate(node)
            node.height = self.__calHeight(node)

        elif node.lChild and node.rChild:
            if node.lChild.height <= node.rChild.height:
                minNode = self.__findMin(node.rChild)
                node.value = minNode.value
                node.rChild = self.__delete(node.rChild, node.value)
            else:
                maxNode = self.__findMax(node.lChild)
                node.value = maxNode.value
                node.lChild = self.__delete(node.lChild, node.value)
            node.height = self.__calHeight(node)

        else:
            node = node.rChild if node.rChild else node.lChild

        return node


avl = AVLTree()
# Insert
for i in range(10):
    avl.insert(i)
print(avl.InOrderTraverse(avl.root))

# Delete
avl.delete(6)
print(avl.InOrderTraverse(avl.root))
