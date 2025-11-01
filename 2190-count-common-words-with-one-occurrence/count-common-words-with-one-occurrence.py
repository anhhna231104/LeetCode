class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        h1, h2 = dict(), dict()

        for w in words1:
            if w not in h1:
                h1[w] = 1
            else:
                h1[w] += 1
        
        for w in words2:
            if w not in h2:
                h2[w] = 1
            else:
                h2[w] += 1
        
        count = 0
        for w in h1:
            if h1[w] == 1:
                if w in h2 and h2[w] == 1:
                    count += 1
        
        return count
        