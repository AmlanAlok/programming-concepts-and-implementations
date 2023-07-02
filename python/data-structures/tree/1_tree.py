import unittest


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        gap = ' ' * 2 * self.get_level() + '|--'
        print(gap + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        print('Starting')
        root = TreeNode('Hiruzen Sarutobi')

        tsunade = TreeNode('Tsunade')
        jiraiya = TreeNode('Jiraiya')
        orochimaru = TreeNode('Orochimaru')

        root.add_child(tsunade)
        root.add_child(jiraiya)
        root.add_child(orochimaru)

        minato = TreeNode('Minato')
        anko = TreeNode('Anko')
        sizune = TreeNode('Sizune')

        jiraiya.add_child(minato)
        tsunade.add_child(sizune)
        orochimaru.add_child(anko)

        kakashi = TreeNode('Kakashi')
        obito = TreeNode('Obito')
        rin = TreeNode('Rin')

        minato.add_child(kakashi)
        minato.add_child(obito)
        minato.add_child(rin)

        naruto = TreeNode('Naruto')
        sasuke = TreeNode('Sasuke')
        sakura = TreeNode('Sakura')

        kakashi.add_child(naruto)
        kakashi.add_child(sasuke)
        kakashi.add_child(sakura)

        root.print_tree()

        print('End')


if __name__ == '__main__':
    unittest.main()
