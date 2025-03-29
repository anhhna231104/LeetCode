class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0:
        #     return 0
        # if n==1 or n==2:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)
        if n == 0:
            return 0
        a, b = 0, 1
        i = 1
        while i < n:
            tmp = a  
            a = b    
            b = tmp + a  
            i+=1
        return b
        