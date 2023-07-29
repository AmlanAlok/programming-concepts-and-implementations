import unittest
from collections import deque

"""
https://docs.python.org/3/library/collections.html#collections.deque
https://realpython.com/python-deque/

1. pronounced “deck” and is short for “double-ended queue”
2. Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

"""


class MyTestCase(unittest.TestCase):

    def test_1(self):
        stack = deque()
        stack.append(1)
        stack.append(2)
        stack.append(3)
        stack.append('a')

        self.assertEqual(deque([1, 2, 3, 'a']), stack)
        # self.assertEqual([1, 2, 3, 'a'], stack)       # list != deque
        self.assertEqual([1, 2, 3, 'a'], list(stack))

        stack.append(True)
        stack.append([99, 100])
        self.assertEqual(deque([1, 2, 3, 'a', True, [99, 100]]), stack)
        stack.append({'a': 98, 98: 'b'})
        stack.appendleft((97, 96))
        self.assertEqual(deque([(97, 96), 1, 2, 3, 'a', True, [99, 100], {'a': 98, 98: 'b'}]), stack)

        self.assertEqual(1, stack.count('a'))
        self.assertEqual(1, stack.count(3))
        # self.assertEqual(1, stack.count(1))       # I do not understand this

        self.assertEqual({'a': 98, 98: 'b'}, stack.pop())
        self.assertEqual((97, 96), stack.popleft())

        self.assertEqual(deque([1, 2, 3, 'a', True, [99, 100]]), stack)
        stack.clear()
        self.assertEqual(deque([]), stack)


if __name__ == '__main__':
    unittest.main()

"""
1. Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.
2. Bounded length deques provide functionality similar to the tail filter in Unix


"""