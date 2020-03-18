import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class LargestPalindromeProduct(IEulerSolution):
    """
    Solution to problem 4
    A palindromic number reads the same both ways. The largest palindrome made from the product 
    of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers
    """

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        result = 0

        for number1 in range (100, 1000):
            for number2 in range (100, 1000):
                product = number1 * number2
                if (MathLibrary.reverse_digits(product) == product) & (product > result):
                    result = product

        return result