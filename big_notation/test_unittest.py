import unittest
from  second_task import finding_number

class TestUnittest(unittest.TestCase):
    def test_finding_numbers(self):
        self.assertEqual(finding_number([1,1,2,3,4,7,1,6,1]), 4)
        


if __name__ == '__main__':
    unittest.main()