from scripts.pythonBasics import make_it_one
import unittest


class TestMakeItOne (unittest.TestCase):

    def test_number_of_operations(self):
        obj = make_it_one.Solution()
        self.assertEqual(obj.number_of_operations(15), 3)
        self.assertEqual(obj.number_of_operations(-3), 0)
        self.assertEqual(obj.number_of_operations(33), 1)
        self.assertEqual(obj.number_of_operations(2049), 1)
        self.assertEqual(obj.number_of_operations(1024), 10)
        self.assertEqual(obj.number_of_operations(1125899906842624), 50)
        self.assertEqual(obj.number_of_operations(9223372036854775808), 63)
        self.assertEqual(obj.number_of_operations(106), 4)
        self.assertRaises(ValueError, obj.number_of_operations, 'k')


if __name__ == '__main__':
    unittest.main()
