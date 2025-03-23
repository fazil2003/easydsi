import heapq

class MinHeap:
    """A MinHeap implementation using the heapq module."""

    def __init__(self, data=None):
        """
        Initializes a MinHeap.

        Args:
            data (list, optional): Initial list of elements. Defaults to an empty list.
        """
        self._heap = list(data) if data else []
        heapq.heapify(self._heap)

    def add(self, element):
        """Inserts an element into the heap."""
        heapq.heappush(self._heap, element)

    def remove(self):
        """Removes and returns the smallest element from the heap."""
        return heapq.heappop(self._heap) if self._heap else None

    def peek(self):
        """Returns the smallest element without removing it."""
        return self._heap[0] if self._heap else None

    def get_elements(self):
        """Returns all elements in the heap as a list (not necessarily sorted)."""
        return list(self._heap)

    def size(self):
        """Returns the number of elements in the heap."""
        return len(self._heap)

    def is_empty(self):
        """Returns True if the heap is empty, otherwise False."""
        return len(self._heap) == 0

    def clear(self):
        """Clears all elements from the heap."""
        self._heap.clear()


class MaxHeap:
    """A MaxHeap implementation using a negated MinHeap approach."""

    def __init__(self, data=None):
        """
        Initializes a MaxHeap.

        Args:
            data (list, optional): Initial list of elements. Defaults to an empty list.
        """
        self._heap = [-i for i in (data or [])]
        heapq.heapify(self._heap)

    def add(self, element):
        """Inserts an element into the heap."""
        heapq.heappush(self._heap, -element)

    def remove(self):
        """Removes and returns the largest element from the heap."""
        return -heapq.heappop(self._heap) if self._heap else None

    def peek(self):
        """Returns the largest element without removing it."""
        return -self._heap[0] if self._heap else None

    def get_elements(self):
        """
        Returns all elements in the heap as a list.
        Unlike a sorted list, this reflects the actual heap structure.
        """
        return [-i for i in self._heap]

    def size(self):
        """Returns the number of elements in the heap."""
        return len(self._heap)

    def is_empty(self):
        """Returns True if the heap is empty, otherwise False."""
        return len(self._heap) == 0

    def clear(self):
        """Clears all elements from the heap."""
        self._heap.clear()


class Heap:
    """
    A generic Heap class that defaults to MinHeap but can act as MaxHeap.
    """

    def __init__(self, data=None, max_heap=False):
        """
        Initializes a Heap.

        Args:
            data (list, optional): Initial list of elements.
            max_heap (bool, optional): If True, creates a MaxHeap; otherwise, creates a MinHeap.
        """
        self._heap = MaxHeap(data) if max_heap else MinHeap(data)

    def __getattr__(self, name):
        """
        Dynamically delegates method calls to the underlying heap instance.

        Args:
            name (str): The name of the method.

        Returns:
            The corresponding method from MinHeap or MaxHeap.
        """
        if hasattr(self._heap, name):
            return getattr(self._heap, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
