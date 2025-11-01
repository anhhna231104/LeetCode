class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn, mx = min(nums), max(nums)
        res = 0

        for i in nums:
            if i > mn and i < mx:
                res += 1
        
        return res
        