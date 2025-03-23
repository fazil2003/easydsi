from easydsi.heap import Heap, MinHeap, MaxHeap
import easydsi.heap.heap_utils as heap_utils

def test_heap():
    """Test all heap functionalities including heap_utils."""

    print("\n===== MinHeap Test =====")
    min_heap = Heap([5, 3, 8, 1, 2])
    print("Initial MinHeap:", min_heap.get_elements())

    min_heap.add(0)
    print("After Adding 0:", min_heap.get_elements())

    print("Peek (Min):", min_heap.peek())
    print("Remove (Min):", min_heap.remove())
    print("After Removal:", min_heap.get_elements())

    print("\n===== MaxHeap Test =====")
    max_heap = Heap([5, 3, 8, 1, 2], max_heap=True)
    print("Initial MaxHeap:", max_heap.get_elements())

    max_heap.add(10)
    print("After Adding 10:", max_heap.get_elements())

    print("Peek (Max):", max_heap.peek())
    print("Remove (Max):", max_heap.remove())
    print("After Removal:", max_heap.get_elements())

    print("\n===== Utility Tests =====")

    # Test heapify_list()
    print("\nTesting heapify_list()...")
    min_heap_util = heap_utils.heapify_list([7, 4, 9, 2, 6])
    max_heap_util = heap_utils.heapify_list([7, 4, 9, 2, 6], max_heap=True)

    print("Heapified MinHeap:", min_heap_util.get_elements())
    print("Heapified MaxHeap:", max_heap_util.get_elements())

    # Test merge_heaps()
    print("\nTesting merge_heaps()...")
    merged_min_heap = heap_utils.merge_heaps(min_heap, min_heap_util)
    merged_max_heap = heap_utils.merge_heaps(max_heap, max_heap_util, max_heap=True)

    print("Merged MinHeap:", merged_min_heap.get_elements())
    print("Merged MaxHeap:", merged_max_heap.get_elements())

    # Test is_heap_sorted()
    print("\nTesting is_heap_sorted()...")
    print("Is MinHeap Sorted?:", heap_utils.is_heap_sorted(min_heap))
    print("Is MaxHeap Sorted?:", heap_utils.is_heap_sorted(max_heap, max_heap=True))

    # Test get_top_n()
    print("\nTesting get_top_n()...")
    print("Top 3 Elements in MinHeap:", heap_utils.get_top_n(min_heap, 3))
    print("Top 3 Elements in MaxHeap:", heap_utils.get_top_n(max_heap, 3))

    # Test heap_sort()
    print("\nTesting heap_sort()...")
    sorted_list_asc = heap_utils.heap_sort([10, 3, 5, 1, 7])
    sorted_list_desc = heap_utils.heap_sort([10, 3, 5, 1, 7], descending=True)

    print("Sorted List (Ascending):", sorted_list_asc)
    print("Sorted List (Descending):", sorted_list_desc)

    # Test contains()
    print("\nTesting contains()...")
    print("MinHeap contains 4?", heap_utils.contains(min_heap, 4))
    print("MaxHeap contains 10?", heap_utils.contains(max_heap, 10))

    # Test size() and is_empty()
    print("\nTesting size() and is_empty()...")
    print("MinHeap Size:", heap_utils.size(min_heap))
    print("MaxHeap Size:", heap_utils.size(max_heap))
    print("MinHeap is Empty?", min_heap.is_empty())
    print("MaxHeap is Empty?", max_heap.is_empty())

    # Test sum_heap()
    print("\nTesting sum_heap()...")
    print("Sum of MinHeap Elements:", heap_utils.sum_heap(min_heap))
    print("Sum of MaxHeap Elements:", heap_utils.sum_heap(max_heap))

    # Test max_in_heap() & min_in_heap()
    print("\nTesting max_in_heap() & min_in_heap()...")
    print("Max in MinHeap:", heap_utils.max_in_heap(min_heap))
    print("Min in MinHeap:", heap_utils.min_in_heap(min_heap))
    print("Max in MaxHeap:", heap_utils.max_in_heap(max_heap))
    print("Min in MaxHeap:", heap_utils.min_in_heap(max_heap))

    # Test clear_heap()
    print("\nTesting clear_heap()...")
    heap_utils.clear_heap(min_heap)
    heap_utils.clear_heap(max_heap)

    print("MinHeap after clear:", min_heap.get_elements())
    print("MaxHeap after clear:", max_heap.get_elements())

if __name__ == "__main__":
    test_heap()
