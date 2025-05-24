class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        kind = set()
        for candy in candyType:
            kind.add(candy)
            if len(kind) == n//2:
                break
        return len(kind)

        