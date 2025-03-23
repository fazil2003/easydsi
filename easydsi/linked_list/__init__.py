# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():

    # Initialize
    def __init__(self, elements, visualize):
        self.head = None
        if (elements is not None and len(elements) > 0):
            self.__generate_list(elements)

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return str(self.head)

    # CREATE
    def __create_node(self, data: int) -> Node | None:
        node = Node(data)
        return node

    # INSERT
    # Insert the node in the front
    def __insert_front(self, node: Node, data: int) -> Node | None:
        new_node = self.create_node(data)
        new_node.next = node
        return new_node

    # Insert the node at some particular position.
    def __insert_at_position(self, node: Node, data: int, position: int) -> Node | None:
        if (position == 1):
            return self.__insert_front(node, data)

        head = node
        while(node and position > 1):
            prev = node
            node = node.next
            position -= 1

        if (position != 1):
            print("Index out of bounds")
            return head

        new_node = self.create_node(data)
        new_node.next = node
        prev.next = new_node
        return head

    def __generate_list(self, data: list = []) -> Node:
        head = self.create_node(data[0])
        prev = head
        for val in data[1:]:
            node = self.create_node(val)
            prev.next = node
            prev = node
        return head

    # DELETE
    # Delete the last element
    def __delete_last(self, node: Node) -> Node | None:
        if (node.next == None):
            return None

        head = node
        while (node.next.next):
            node = node.next

        node.next = None
        return head

    # Delete the node at the given position
    def __delete_at_position(self, node: Node, position: int) -> Node | None:
        if (position == 1):
            return node.next

        head = node
        while(node.next and position > 1):
            prev = node
            node = node.next
            position -= 1
        
        if (position != 1):
            print("Index out of bounds")
            return head

        prev.next = node.next
        return head

    # Traverse the linked list
    def __traverse(self, node: Node) -> None:
        index = 0
        while(node):
            index += 1
            print("position:", index, ", data:", node.data)
            node = node.next

    # Reverse the linked list
    def __reverse_list(self, node: Node) -> Node:
        if (node.next == None):
            return node

        head = self.__reverse_list(node.next, False)
        node.next.next = node
        node.next = None
        return head

    def create_node(self, data: int) -> Node | None:
        return self.__create_node(data)

    def insert_front(self, data: int) -> Node | None:
        self.head = self.__insert_front(self.head, data)
        return self.head

    def insert_at_position(self, data: int, position: int) -> Node | None:
        self.head = self.__insert_at_position(self.head, data, position)
        return self.head

    def generate_list(self, data: list = []) -> Node | None:
        self.head = self.__generate_list(data)
        return self.head

    def delete_last(self) -> Node | None:
        self.head = self.__delete_last(self.head, position)
        return self.head

    def delete_at_position(self, position: int) -> Node | None:
        self.head = self.__delete_at_position(self.head, position)
        return self.head

    def traverse(self) -> None:
        self.__traverse(self.head)

    def reverse_list(self) -> Node:
        self.head = self.__reverse_list(self.head)
        return self.head

# Create a linked list
def linked_list(elements = [], visualize = False):
    return LinkedList(elements, visualize)