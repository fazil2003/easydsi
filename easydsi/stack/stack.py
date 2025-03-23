from .stack_exceptions import StackUnderflowError

class Stack:
    """A simple stack implementation."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pop the top item from the stack and return it."""
        if not self.is_empty():
            return self.items.pop()
        raise StackUnderflowError("Cannot pop from an empty stack")

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise StackUnderflowError("Cannot peek an empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def clear(self):
        """Remove all items from the stack."""
        self.items = []

    def __str__(self):
        return f"Stack({self.items})"
