class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        h = set()

        for e in edges:
            for i in range(len(e)):
                if e[i] not in h:
                    h.add(e[i])
                else:
                    return e[i]
        