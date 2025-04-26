class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count, major, i = 0, None, 0
        # while(i < len(nums)):
        #     if count==0:
        #         major=nums[i]
        #         count+=1
        #     elif major == nums[i]:
        #         count+=1
        #     else:
        #         count-=1
        #     i+=1
        # return major

        count, major = 0, None
        for num in nums:
            if count==0:
                major = num
                count +=1
            elif major == num:
                count+=1
            else: 
                count -=1
        return major


        