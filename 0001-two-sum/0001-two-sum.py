class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in map:
                return [map[comp], idx]
            map[num] = idx
        return []
        
        