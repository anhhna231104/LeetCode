class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        if num1 == 0 or num2 == 0:
            return 0

        res = 0
        flag = True

        while flag:
            if num1 > num2:
                num1 = num1 - num2
                res += 1
            else:
                num2 = num2 - num1
                res += 1

            if num1 == 0 or num2 == 0:
                flag = False
        
        return res

        