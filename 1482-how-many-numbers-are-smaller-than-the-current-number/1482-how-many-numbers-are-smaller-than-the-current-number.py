class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = dict()
        for i,num in enumerate(sorted(nums)):
            if num not in res:
                res[num] = i
        return [res[item] for item in nums]
            
        