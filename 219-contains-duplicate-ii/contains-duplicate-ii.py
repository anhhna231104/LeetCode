class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return
        
        hash_dict = dict()

        for i, num in enumerate(nums):
            if num in hash_dict:
                if abs(i - hash_dict[num]) <= k:
                    return True
            hash_dict[num] = i
        
        return False