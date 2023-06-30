import unittest


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        # do nothing
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
