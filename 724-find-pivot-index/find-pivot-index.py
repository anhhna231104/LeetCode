class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        total_left = 0

        for i in range(len(nums)):
            total_right = total - total_left - nums[i]

            if total_left == total_right:
                return i
            else:
                total_left += nums[i]

        return -1
        