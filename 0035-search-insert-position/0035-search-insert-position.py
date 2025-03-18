class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i == 0 and target < nums[i]:
                return i
            if nums[i] == target:
                return i
            if i == len(nums)-1 and target > nums[i]:
                return i + 1
            if nums[i-1] < target and nums[i] > target:
                return i
            i+=1


        