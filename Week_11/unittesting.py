import unittest

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x/y

def remainder(x,y):
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x%y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)

    def test_substract(self):
        self.assertEqual(substract(6,3),3)
        self.assertEqual(substract(0,0),0)

    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(-1,1),-1)

    def test_divide(self):
        self.assertEqual(divide(6,3),2)
        with self.assertRaises(ZeroDivisionError):
            divide(1,0)

    def test_remainder(self):
        self.assertEqual(remainder(5,2),1)
        self.assertEqual(remainder(4,2),0)
        with self.assertRaises(ZeroDivisionError):
            remainder(1,0)

            

if __name__ == '__main__':
    unittest.main()
        