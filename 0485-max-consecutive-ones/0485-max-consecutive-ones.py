class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = []
        for num in nums:
            if num==1:
                count+=1
            else:
                res.append(count)
                count = 0
        res.append(count)
        return max(res)


        