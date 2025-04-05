class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = 0
        # k = 1
        # while n > 0:
        #     n-=k 
        #     if n >= 0:
        #         res += 1
        #     k+=1 
        # return res  
        res = 0
        left, right = 1, n
        while left <= right:
            mid = (left+right)//2
            if(mid*(mid+1))//2 <= n:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res            
                          
        