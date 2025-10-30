class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        while k > 0:
            taken = max(gifts)
            i = gifts.index(taken)
            gifts[i] = int(floor(sqrt(taken)))
            k -= 1

        return sum(gifts)
        