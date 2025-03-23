from easydsi.stack.stack import Stack
from easydsi.stack.stack_utils import reverse_stack

# Create a stack and perform operations
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # Output: 20

# Test stack reversal
s.push(30)
s.push(40)
reversed_s = reverse_stack(s)
print(reversed_s.pop())  # Output: 30