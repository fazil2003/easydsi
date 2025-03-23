from collections import deque
from .stack_exceptions import StackUnderflowError

class Stack:
    """A memory-efficient stack implementation using deque."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = deque()  # Use deque for optimized push/pop operations

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)  # O(1) time complexity

    def pop(self):
        """Pop and return the top item of the stack. Raises StackUnderflowError if empty."""
        if self.items:
            return self.items.pop()  # O(1) time complexity
        raise StackUnderflowError("Cannot pop from an empty stack")

    def peek(self):
        """Return the top item of the stack without removing it. Raises StackUnderflowError if empty."""
        if self.items:
            return self.items[-1]  # O(1) time complexity
        raise StackUnderflowError("Cannot peek an empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return not self.items  # More Pythonic than len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)  # O(1) time complexity

    def clear(self):
        """Remove all items from the stack."""
        self.items.clear()  # More efficient than reassigning an empty deque

    def __iter__(self):
        """Allow iteration over the stack (from top to bottom)."""
        return reversed(self.items)

    def __repr__(self):
        """Return a string representation of the stack."""
        return f"Stack({list(self.items)})"
