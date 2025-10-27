class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        res = []

        for i in nums1:
            if i in nums2 or i in nums3:
                res.append(i)
        for j in nums2:
            if j in nums1 or j in nums3:
                res.append(j)
        for k in nums3:
            if k in nums1 or k in nums2:
                res.append(k)
        return list(set(res))

        
        