class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]

        for i in range(len(gain)):
            h = altitudes[i] + gain[i]
            altitudes.append(h)
        
        return max(altitudes)