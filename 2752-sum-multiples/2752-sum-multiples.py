class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return sum(num for num in range(1, n+1) if num%3==0 or num%5==0 or num%7==0)

        selected = set()
        for k in [3, 5, 7]:
            for num in range(k, n+1, k):
                selected.add(num)
        return sum(selected)
        
