class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        i, sum = 2, 1
        while i <= math.sqrt(num):
            if num%i==0:
                sum+=i
                if i!= num//i:
                    sum+=num//i
            i+=1    
        return sum==num   
