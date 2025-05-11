import unittest

class Testing(unittest.TestCase):
    def testEdgeCases(self):
        self.assertFalse(isPowerOfTwo(0))    
        self.assertFalse(isPowerOfTwo(-1))    
        self.assertFalse(isPowerOfTwo(0.1))
        self.assertFalse(isPowerOfTwo(True))
        self.assertFalse(isPowerOfTwo('hay'))
    def testCleanInputTrue(self):
        self.assertTrue(isPowerOfTwo(1))    
        self.assertTrue(isPowerOfTwo(2))    
        self.assertTrue(isPowerOfTwo(4))    
        self.assertTrue(isPowerOfTwo(256))    
        self.assertTrue(isPowerOfTwo(1024))    
    def testCleanInputFalse(self):
        self.assertFalse(isPowerOfTwo(3))    
        self.assertFalse(isPowerOfTwo(5))    
        self.assertFalse(isPowerOfTwo(78))    
        self.assertFalse(isPowerOfTwo(6))    
        self.assertFalse(isPowerOfTwo(1025))    


def isPowerOfTwo(n: int) -> bool:
    if type(n) != int or n <= 0: return False
    return not n & (n - 1) > 0

if __name__ == '__main__':
    unittest.main()
