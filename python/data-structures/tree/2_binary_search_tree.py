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

    def inorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self, data):

        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def delete(self, val):
        if val < self.data and self.left:
            self.left = self.left.delete(val)
        elif val > self.data and self.right:
            self.right = self.right.delete(val)
        else:
            # 0 children
            if not self.left and not self.right:
                return None
            # 1 child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # 2 children
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    if elements:
        root = BinaryTreeNode(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root
    else:
        print('No elements given')
    return


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        numbers = [17, 4, 1, 20, 9, 23, 18, 22, 34]

        numbers_tree = build_tree(numbers)
        self.assertEqual([1, 4, 9, 17, 18, 20, 22, 23, 34], numbers_tree.inorder_traversal())

        self.assertEqual(False, numbers_tree.search(21))
        self.assertEqual(True, numbers_tree.search(22))
        self.assertEqual(1, numbers_tree.find_min())
        self.assertEqual(34, numbers_tree.find_max())
        numbers_tree.delete(34)
        self.assertEqual([1, 4, 9, 17, 18, 20, 22, 23], numbers_tree.inorder_traversal())

    def test_2(self):

        x = []

        if x:
            print('Not empty')
        else:
            print('Empty')

        y = None
        if y:
            print('Not none')
        else:
            print('None')


if __name__ == '__main__':
    unittest.main()
