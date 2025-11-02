class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        mx = 0

        for s in sentences:
            w = s.split()
            current = len(w)
            mx = max(mx, current)
                
        return mx
        