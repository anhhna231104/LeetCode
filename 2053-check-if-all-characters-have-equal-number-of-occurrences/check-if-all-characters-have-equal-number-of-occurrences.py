class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = dict()

        for i in s:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        
        count = h[s[0]]
        for k, v in h.items():
            if v != count:
                return False
        
        return True

        