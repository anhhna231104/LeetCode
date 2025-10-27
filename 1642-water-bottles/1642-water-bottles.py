class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # test syncing
        res, emptyBottles = 0, 0
        while numBottles > 0:
            res += numBottles
            emptyBottles += numBottles
            numBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange

        return res
        