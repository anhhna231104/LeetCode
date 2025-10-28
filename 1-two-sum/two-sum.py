class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return

        map = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in map:
                return [map[comp], i]
            map[num] = i

        return map
        
        