class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        (x1,y1), (x2,y2), (x3,y3) = points
        vector_A_X = x2-x1
        vector_B_X = x3-x2

        vector_A_Y = y2-y1        
        vector_B_Y = y3-y2

        if vector_A_X*vector_B_Y - vector_B_X*vector_A_Y == 0:
            return False
        return True
        