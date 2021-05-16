import unittest
from next_largest import Solution


class NextLarger(unittest.TestCase):
    def test_next_larger_element(self):
        ob = Solution()
        self.assertEqual(ob.next_larger_element([2, 3, 1]), [3, -1, -1])
        self.assertEqual(ob.next_larger_element([2, 0, 18, 48]), [18, 18, 48, -1])
        self.assertEqual(ob.next_larger_element([20, -3, -1, -8]), [-1, -1, -1, -1])
        self.assertEqual(ob.next_larger_element([32, 34, 101, 10, 908]), [34, 101, 908, 908, -1])
        self.assertEqual(ob.next_larger_element([-12, 30]), [30, -1])
        self.assertEqual(ob.next_larger_element([10, 53, 121, 0, 99, 10001, 2560]), [53, 121, 10001, 99, 10001, -1, -1])
        self.assertEqual(ob.next_larger_element([2]), [-1])
        self.assertEqual(ob.next_larger_element([0, -102]), [-1, -1])
        self.assertEqual(ob.next_larger_element([92, 113, 19, 438, 131245, 65, 23, 90, -1]), [113, 438, 438, 131245, -1, 90, 90, -1, -1])
        self.assertEqual(ob.next_larger_element([-1]), [-1])
        self.assertEqual(ob.next_larger_element([0]), [-1])
        self.assertEqual(ob.next_larger_element([]), [])


if __name__ == '__main__':
    unittest.main()

