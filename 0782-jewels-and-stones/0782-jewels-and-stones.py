class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum = 0
        for i in range(len(jewels)):
            sum+=stones.count(jewels[i])
        return sum
            

        