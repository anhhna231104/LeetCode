class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = dict()

        for n in nums:
            if n not in h:
                h[n] = 1
            else:
                h[n] += 1
        
        total = 0
        for k, v in h.items():
            if v == 1:
                total += k
        
        return total
        