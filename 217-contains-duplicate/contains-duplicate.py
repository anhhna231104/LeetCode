class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return

        map = set()

        for i in nums:
            if i in map:
                return True
            map.add(i)
        
        return False
        