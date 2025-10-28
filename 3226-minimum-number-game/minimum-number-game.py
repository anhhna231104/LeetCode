class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr, taken = [], []

        while nums:
            min_val = min(nums)
            taken.append(min_val)
            nums.remove(min_val)

        for i in range(0, len(taken), 2):
            arr.append(taken[i+1])
            arr.append(taken[i])

        return arr
        
