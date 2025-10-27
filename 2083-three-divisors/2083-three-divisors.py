class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 2
        for i in range(2, n):
            if n%i == 0:
                count += 1
        return count == 3 
        