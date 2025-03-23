from collections import deque

def get_max(queue, visualize=False):
    """Returns the maximum integer value in the queue."""
    numbers = [x for x in queue.get_elements() if isinstance(x, (int, float))]
    max_value = max(numbers, default="No numbers in queue")

    if visualize:
        print(f"Max value: {max_value}")

    return max_value

def get_min(queue, visualize=False):
    """Returns the minimum integer value in the queue."""
    numbers = [x for x in queue.get_elements() if isinstance(x, (int, float))]
    min_value = min(numbers, default="No numbers in queue")

    if visualize:
        print(f"Min value: {min_value}")

    return min_value

def get_sum(queue, visualize=False):
    """Returns the sum of all numerical values in the queue."""
    total = sum(x for x in queue.get_elements() if isinstance(x, (int, float)))

    if visualize:
        print(f"Sum: {total}")

    return total

def get_avg(queue, visualize=False):
    """Returns the average of all numerical elements in the queue."""
    numbers = [x for x in queue.get_elements() if isinstance(x, (int, float))]
    avg_value = sum(numbers) / len(numbers) if numbers else 0

    if visualize:
        print(f"Average: {avg_value}")

    return avg_value

def reverse_queue(queue, inplace=False, visualize=False):
    """Reverses the queue."""
    reversed_queue = deque(reversed(queue.get_elements()))

    if inplace:
        queue._elements = reversed_queue  # Directly update the private attribute

    if visualize:
        print(f"Reversed Queue: {list(reversed_queue)}")

    return reversed_queue

def sort_queue(queue, descending=False, inplace=False, visualize=False):
    """Sorts the queue in ascending or descending order."""
    sorted_elements = sorted(queue.get_elements(), reverse=descending)

    if inplace:
        queue._elements = deque(sorted_elements)

    if visualize:
        order = "descending" if descending else "ascending"
        print(f"Sorted Queue ({order}): {list(sorted_elements)}")

    return deque(sorted_elements)

def clear_queue(queue, visualize=False):
    """Clears all elements from the queue."""
    queue.clear()

    if visualize:
        print("Queue cleared")

    return "Queue cleared"

def contains(queue, item, visualize=False):
    """Checks if the queue contains a specific item."""
    found = item in queue.get_elements()

    if visualize:
        print(f"Queue contains {item}: {found}")

    return found
