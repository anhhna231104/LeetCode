# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        self.min_depth = float('inf')

        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.min_depth = min(depth, self.min_depth)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)

        return self.min_depth
        