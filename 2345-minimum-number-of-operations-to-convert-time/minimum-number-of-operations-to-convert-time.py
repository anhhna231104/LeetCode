class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        def convert_min(t):
            hh, mm = t.split(':')
            return int(hh)*60 + int(mm)
        
        current, correct = convert_min(current), convert_min(correct)
        ops = 0
        comp = correct - current

        for m in [60, 15, 5, 1]:
            if comp == 0:
                break
            ops += comp // m
            comp %= m

        return ops
        

        