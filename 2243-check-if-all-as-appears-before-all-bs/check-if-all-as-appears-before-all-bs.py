class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s[i] == 'a' and i > 0:
                if s[i - 1] == 'b':
                    return False
        
        return True
        