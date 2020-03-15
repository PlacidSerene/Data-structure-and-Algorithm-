class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left == None:
                        currentNode.left = new_node
                        return self
                    currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        currentNode.right = new_node
                        return self
                    currentNode = currentNode.right

            
    def lookup(self,data):
        currentNode = self.root
        if currentNode == None:
            return False
        else:
            while currentNode != None:

                if data < currentNode.value:
                    if currentNode.value == data:
                        return True
              
                    currentNode = currentNode.left
        
                else:
                    if currentNode.value == data:
                        return True
                    currentNode = currentNode.right

            return False

    def remove(self,value):
        if self.root == None:
            return False
        currentNode = self.root
        parentNode = None
        while (currentNode != None):
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else: # we have a match
                # case 1: No right child
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left    
                    else:
                        #if parent > current value, make current left child a child of parent
                        if parentNode.value > currentNode.value:
                            parentNode.left = currentNode.left
                        #if parent < current value, make left child a right child of parent
                        elif parentNode.value < currentNode.value:
                            parentNode.right = currentNode.left
                #case 2: Right child which doesn't have a left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        #if parent > current, make right child of the left the parent
                        if parentNode.value > currentNode.value:
                            parrentNode.left = currentNode.right
                        #if parent < current, make right child a right child of the parent
                        elif parentNode.value < currentNode.value:
                            parentNode.right = currentNode.right

                #case 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while (leftmost.left != None):
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    #Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if parentNode.value < currentNode.value:
                            parentNode.right = leftmost
                        elif parentNode.value > currentNode.value:
                            parentNode.left = leftmost
            return True




        

firstTree = BinarySearchTree()
firstTree.insert(9)
firstTree.insert(4)
firstTree.insert(6)
firstTree.insert(1)
firstTree.insert(20)
firstTree.insert(15)
firstTree.insert(170)
print(firstTree.lookup(10))


