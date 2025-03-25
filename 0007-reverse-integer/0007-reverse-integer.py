class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x < 0:
            is_neg = True
        else:
            is_neg = False
        num_input = abs(x)  
        while num_input > 0:
            tmp = num_input % 10
            rev = rev * 10 + tmp
            num_input = num_input//10
        if rev < -2**31 or rev > 2**31 -1:
            return 0
        if is_neg:
            return -rev
        return rev

        