class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        arr = num_people *[0]
        gave = 0
        while candies > 0:
            arr[gave%num_people] += min(gave+1,candies)
            gave+=1
            candies-=gave
        return arr
        

        