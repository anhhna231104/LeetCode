class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        if n <= 2:
            return sum(cost)
        
        cost.sort(reverse = True)
        res = 0
        for i in range(n):
            if (i + 1) % 3 == 0:
                continue
            res += cost[i]

        return res

        
        