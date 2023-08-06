import unittest
import heapq


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_01(self):
        odd = [1, 3, 5, 7, 9]
        even = [2, 4, 6, 8, 10]

        heapq.heapify(odd)
        heapq.heapify(even)
        self.assertEqual([1, 3, 5, 7, 9], odd)
        self.assertEqual([2, 4, 6, 8, 10], even)

        p = list(heapq.merge(odd, even))

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], p)



if __name__ == '__main__':
    unittest.main()
