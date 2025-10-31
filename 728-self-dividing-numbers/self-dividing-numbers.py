class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []

        for n in range(left, right + 1):
            is_self_div = True
            i = n
            while i > 0:
                tmp = i % 10
                if tmp == 0 or n % tmp != 0:
                    is_self_div = False
                    break
                i //= 10

            if is_self_div:
                res.append(n)

        return res
            
        