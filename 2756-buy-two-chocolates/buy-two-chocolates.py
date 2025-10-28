class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """      
        min1, min2 = float('inf'), float('inf')
        
        for price in prices:
            if min1 >= price:
                min2 = min1
                min1 = price
            elif min2 > price:
                min2 = price

        min_sub_total = min1 + min2

        if min_sub_total <= money:
            return money - min_sub_total
        return money
        

            
        