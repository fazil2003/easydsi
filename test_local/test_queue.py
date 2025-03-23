from easydsi.queue import Queue
from easydsi.queue.queue_utils import get_max, get_min, get_sum, reverse_queue

q = Queue([1, 3, 5, 7])
q.enqueue(9)
q.display()  # Output: Queue: [1, 3, 5, 7, 9]
q.dequeue()
print(get_max(q))  # Output: 9
print(reverse_queue(q))  # Output: deque([9, 7, 5, 3])
