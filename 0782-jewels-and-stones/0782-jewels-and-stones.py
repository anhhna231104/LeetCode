class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jelList = list(jewels)
        sum = 0
        for i in range(len(jelList)):
            sum+=stones.count(jelList[i])
        return sum
            

        