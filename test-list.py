import unittest
from sort_list import list_sort

class listsortingTest(unittest.TestCase):

    def test_emptylist(self):
        self.assertEqual(list_sort([]), 'this is an empty list')

    def test_sortedlist(self):
        self.assertEqual([5,6,7,'y','u','s']), {'evens': []})
        self.assertEqual((list_sort([5,6,7,'y','u','s']),{'odds': [5,7], 'evens': [6], 'chars': ['y', 'u','s']}))

if __name__ == '__main__':
    unittest.main()
