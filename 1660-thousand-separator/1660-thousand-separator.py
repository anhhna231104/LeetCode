class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1000:
            return str(n)
        count, rev = 0, []
        while n > 0:
            rev.append(str(n%10))
            n = n//10
            count += 1
            if count == 3 and n > 0:
                rev.append(".")
                count = 0
        return "".join(list(reversed(rev)))
            

        

        
        