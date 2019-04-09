import unittest
from lab1 import *

#will add more cases later
 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests if the function finds the maximum number in a list
        correctly."""
        tlist = [1, 2, 3, 4, 5] #sorted list with no repeats
        tlist2 = [98, 9, 0, 3, 98, 33, 69, 69, 33] #unsorted list w/ repeats
        tlist3 = [] #empty list
        tlist4 = None #when None is passed into the function
        self.assertEqual(max_list_iter(tlist), 5)
        self.assertEqual(max_list_iter(tlist2), 98)
        self.assertEqual(max_list_iter(tlist3), None)
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist4)

    def test_reverse_rec(self):
        """Tests if the function reverses a list of numbers correctly."""
        list1 = [123, 101, 202, 357] #list with no repeats
        list2 = [8, 9, 10, 22, 25, 121, 490] #list with no repeats
        list3 = [0] #list with length 1
        list4 = [] #list with length 0
        list5 = None #when None is passed into the function
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec(list1), [357, 202, 101, 123])
        self.assertEqual(reverse_rec(list2), [490, 121, 25, 22, 10, 9, 8])
        self.assertEqual(reverse_rec(list3), [0])
        self.assertEqual(reverse_rec(list4), [])
        with self.assertRaises(ValueError):
            reverse_rec(list5)

    def test_bin_search(self):
        """Tests to see if function finds index of target value in a list
        properly with binary search."""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        list2 = [3, 6, 9]
        list3 = [2, 5]
        list4 = [420]
        list5 = []
        list6 = [0, 0, 1, 2, 3, 3, 4]
        self.assertEqual(bin_search(4, low, high, list_val), 4)
        self.assertEqual(bin_search(6, low, high, list_val), None)
        self.assertEqual(bin_search(4, high, low, list_val), None)
        self.assertEqual(bin_search(0, low, high, list_val), 0)
        self.assertEqual(bin_search(10, low, high, list_val), 8)
        self.assertEqual(bin_search(2, low, high, list_val), 2)
        self.assertEqual(bin_search(9, low, high, list_val), 7)
        self.assertEqual(bin_search(3, low, len(list2) - 1, list2), 0)
        self.assertEqual(bin_search(6, low, len(list2) - 1, list2), 1)
        self.assertEqual(bin_search(9, low, len(list2) - 1, list2), 2)
        self.assertEqual(bin_search(2, low, len(list3) - 1, list3), 0)
        self.assertEqual(bin_search(5, low, len(list3) - 1, list3), 1)
        self.assertEqual(bin_search(420, low, len(list4) - 1, list4), 0)
        self.assertEqual(bin_search(0, low, len(list5) - 1, list5), None)
        self.assertEqual(bin_search(3, low, len(list6) - 1, list6), 4)
        with self.assertRaises(ValueError): #check for exception
            bin_search(4, 0, 10, None) 

if __name__ == "__main__":
        unittest.main()

    
