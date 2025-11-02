class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        l, r = 0, len(colors) - 1
        distance = 0

        while l < r:
            if colors[l] != colors[r]:
                distance = r - l
                break
            r -= 1
        
        l, r = 0, len(colors) - 1
        while l < r:
            if colors[r] != colors[l]:
                distance = max(distance, r - l)
                break
            l += 1
        return distance
        