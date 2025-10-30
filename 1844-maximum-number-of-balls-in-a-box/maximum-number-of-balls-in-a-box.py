class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box = dict()

        for i in range(lowLimit, highLimit + 1):
            total, dummy = 0, i
            
            while dummy > 0:
                tmp = dummy % 10
                total += tmp
                dummy //= 10
            
            if total not in box:
                box[total] = 1
            else:
                box[total] += 1
            total = 0
        
        return max(box.values())
        