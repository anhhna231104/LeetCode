class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        tmp = num
        while 1: 
            sum += tmp%10
            tmp//=10
            if tmp==0:
                if sum//10==0:
                    return sum
                else:
                    tmp = sum
                    sum = 0
        return 0
                                                                                  
        