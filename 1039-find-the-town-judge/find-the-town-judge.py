class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1 if not trust else -1

        trusted = set()
        be_trusted_counts = [0] * (n + 1)

        for a, b in trust:
            trusted.add(a)
            be_trusted_counts[b] += 1      

        for p in range(1, n + 1):
            trusts_nobody = (p not in trusted)
            trusted_by_all = (be_trusted_counts[p] == n - 1)
            
            if trusts_nobody and trusted_by_all:
                return p

        return -1
