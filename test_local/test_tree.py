from easydsi.tree.binary_tree import BinaryTree, BinarySearchTree
from easydsi.tree.tree_utils import max_in_tree, sum_tree

bt = BinaryTree([3, 5, 1, 7, 2])
print(bt.inorder())  # Get inorder traversal

bst = BinarySearchTree([10, 5, 15, 2, 7])
print(max_in_tree(bst))  # Get max value in BST

bt.add(6)
print(bt.get_elements())  # Get elements after adding 6

bst.remove(5)
print(sum_tree(bst))  # Get sum of BST elements after removal

print(bst)