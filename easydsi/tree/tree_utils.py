def contains(tree, value):
    """Checks if a tree contains a specific value."""
    return value in tree.get_elements()

def sum_tree(tree):
    """Returns the sum of all elements in the tree."""
    return sum(tree.get_elements())

def max_in_tree(tree):
    """Returns the maximum value in the tree."""
    return max(tree.get_elements(), default=None)

def min_in_tree(tree):
    """Returns the minimum value in the tree."""
    return min(tree.get_elements(), default=None)
