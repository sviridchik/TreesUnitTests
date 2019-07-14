import solution
import unittest

class TestPython(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_addFirst_and_del_first(self):
        checklist = solution.LinkedList()
        checklist.addFirst(1)
        checklist.addFirst(2)
        checklist.addFirst(3)
        self.assertEqual(checklist.del_first(), 3)
        self.assertEqual(checklist.del_first(), 2)
        self.assertEqual(checklist.del_first(), 1)
        self.assertFalse(checklist.empty())

    def addAfter_and_test_delAfter(self):
        checklist = solution.LinkedList()
        checklist.add(0)
        checklist.addAfter(0, 1)
        checklist.addAfter(0)
        checklist.del_first()
        self.assertFalse(checklist.empty())

    def test_destroy(self):
        checklist = solution.LinkedList()
        checklist.add(0)
        checklist.add(1)
        checklist.add(2)
        checklist.destroy()
        self.assertTrue(checklist.empty())

    def test_len_and_add(self):
        checklist = solution.LinkedList()
        checklist.add(0)
        checklist.add(1)
        checklist.add(2)
        self.assertEqual(checklist.len, 3, "Wrong lenght")

    def test_findIndexByValue(self):
        checklist = solution.LinkedList()
        checklist.add(0)
        checklist.add(1)
        checklist.add(2)
        self.assertEqual(checklist.findIndexByValue(1), 1, "wrong index")

    def test_bub_sort(self):
        checklist = solution.LinkedList()
        checklist.add(5)
        checklist.add(1)
        checklist.add(2)
        checklist.bub_sort()
        self.assertEqual(checklist.del_first(), 1, "Wrong first")
        self.assertEqual(checklist.del_first(), 2, "Wrong second")
        self.assertEqual(checklist.del_first(), 5, "Wrong last")


if __name__ == '__main__':
    unittest.main()