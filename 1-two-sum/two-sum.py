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
            complementary = target - num

            if complementary in map:
                return [map[complementary], i]
            
            map[num] = i
            
        return map
        
        