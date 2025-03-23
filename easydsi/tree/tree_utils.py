def contains(tree, value):
    """Checks if a tree contains a specific value."""
    return value in tree.get_elements()

def sum_tree(tree):
    """Returns the sum of all elements in the tree."""
    return sum(tree.get_elements(), default=0)

def max_in_tree(tree):
    """Returns the maximum value in the tree."""
    return max(tree.get_elements(), default=None)

def min_in_tree(tree):
    """Returns the minimum value in the tree."""
    return min(tree.get_elements(), default=None)

def count_nodes(tree):
    """Returns the total number of nodes in the tree."""
    return tree.get_size()

def count_leaves(tree):
    """Returns the number of leaf nodes in the tree."""
    return sum(1 for node in tree.get_nodes() if node.is_leaf())

def depth_of_value(tree, value):
    """Finds the depth of a specific value in the tree."""
    queue = [(tree.root, 0)]
    while queue:
        node, depth = queue.pop(0)
        if node.value == value:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return -1  # Value not found

def is_balanced(tree):
    """Checks if a tree is height-balanced."""
    return tree.get_height() <= (2 * (tree.get_size() ** 0.5))  # Rough balance check

def is_full(tree):
    """Checks if a tree is a full binary tree (each node has 0 or 2 children)."""
    for node in tree.get_nodes():
        if (node.left is None) != (node.right is None):  # XOR check
            return False
    return True

def is_perfect(tree):
    """Checks if a tree is a perfect binary tree (all levels are full)."""
    size = tree.get_size()
    height = tree.get_height()
    return size == (2 ** (height + 1)) - 1  # Perfect tree formula

def is_complete(tree):
    """Checks if a tree is a complete binary tree (all levels except last are full, last level left-aligned)."""
    queue = [tree.root]
    found_none = False
    while queue:
        node = queue.pop(0)
        if node:
            if found_none:
                return False  # Found a `None` before a node
            queue.append(node.left)
            queue.append(node.right)
        else:
            found_none = True
    return True

def mirror_tree(tree):
    """Creates a mirrored version of the tree (left and right children swapped)."""
    def mirror(node):
        if node:
            node.left, node.right = mirror(node.right), mirror(node.left)
        return node
    mirrored_root = mirror(tree.root)
    return type(tree)(mirrored_root)  # Return new tree instance

def print_tree(tree):
    """Prints a visual representation of the tree."""
    print(tree)

def get_leaf_nodes(tree):
    """Returns a list of leaf nodes in the tree."""
    return [node.value for node in tree.get_nodes() if node.is_leaf()]

def get_internal_nodes(tree):
    """Returns a list of internal (non-leaf) nodes in the tree."""
    return [node.value for node in tree.get_nodes() if not node.is_leaf()]

def get_height(tree):
    """Returns the height of the tree."""
    return tree.get_height()

def get_root(tree):
    """Returns the root node of the tree."""
    return tree.root.value if tree.root else None

def get_leaves(tree):
    """Returns all leaf node values."""
    return [node.value for node in tree.get_nodes() if node.is_leaf()]

def get_internal_nodes(tree):
    """Returns all internal (non-leaf) node values."""
    return [node.value for node in tree.get_nodes() if not node.is_leaf()]

def get_deepest_node(tree):
    """Finds and returns the deepest node in the tree."""
    queue = [tree.root]
    deepest_node = None
    while queue:
        deepest_node = queue.pop(0)
        if deepest_node.left:
            queue.append(deepest_node.left)
        if deepest_node.right:
            queue.append(deepest_node.right)
    return deepest_node.value if deepest_node else None

def get_level_of_node(tree, value):
    """Returns the level of a given node value."""
    queue = [(tree.root, 0)]
    while queue:
        node, level = queue.pop(0)
        if node.value == value:
            return level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return -1  # Node not found

def get_ancestors(tree, value):
    """Returns a list of ancestor nodes for a given value."""
    def find_ancestors(node, target, path):
        if not node:
            return False
        if node.value == target:
            return True
        if find_ancestors(node.left, target, path) or find_ancestors(node.right, target, path):
            path.append(node.value)
            return True
        return False

    path = []
    find_ancestors(tree.root, value, path)
    return path[::-1]  # Reverse the list to get root to node order

def lowest_common_ancestor(tree, value1, value2):
    """Finds the lowest common ancestor (LCA) of two nodes."""
    def find_lca(node, v1, v2):
        if not node:
            return None
        if node.value == v1 or node.value == v2:
            return node
        left_lca = find_lca(node.left, v1, v2)
        right_lca = find_lca(node.right, v1, v2)
        if left_lca and right_lca:
            return node
        return left_lca if left_lca else right_lca

    lca_node = find_lca(tree.root, value1, value2)
    return lca_node.value if lca_node else None

def get_diameter(tree):
    """Finds the diameter (longest path) of the tree."""
    def height_and_diameter(node):
        if not node:
            return 0, 0
        left_height, left_diameter = height_and_diameter(node.left)
        right_height, right_diameter = height_and_diameter(node.right)
        return 1 + max(left_height, right_height), max(left_diameter, right_diameter, 1 + left_height + right_height)

    return height_and_diameter(tree.root)[1]

def get_boundary_nodes(tree):
    """Returns the boundary nodes of the tree (left boundary, leaves, right boundary)."""
    if not tree.root:
        return []

    def left_boundary(node):
        return [node.value] + left_boundary(node.left) if node and (node.left or node.right) else []

    def right_boundary(node):
        return right_boundary(node.right) + [node.value] if node and (node.left or node.right) else []

    def leaves(node):
        return leaves(node.left) + ([node.value] if node.is_leaf() else []) + leaves(node.right) if node else []

    return [tree.root.value] + left_boundary(tree.root.left) + leaves(tree.root) + right_boundary(tree.root.right)

def zigzag_traversal(tree):
    """Returns the zigzag level order traversal of the tree."""
    if not tree.root:
        return []
    
    result, temp, stack, direction = [], [], [tree.root], 1
    while stack:
        for _ in range(len(stack)):
            node = stack.pop(0)
            temp.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.append(temp[::direction])
        temp, direction = [], -direction
    return result

def is_symmetric(tree):
    """Checks if the tree is symmetric (mirror image of itself)."""
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.value != t2.value:
            return False
        return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

    return is_mirror(tree.root.left, tree.root.right) if tree.root else True

def is_identical(tree1, tree2):
    """Checks if two trees are identical."""
    def check_identical(n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2 or n1.value != n2.value:
            return False
        return check_identical(n1.left, n2.left) and check_identical(n1.right, n2.right)

    return check_identical(tree1.root, tree2.root)

def inorder(tree):
    """Returns the in-order traversal of the tree (Left, Root, Right)."""
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    traverse(tree.root)
    return result

def preorder(tree):
    """Returns the pre-order traversal of the tree (Root, Left, Right)."""
    result = []
    def traverse(node):
        if node:
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)
    traverse(tree.root)
    return result

def postorder(tree):
    """Returns the post-order traversal of the tree (Left, Right, Root)."""
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
    traverse(tree.root)
    return result

def levelorder(tree):
    """Returns the level-order traversal of the tree (Breadth-First)."""
    if not tree.root:
        return []
    result, queue = [], [tree.root]
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
