class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 10:
            return False
        stones = n
        alice_turn = True
        to_remove = 10       
        while True:
            if stones < to_remove:
                return not alice_turn
            stones -= to_remove
            alice_turn = not alice_turn
            to_remove -= 1
            if to_remove < 1:
                to_remove = 1