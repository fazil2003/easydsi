from easydsi.stack import Stack
from easydsi.stack.stack_utils import (
    reverse_stack, sort_stack, merge_stacks,
    is_balanced, remove_duplicates, sum_stack,
    max_in_stack, min_in_stack
)

stack1 = Stack()
stack1.push(3)
stack1.push(1)
stack1.push(4)
stack1.push(2)

stack2 = Stack()
stack2.push(10)
stack2.push(5)

print(sort_stack(stack1))  # Stack([1, 2, 3, 4])
print(reverse_stack(stack1))  # Stack([4, 3, 2, 1])
print(merge_stacks(stack1, stack2))  # Stack([3, 1, 4, 2, 10, 5])

print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False

print(remove_duplicates(merge_stacks(stack1, stack2)))  # Stack without duplicates

print(sum_stack(stack1))  # Sum of all elements
print(max_in_stack(stack1))  # Max element
print(min_in_stack(stack1))  # Min element
