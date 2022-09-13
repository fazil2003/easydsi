# Import the libraries
from ast import Delete
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
    
    # Used in remove function
    # function to delete the given deepest node (d_node) in binary tree
    def deleteDeepest(self, d_node):
        q = []
        q.append(self.root)
        while(len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)
    
    # function to delete element in binary tree
    def remove(self, value):
        if self.root == None :
            return None
        if self.root.left == None and self.root.right == None:
            if self.root.value == value :
                return None
            else :
                return self.root
        value_node = None
        q = []
        q.append(self.root)
        temp = None
        while(len(q)):
            temp = q.pop(0)
            if temp.value == value:
                value_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if value_node :
            x = temp.value
            self.deleteDeepest(temp)
            value_node.value = x
        return self.root
            
    # Getting list of nodes
    def get_nodes(self):
        return list(self.root)

    # Getting list of values
    def get_elements(self):
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
    
     
    # Used in remove function
    def minValueNode(node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current

    def delete(self, root, value):
        # Base Case
        if root is None:
            return root
    
        # If the value to be deleted 
        # is smaller than the root's
        # value then it lies in  left subtree
        if value < root.value:
            root.left = self.delete(root.left, value)
    
        # If the kye to be delete 
        # is greater than the root's value
        # then it lies in right subtree
        elif(value > root.value):
            root.right = self.delete(root.right, value)
    
        # If value is same as root's value, then this is the node
        # to be deleted
        else:
    
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            # Node with two children: 
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)
    
            # Copy the inorder successor's 
            # content to this node
            root.value = temp.value
    
            # Delete the inorder successor
            root.right = self.delete(root.right, temp.value)
    
        return root

    def remove(self, value):
        self.root = self.delete(self.root, value)

def tree(data = []):
    return BinaryTree(data)

def binary_tree(data = []):
    return BinaryTree(data)

def binary_search_tree(data = []):
    return BinarySearchTree(data)

t = tree([3,4,5,2,4,8])
print(t.get_size())