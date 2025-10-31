class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even, odd = [], []

        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        even.sort()
        odd.sort()
        res = []

        a, b = 0, -1
        
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[a])
                a += 1
            else:
                res.append(odd[b])
                b -= 1
        
        return res
            
