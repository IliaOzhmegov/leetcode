from Solution import Solution
import unittest
import json
import os


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.filepaths = os.listdir('tests')

    def test_findMaximizedCapital_from_dict(self):
        args = {
            "k": 1,
            "w": 2,
            "profits": [1, 2, 3],
            "capital": [1, 1, 2]
        }

        self.assertEqual(self.s.findMaximizedCapital(**args), 5)

    def test_findMaximizedCapital(self):
        for filepath in self.filepaths:
            filename = os.path.join('tests', filepath)
            with open(filename, 'r') as f:
                kwars = json.load(f)
                self.assertEqual(self.s.findMaximizedCapital(**kwars['payload']), kwars['answer'])


if __name__ == '__main__':
    unittest.main()



