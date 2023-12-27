import unittest
from first_task_generator import fibonacci_generator
from second_task_generator import generate_palindromic_numbers

class TestFibonachiGenerator(unittest.TestCase):

    def test_fibonachi_generator(self):
        gen = fibonacci_generator(5)
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)

        
        with self.assertRaises(StopIteration):
            next(gen)


class TestPalindromGenerator(unittest.TestCase):

    def test_palindrom_generator(self):
        gen = generate_palindromic_numbers()
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 4)

       
if __name__ == '__main__':
    unittest.main()