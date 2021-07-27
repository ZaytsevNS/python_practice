# Условие:

# Ваша задача — написать функцию, которая проверит, все ли значения увеличиваются на один

# Пример:
# increasing([-1, 0, 1, 2, 3]) -> True
# increasing([-1, 0, 1, 3, 4])) -> False
# increasing([0, 1]) -> True
# increasing([1, 0]) -> False

import unittest


def increasing(arr: list) -> bool:
    # First way
    if arr == list(range(arr[0], arr[-1]+1)):
        return True
    return False
    
    # Second way
    # for i in range(len(arr)-1):
        # if arr[i + 1] - arr[i] == 1:
            # continue
        # else:
            # return False
    # return True
                
class TestIncreasing(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, increasing([-1, 0, 1, 2, 3]))
        self.assertEqual(True, increasing([0, 1]))
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, increasing([-1, 0, 1, 3, 4]))
        self.assertEqual(False, increasing([1, 0]))
                
if __name__ == '__main__':
    unittest.main()
        