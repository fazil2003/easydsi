# Import the libraries
from binarytree import bst, Node, build, tree

class Tree():

    root = None

    def __init__(self, data):
        if not data:
            self.root = None
        else:
            self.root = build(data)

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self.root)

    def add(self, value):

        queue = []
        queue.append(self.root)

        if self.root is None:
            self.root = Node(value)
        else:
            while(len(queue) > 0):
                curr_node = queue.pop(0)
                if curr_node.left is None:
                    curr_node.left = Node(value)
                    break
                elif curr_node.right is None:
                    curr_node.right = Node(value)
                    break
                else:
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
    
    def remove(self, value):

        queue = []
        queue.append(self.root)

        if self.root is None:
            return None

        elif self.root.value == value:
            if self.root.left is None:
                self.root.right.left = self.root.left
                self.root = self.root.right
            elif self.root.right is None:
                self.root.left.right = self.root.right
                self.root = self.root.left
            else:
                self.root.right.left = self.root.left
                self.root = self.root.right
        else:

            while(len(queue) > 0):
                curr_node = queue.pop(0)

                if curr_node.left is not None:
                    if curr_node.left.value == value:
                        if curr_node.left.right is not None:
                            curr_node.left.right.left = curr_node.left.left
                            curr_node.left = curr_node.left.right
                        else:
                            curr_node.left.left.right = curr_node.left.right
                            curr_node.left = curr_node.left.left
                        break
                    else:
                        queue.append(curr_node.left)
                if curr_node.right is not None:
                    if curr_node.right.value == value:
                        if curr_node.right.right is not None:
                            curr_node.right.right.left = curr_node.right.left
                            curr_node.right = curr_node.right.right
                        else:
                            curr_node.right.left.right = curr_node.right.right
                            curr_node.right = curr_node.right.left
                        break
                    else:
                        queue.append(curr_node.right)
            
    # Getting list of nodes
    def get_nodes(self):
        return list(self.root)

    # Getting list of values
    def get_values(self):
        return self.root.values
  
    # Getting inorder of nodes
    def inorder(self):
        return self.root.inorder

    # Getting preorder of nodes
    def preorder(self):
        return self.root.preorder

    # Getting postorder of nodes
    def postorder(self):
        return self.root.postorder

    # Getting levelorder of nodes
    def levelorder(self):
        return self.root.levelorder
    
    # Get the size of tree
    def get_size(self):
        return self.root.size

    # Get the height of tree
    def get_height(self):
        return self.root.height
    
    # Get all properties at once
    def get_properties(self):
        return self.root.properties

class BinaryTree(Tree):
    def __init__(self, data):
        super().__init__(data)

class BinarySearchTree(Tree):

    root = None

    def __init__(self, data = []):
        
        if data == []:
            self.root = None

        else:

            for value in data:
                if self.root is None:
                    self.root = Node(value)
                else:
                    curr_node = self.root

                    while True:
                        if value == curr_node.value:
                            break
                        elif value < curr_node.value:
                            if curr_node.left is None:
                                curr_node.left = Node(value)
                                break
                            else:
                                curr_node = curr_node.left
                        elif value > curr_node.value:
                            if curr_node.right is None:
                                curr_node.right = Node(value)
                                break
                            else:
                                curr_node = curr_node.right
    


    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            curr_node = self.root

            while True:
                if value == curr_node.value:
                    break
                elif value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = Node(value)
                        break
                    else:
                        curr_node = curr_node.left
                elif value > curr_node.value:
                    if curr_node.right is None:
                        curr_node.right = Node(value)
                        break
                    else:
                        curr_node = curr_node.right
    
    def remove(self, value):
        if self.root is None:
            return None
        elif self.root.value == value:
            if self.root.left is None:
                self.root.right.left = self.root.left
                self.root = self.root.right
            elif self.root.right is None:
                self.root.left.right = self.root.right
                self.root = self.root.left
            else:
                self.root.right.left = self.root.left
                self.root = self.root.right
        else:
            curr_node = self.root

            parent_node = curr_node

            # 0 - left, 1 - right
            side = 0

            while True:
                if curr_node is None:
                    break
                elif value == curr_node.value:
                    if side == 0:
                        if curr_node.right is None:
                            parent_node.left = curr_node.left
                        elif curr_node.left is None:
                            parent_node.left = curr_node.right
                        else:
                            curr_node
                            parent_node.left = curr_node.right
                    else:
                        if curr_node.right is None:
                            parent_node.right = curr_node.left
                        elif curr_node.left is None:
                            parent_node.right = curr_node.right
                        else:
                            parent_node.right = curr_node.right
                    break
                elif value < curr_node.value:
                    parent_node = curr_node
                    curr_node = curr_node.left
                    side = 0
                elif value > curr_node.value:
                    parent_node = curr_node
                    curr_node = curr_node.right
                    side = 1


def binary_tree(data = []):
    return BinaryTree(data)

def binary_search_tree(data = []):
    return BinarySearchTree(data)