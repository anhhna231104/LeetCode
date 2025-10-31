class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        src, dest = set(), set()
        
        for p in paths:
            src.add(p[0])
            dest.add(p[1])
        
        return list(dest - src)[0]

        