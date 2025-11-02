class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new = ''
            for i in range(0, len(s), k):
                new += str(sum(int(i) for i in s[i : i+k]))
            s = new
        
        return s

        