import tree
import unittest


class TestTree(unittest.TestCase):

    def test_add_to_del(self):
        checktree = tree.BinaryTree()
        checktree.add(23)
        checktree.add(65)
        checktree.add(12)
        checktree.add(80)
        checktree.delete(23)
        checktree.delete(65)
        checktree.delete(12)
        checktree.delete(80)
        self.assertTrue(checktree.is_empty())

    #ok
    def test_find(self):
        checktree = tree.BinaryTree()
        checktree.add(32)
        self.assertTrue(checktree.find(32))
        self.assertFalse(checktree.find(123))


if __name__ == '__main__':
    unittest.main()
