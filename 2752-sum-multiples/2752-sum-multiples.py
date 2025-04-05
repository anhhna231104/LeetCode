class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        seen = set() 
        for k in [3, 5, 7]:
            for num in range(k, n+1, k):
                if num not in seen:  
                    sum += num
                    seen.add(num)
        return sum
        
