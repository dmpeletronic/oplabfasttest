import unittest

import sys
sys.path.append('src')

from searchsequence import searchsequence

class TestStringMethods(unittest.TestCase):

    def test_searchsequence(self):
        nlist = [1,2,3,4,5,6,7,8]
        self.assertEqual(searchsequence.searchsequence(nlist, 1), (0,0))
        self.assertEqual(searchsequence.searchsequence(nlist, 2), (1,1))
        self.assertEqual(searchsequence.searchsequence(nlist, 3), (0,1))
        self.assertEqual(searchsequence.searchsequence(nlist, 4), (3,3))
        self.assertEqual(searchsequence.searchsequence(nlist, 5), (1,2))
        self.assertEqual(searchsequence.searchsequence(nlist, 6), (0,2))
        self.assertEqual(searchsequence.searchsequence(nlist, 7), (2,3))
        self.assertEqual(searchsequence.searchsequence(nlist, 8), (7,7))
        self.assertEqual(searchsequence.searchsequence(nlist, 9), (1,3))
        self.assertEqual(searchsequence.searchsequence(nlist, 10), (0,3))
        self.assertEqual(searchsequence.searchsequence(nlist, 19), (-1,1))

    def test_searchsequence2(self):
        nlist = [1, 2, 3, 4]
        self.assertEqual(searchsequence.searchsequence(nlist, 15), (-1,1))
        
    def test_searchsequence3(self):
        nlist = [4, 3, 10, 2, 8]
        self.assertEqual(searchsequence.searchsequence(nlist, 12), (2,3))

    def test_searchsequence4(self):
        nlist = [250]
        self.assertEqual(searchsequence.searchsequence(nlist, 250), (0,0))
        self.assertEqual(searchsequence.searchsequence(nlist, 249), (-1,1))
        self.assertEqual(searchsequence.searchsequence(nlist, 251), (-1,1))
        self.assertEqual(searchsequence.searchsequence(nlist, 0), (-1,1))
        self.assertEqual(searchsequence.searchsequence(nlist, -1), (-1,1))

    def test_searchsequence5(self):
            nlist = [1]*100
            self.assertEqual(searchsequence.searchsequence(nlist, 100), (0,99))
            self.assertEqual(searchsequence.searchsequence(nlist, 50), (0,49))
            self.assertEqual(searchsequence.searchsequence(nlist, 101), (-1,1))
    
    def test_searchsequence6(self):
            nlist = [100]*100
            self.assertEqual(searchsequence.searchsequence(nlist, 100), (0,0))
            self.assertEqual(searchsequence.searchsequence(nlist, 10000), (0,99))
            self.assertEqual(searchsequence.searchsequence(nlist, 5000), (0,49))
            self.assertEqual(searchsequence.searchsequence(nlist, 10100), (-1,1))

    def test_searchsequence7(self):
            nlist = [250]*100
            self.assertEqual(searchsequence.searchsequence(nlist, 250), (0,0))
            self.assertEqual(searchsequence.searchsequence(nlist, 250*100), (0,99))
            self.assertEqual(searchsequence.searchsequence(nlist, 250*50), (0,49))
            self.assertEqual(searchsequence.searchsequence(nlist, 250*101), (-1,1))


if __name__ == '__main__':
    unittest.main()
    