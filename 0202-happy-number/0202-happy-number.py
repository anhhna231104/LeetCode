class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ck_arr = []
        while n!=1:
            sum = 0
            while n > 0:
                digit = n%10
                sum += digit*digit
                n//=10
            if sum in ck_arr:
                return False
            ck_arr.append(sum)
            n = sum
        return True
        