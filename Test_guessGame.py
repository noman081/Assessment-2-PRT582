import unittest
from guessGame import guessGame

class TestAssignment1(unittest.TestCase):
    def setUp(self):
        self.assignment = guessGame()

    def test_generate_random_number(self):
        random_number = self.assignment.generate_random_number()
        self.assertTrue(1000 <= random_number <= 9999)

    def test_check_guess_Equal(self):
        # four matched but two in position and two out of position with the random number to the guess number
        hints = self.assignment.check_guess([1, 2, 3, 4], [1, 3, 2, 4])
        self.assertEqual(hints, ['o', 'x', 'x', 'o'])

        # nothing matched with the random number to the guess number
        hints = self.assignment.check_guess([7, 8, 5, 0], [1, 3, 2, 4])
        self.assertEqual(hints, ['_', '_', '_', '_'])
        
        # three matched and in position and the otherone not guessed well with the random number to the guess number
        hints = self.assignment.check_guess([6, 5, 5, 1], [6, 5, 5, 0])
        self.assertEqual(hints, ['o', 'o', 'o', '_'])

        # All matched with the random number to the guess number
        hints = self.assignment.check_guess([5, 0, 0, 6], [5, 0, 0, 6])
        self.assertEqual(hints, ['o', 'o', 'o', 'o'])

        # three matched but in wrong position with the random number to the guess number
        hints = self.assignment.check_guess([7, 8, 5, 0], [2,7,8,5])
        self.assertEqual(hints, ['_', 'x', 'x', 'x'])

        # all matched but all are in wrong position with the random number to the guess number
        hints = self.assignment.check_guess([8, 1, 9, 3], [1, 3, 8, 9])
        self.assertEqual(hints, ['x', 'x', 'x', 'x'])


    def test_check_guess_notEqual(self):
        hints = self.assignment.check_guess([1,2,3,4],[1,2,3,5])
        self.assertNotEqual(hints,['o','o','o','o'])

        hints = self.assignment.check_guess([1,2,3,4],[1,2,3,5])
        self.assertNotEqual(hints,['o','o','o','x'])

        hints = self.assignment.check_guess([1,2,3,4],[1,2,3,4])
        self.assertNotEqual(hints,['x','x','x','x'])

        hints = self.assignment.check_guess([1,2,3,4],[0,0,0,0])
        self.assertNotEqual(hints,['o','x','x','o'])
        
    def test_check_guess_invalid_guess(self):
        # Test when guess has non-numeric characters
        hints = self.assignment.check_guess([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
        self.assertEqual(hints, ['_','_','_','_'])

if __name__ == '__main__':
    unittest.main()        