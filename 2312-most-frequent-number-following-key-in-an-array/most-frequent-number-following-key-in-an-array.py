class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        h = dict()
        i = 0

        while i <= len(nums) - 2:
            if nums[i] == key:
                if nums[i + 1] not in h:
                    h[nums[i + 1]] = 1
                else:
                    h[nums[i + 1]] += 1

            i += 1
        
        return max(h, key = h.get)
        