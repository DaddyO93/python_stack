# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False

def reverseList(list_A):
    for i in range(len(list_A)-1, -1, -1):
        list_A.append(list_A[i])
        list_A.pop(i)
    return list_A

def sumNums(a,b):
    total = a+b
    if total%2==0:
        return True
    else:
        return False

def inList(a,b):
    b.append(a)
    return a

# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(reverseList(["abc", True, 5, [1,2,3,4]]), [[1,2,3,4], 5, True, "abc"])

    def testThree(self):
        self.assertNotEqual(reverseList(["abc", True, 5, [1,2,3,4]]), ["abc", True, 5, [1,2,3,4]])
        
    def testFour(self):
        self.assertTrue(sumNums(2,2))
        
    def testFive(self):
        self.assertFalse(sumNums(2,3))
        
    def testSix(self):
        list_1 = [1,2,3,4]
        self.assertIn(inList(5,list_1), list_1)

    def testSeven(self):
        self.assertNotIn(inList("a", [1,2,3,4])

    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests
