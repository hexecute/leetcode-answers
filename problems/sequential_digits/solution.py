import math

class Solution(object):
    def generateSequentialNumber(self, first_digit, number_of_digits):
        rv = 0
        digit = first_digit
        for n in range(number_of_digits, 0, -1):
            if digit > 9:
                return -1
            rv += digit * (10**(n - 1))
            digit = digit + 1
        return rv
        
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        def get_number_of_digits(n):
            rv = 0
            while n >= 1:
                n = n /10
                rv += 1
            return rv
        
        low_digits = get_number_of_digits(low)
        high_digits = get_number_of_digits(high)
        
        rv = []
        for number_of_digits in range(low_digits, high_digits + 1):
            for first_digit in range(1, 10):
                test_number = self.generateSequentialNumber(first_digit, number_of_digits)
                if test_number >= low and test_number <= high:
                    rv.append(test_number)
        return rv
    