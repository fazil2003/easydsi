from .stack import Stack

def reverse_stack(stack):
    """Reverse the order of elements in a stack."""
    temp_stack = Stack()
    while not stack.is_empty():
        temp_stack.push(stack.pop())
    return temp_stack
