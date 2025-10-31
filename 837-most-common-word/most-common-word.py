class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        filtered = re.sub(r'[^\w\s]', ' ', paragraph)
        words = filtered.lower().split()
        seen = dict()

        for w in words:
            if w not in ban:
                if w not in seen:
                    seen[w] = 1
                else:
                    seen[w] += 1
            else:
                continue
        
        return max(seen, key=seen.get)

        