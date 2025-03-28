class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_single = 0
        total = 0
        for num in nums:
            total += num
            if num < 10:
                sum_single += num
        return 2 * sum_single != total