class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        res = 0

        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    res += 1
            elif ruleKey == "color":
                if item[1] == ruleValue:
                    res += 1
            else:
                if item[2] == ruleValue:
                    res += 1
        
        return res
                
        