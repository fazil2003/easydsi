from binarytree import Node, build

class Tree:
    def __init__(self, data=None):
        """Initialize the tree with given data."""
        self.root = build(data) if data else None

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self.root)

    def add(self, value):
        """Adds a value to the tree using level-order traversal."""
        if self.root is None:
            self.root = Node(value)
            return
        
        queue = [self.root]
        while queue:
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

    def get_nodes(self):
        """Returns the list of nodes."""
        return list(self.root) if self.root else []

    def get_elements(self):
        """Returns the list of values in the tree."""
        return self.root.values if self.root else []

    def inorder(self):
        """Returns the inorder traversal of the tree."""
        return self.root.inorder if self.root else []

    def preorder(self):
        """Returns the preorder traversal of the tree."""
        return self.root.preorder if self.root else []

    def postorder(self):
        """Returns the postorder traversal of the tree."""
        return self.root.postorder if self.root else []

    def levelorder(self):
        """Returns the level-order traversal of the tree."""
        return self.root.levelorder if self.root else []

    def get_size(self):
        """Returns the size of the tree (number of nodes)."""
        return self.root.size if self.root else 0

    def get_height(self):
        """Returns the height of the tree."""
        return self.root.height if self.root else 0

    def get_properties(self):
        """Returns all properties of the tree."""
        return self.root.properties if self.root else {}

    def clear(self):
        """Clears the tree."""
        self.root = None
