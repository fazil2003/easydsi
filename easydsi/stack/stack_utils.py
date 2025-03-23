from .stack import Stack

def reverse_stack(stack):
    """
    Reverse the order of elements in a stack.

    Args:
        stack (Stack): The stack to be reversed.

    Returns:
        Stack: A new stack with elements in reversed order.
    """
    temp_list = list(stack)  # Convert stack to list (bottom to top)
    temp_list.reverse()  # Reverse list in-place (O(n))
    
    reversed_stack = Stack()
    for item in temp_list:
        reversed_stack.push(item)  # O(1) per push
    
    return reversed_stack

def sort_stack(stack):
    """
    Sort a stack in ascending order.

    Uses a temporary stack to maintain sorted order.

    Args:
        stack (Stack): The stack to be sorted.

    Returns:
        Stack: A new stack with elements sorted in ascending order.
    """
    temp_list = list(stack)  # Convert stack to list
    temp_list.sort()  # Sort list (O(n log n))

    sorted_stack = Stack()
    for item in temp_list:
        sorted_stack.push(item)  # O(1) per push
    
    return sorted_stack

def duplicate_stack(stack):
    """
    Create a duplicate of a stack without modifying the original.

    Args:
        stack (Stack): The stack to be duplicated.

    Returns:
        Stack: A duplicate stack with identical elements.
    """
    duplicate = Stack()
    for item in stack:
        duplicate.push(item)  # Copy elements one by one
    
    return duplicate

def sum_stack(stack):
    """
    Compute the sum of all elements in a stack.

    Args:
        stack (Stack): The stack of numerical values.

    Returns:
        int/float: The sum of all stack elements.
    """
    return sum(stack) if not stack.is_empty() else 0

def max_in_stack(stack):
    """
    Find the maximum value in a stack.

    Args:
        stack (Stack): The stack of numerical values.

    Returns:
        int/float: The maximum value in the stack.
    """
    return max(stack) if not stack.is_empty() else float('-inf')

def min_in_stack(stack):
    """
    Find the minimum value in a stack.

    Args:
        stack (Stack): The stack of numerical values.

    Returns:
        int/float: The minimum value in the stack.
    """
    return min(stack) if not stack.is_empty() else float('inf')

def merge_stacks(stack1, stack2):
    """
    Merge two stacks into one, maintaining order.

    Elements of `stack1` will be below elements of `stack2` in the merged stack.

    Args:
        stack1 (Stack): The first stack.
        stack2 (Stack): The second stack.

    Returns:
        Stack: A new stack containing elements of both stacks.
    """
    merged_stack = Stack()

    # Push elements from stack1
    for item in stack1:
        merged_stack.push(item)

    # Push elements from stack2
    for item in stack2:
        merged_stack.push(item)

    return merged_stack

def is_balanced(expression):
    """
    Check if a given expression has balanced parentheses.

    Args:
        expression (str): The string containing brackets/parentheses.

    Returns:
        bool: True if balanced, False otherwise.
    """
    stack = Stack()
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return False

    return stack.is_empty()

def remove_duplicates(stack):
    """
    Remove duplicate elements from a stack while maintaining order.

    Args:
        stack (Stack): The stack with possible duplicate values.

    Returns:
        Stack: A new stack without duplicates.
    """
    seen = set()
    unique_stack = Stack()

    for item in stack:
        if item not in seen:
            seen.add(item)
            unique_stack.push(item)

    return reverse_stack(unique_stack)  # Reverse to maintain original order
