class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)

        r_seen, c_seen = [[] for _ in range(n)], [[] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                v = matrix[r][c]
                if v in r_seen[r] or v in c_seen[c]:
                    return False
                r_seen[r].append(v)
                c_seen[c].append(v)

        return True
        