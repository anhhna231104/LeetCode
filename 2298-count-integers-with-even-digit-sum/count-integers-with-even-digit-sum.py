class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 2:
            return 0
            
        count = 0
        for i in range(2, num + 1):
            total = 0
            dummy = i
            while dummy > 0:
                tmp = dummy % 10
                total += tmp
                dummy //= 10
            
            if total % 2 == 0:
                count += 1
        
        return count
            
        