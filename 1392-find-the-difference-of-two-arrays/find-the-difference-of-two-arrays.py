class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1, n2 = set(nums1), set(nums2)

        l1 = n1 - n2
        l2 = n2 - n1

        return [list(l1), list(l2)]