class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = nums.sort()
        left,right = 0,len(nums)
        while(left<right):
            mid = (left+right)//2
            if(mid<nums[mid]):
                right = mid
            else:
                left = mid+1
        return left
        
        