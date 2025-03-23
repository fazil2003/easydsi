import unittest
from easydsi.stack.stack import Stack
from easydsi.stack.stack_exceptions import StackUnderflowError
from easydsi.stack.stack_utils import reverse_stack

class TestStack(unittest.TestCase):

    def test_push_and_pop(self):
        s = Stack()
        s.push(10)
        s.push(20)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)

    def test_peek(self):
        s = Stack()
        s.push(15)
        self.assertEqual(s.peek(), 15)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(5)
        self.assertFalse(s.is_empty())

    def test_size(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.size(), 3)

    def test_clear(self):
        s = Stack()
        s.push(100)
        s.push(200)
        s.clear()
        self.assertTrue(s.is_empty())

    def test_pop_empty_stack(self):
        s = Stack()
        with self.assertRaises(StackUnderflowError):
            s.pop()

    def test_reverse_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        reversed_s = reverse_stack(s)
        self.assertEqual(reversed_s.pop(), 1)
        self.assertEqual(reversed_s.pop(), 2)
        self.assertEqual(reversed_s.pop(), 3)

if __name__ == '__main__':
    unittest.main()
