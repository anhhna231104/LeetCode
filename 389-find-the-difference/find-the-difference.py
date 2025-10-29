class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h = dict()

        for i in s:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        
        for i in t:
            if i not in s or h[i] == 0:
                return i
            h[i] -= 1
