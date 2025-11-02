class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = float('inf')

        for n in nums:
            closest = min(abs(n - 0), closest)

        return closest if closest in nums else -closest
        