class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = sorted(str(num))
        return int(num[0] + num[2]) + int(num[1] + num[3])
        