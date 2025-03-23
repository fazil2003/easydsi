import sys
import time
from collections import deque

class Queue:
    """Implementation of a Queue using deque for efficient operations."""

    def __init__(self, elements=None, visualize=False):
        """
        Initialize the queue.

        Args:
            elements (list): Initial elements in the queue.
            visualize (bool): Whether to enable visualization.
        """
        start_time = time.time()
        self.elements = deque(elements or [])  # Use deque for O(1) add/remove
        self.visualize = visualize
        self.max_size = float('inf')  # Default to unlimited size
        self.allow_str = True

        if visualize:
            self.display_visualize_message(f"Queue created with elements: {list(self.elements)}", time.time() - start_time)

    def __str__(self):
        return str(list(self.elements))

    def __repr__(self):
        return str(list(self.elements))

    def display_visualize_message(self, message, time_taken=0):
        """Prints queue visualization."""
        print(f"{message}\nQueue: {list(self.elements)}\nMemory Usage: {sys.getsizeof(self.elements)} bytes\nTime Taken: {time_taken:.6f} sec")

    def set_config(self, visualize=False, max_size=float('inf'), allow_str=True):
        """Configures queue settings."""
        self.visualize = visualize
        self.max_size = max_size
        self.allow_str = allow_str

    def enqueue(self, item):
        """Adds an item to the queue (rear)."""
        if len(self.elements) >= self.max_size:
            return "Queue overflow"

        if not self.allow_str and isinstance(item, str):
            return "String elements not allowed"

        self.elements.append(item)
        if self.visualize:
            self.display_visualize_message(f"Enqueued: {item}")

    def dequeue(self):
        """Removes and returns the front element of the queue."""
        if not self.elements:
            return "Queue underflow"
        item = self.elements.popleft()
        if self.visualize:
            self.display_visualize_message(f"Dequeued: {item}")
        return item

    def peek(self):
        """Returns the front element without removing it."""
        return self.elements[0] if self.elements else None

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.elements)

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.elements) == 0

    def display(self):
        """Prints the queue elements."""
        print(f"Queue: {list(self.elements)}")

    def get_elements(self):
        """Returns the queue elements as a list (for utilities)."""
        return list(self.elements)