from easydsi.heap import MinHeap, MaxHeap
import heapq

def heapify_list(data, max_heap=False):
    """
    Converts a list into a MinHeap or MaxHeap.

    Args:
        data (list): The list of elements.
        max_heap (bool, optional): If True, creates a MaxHeap. Defaults to False.

    Returns:
        MinHeap or MaxHeap: The corresponding heap.
    """
    return MaxHeap(data) if max_heap else MinHeap(data)

def merge_heaps(heap1, heap2, max_heap=False):
    """
    Merges two heaps into a new MinHeap or MaxHeap.

    Args:
        heap1: The first heap instance.
        heap2: The second heap instance.
        max_heap (bool, optional): If True, creates a MaxHeap. Defaults to False.

    Returns:
        MinHeap or MaxHeap: The merged heap.
    """
    merged_data = heap1.get_elements() + heap2.get_elements()
    return MaxHeap(merged_data) if max_heap else MinHeap(merged_data)

def is_heap_sorted(heap, max_heap=False):
    """
    Checks if a given heap is sorted.

    Args:
        heap: The heap instance.
        max_heap (bool, optional): If True, checks for max-heap order. Defaults to False.

    Returns:
        bool: True if sorted, False otherwise.
    """
    elements = heap.get_elements()
    return elements == sorted(elements, reverse=max_heap)

def get_top_n(heap, n=1):
    """
    Retrieves the top 'n' elements from a MinHeap or MaxHeap.

    Args:
        heap: The heap instance.
        n (int, optional): Number of elements to retrieve. Defaults to 1.

    Returns:
        list: Top 'n' elements.
    """
    return heapq.nlargest(n, heap.get_elements()) if isinstance(heap, MinHeap) else sorted(heap.get_elements(), reverse=True)[:n]

def heap_sort(data, descending=False):
    """
    Sorts a list using heap sort.

    Args:
        data (list): The list of elements to sort.
        descending (bool, optional): If True, sorts in descending order. Defaults to False.

    Returns:
        list: The sorted list.
    """
    heap = MaxHeap(data) if descending else MinHeap(data)
    sorted_list = [heap.remove() for _ in range(len(data))]
    return sorted_list

def contains(heap, element):
    """
    Checks if an element exists in the heap.

    Args:
        heap: The heap instance.
        element: The element to check.

    Returns:
        bool: True if found, False otherwise.
    """
    return element in heap.get_elements()

def clear_heap(heap):
    """
    Clears all elements from the heap.

    Args:
        heap: The heap instance.
    """
    heap._heap.clear()

def size(heap):
    """
    Returns the number of elements in the heap.

    Args:
        heap: The heap instance.

    Returns:
        int: Number of elements in the heap.
    """
    return len(heap.get_elements())

def sum_heap(heap):
    """
    Computes the sum of all elements in the heap.

    Args:
        heap: The heap instance.

    Returns:
        int: Sum of elements.
    """
    return sum(heap.get_elements())

def max_in_heap(heap):
    """
    Finds the maximum element in the heap.

    Args:
        heap: The heap instance.

    Returns:
        int: Maximum element.
    """
    return max(heap.get_elements(), default=None)

def min_in_heap(heap):
    """
    Finds the minimum element in the heap.

    Args:
        heap: The heap instance.

    Returns:
        int: Minimum element.
    """
    return min(heap.get_elements(), default=None)
