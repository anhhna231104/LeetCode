class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        current = 1
        direction = 1
        for sec in range(time):
            current+=direction
            if current == n:
                direction = -1
            elif current == 1:
                direction = 1
        return current