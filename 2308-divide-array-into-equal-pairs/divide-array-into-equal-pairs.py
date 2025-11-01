class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = Counter(nums)

        for c in counts.values():
            if c % 2 != 0:
                return False

        return True
        