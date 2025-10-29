# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        
        values = []
        
        def inorder(node):
            if not node: 
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        l, r = 0, len(values) - 1

        while l < r:
            comp = values[l] + values[r]
            if comp == k:
                return True
            elif comp > k:
                r -= 1
            else:
                l += 1
        
        return False
        


        