class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        tmp = abs(x)
        while tmp != 0:
            rev = (rev*10) + (tmp%10)
            tmp = tmp//10
        if rev == x:
            return True
        else:
            return False
        