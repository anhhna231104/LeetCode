class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves, i = 0, 0

        while i < len(s):
            if s[i] == 'O':
                i += 1
            else:
                moves += 1
                i += 3
        
        return moves


        