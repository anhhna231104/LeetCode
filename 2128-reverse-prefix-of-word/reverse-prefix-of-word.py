class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        
        res = ""
        for i in range(len(word)):
            if word[i] == ch:
                for j in range(i, -1, -1):
                    res += word[j]
                res += word[i+1 : len(word)]
                break
        
        return res
        
        