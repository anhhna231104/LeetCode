class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()

        for i in s:
            if '0' <= i <= '9':
                res.add(int(i))

        if len(res) > 1:
            return sorted(list(res))[-2]
        return -1

        