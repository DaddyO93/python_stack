import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add_nums(self, num, *nums):
        for i in nums:
            self.result+=i
        self.result+=num
        return self
    
    def subtract_nums(self, num, *nums):
        for i in nums:
            self.result-=i
        self.result-=num
        return self
    

class MathDojoTests(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()
        print("Running SetUp ...")
    
    def tearDown(self):
        print("Tearing Down ...")
        
    def testOne(self):
        self.assertEqual(self.md.add_nums(3,3).result, 6)
        
    def testTwo(self):
        self.assertNotEqual(self.md.add_nums(3,4).result, 6)
    
    def testThree(self):
        self.assertEqual(self.md.subtract_nums(3,2).result,1)
    
    def testFour(self):
        self.assertNotEqual(self.md.subtract_nums(3,2).result,1)
        

if __name__ == '__main__':
    unittest.main()