class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum_digit = 0
        tmp = x 
        while tmp > 0:
            sum_digit += tmp%10
            tmp//=10
        if x%sum_digit == 0:
            return sum_digit
        return -1

        