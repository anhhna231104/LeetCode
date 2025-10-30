class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        total = (n * (n + 1)) // 2

        while l <= r:
            pivot = (l + r) // 2
            total_left = (pivot * (pivot + 1)) // 2
            total_right = total - total_left + pivot
    
            if total_left < total_right:
                l = pivot + 1
            elif total_left > total_right:
                r = pivot - 1
            else:
                return pivot 

        return -1
        