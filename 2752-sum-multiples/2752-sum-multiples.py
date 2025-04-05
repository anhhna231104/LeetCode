class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        multiples = set()
        for k in [3, 5, 7]:
            for num in range(k, n+1, k):
                    multiples.add(num)
        return sum(multiples)
        
