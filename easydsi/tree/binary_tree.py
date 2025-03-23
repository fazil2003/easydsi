from easydsi.tree import Tree
from binarytree import Node

class BinaryTree(Tree):
    """Represents a Binary Tree."""
    def __init__(self, data=None):
        super().__init__(data)

class BinarySearchTree(Tree):
    """Represents a Binary Search Tree (BST)."""
    def __init__(self, data=None):
        super().__init__()
        if data:
            for value in data:
                self.add(value)

    def add(self, value):
        """Inserts a value into the BST."""
        if self.root is None:
            self.root = Node(value)
            return

        curr_node = self.root
        while True:
            if value == curr_node.value:
                break  # No duplicates allowed
            elif value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = Node(value)
                    break
                curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = Node(value)
                    break
                curr_node = curr_node.right

    def _min_value_node(self, node):
        """Finds the node with the minimum value in the subtree."""
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, root, value):
        """Helper function for deleting a node."""
        if root is None:
            return root

        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self._min_value_node(root.right)
            root.value = temp.value
            root.right = self._delete(root.right, temp.value)

        return root

    def remove(self, value):
        """Removes a value from the BST."""
        self.root = self._delete(self.root, value)
