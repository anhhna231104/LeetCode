class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        h = dict()
        count = 0

        for n1 in nums1:
            for n2 in nums2:
                total_12 = n1 + n2
                if total_12 not in h:
                    h[total_12] = 1
                else:
                     h[total_12] += 1
        
        for n3 in nums3:
            for n4 in nums4:
                total_34 = - (n3 + n4)
                if total_34 in h:   
                    count += h[total_34]
        
        return count
                    

        
        