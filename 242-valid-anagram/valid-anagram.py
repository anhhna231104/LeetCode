class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        h = dict()

        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        for i in t:
            if i not in h or h[i] == 0:
                return False
            h[i] -= 1  
            
        return True

        

        