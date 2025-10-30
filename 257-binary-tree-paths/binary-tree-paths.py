# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []

        res, q = [], collections.deque([(root, "")])
        while q:
            node, l = q.popleft()
            if not node.left and not node.right:
                res.append(l + str(node.val))
            if node.left:
                q.append((node.left, l + str(node.val) + "->"))
            if node.right:
                q.append((node.right, l + str(node.val) + "->"))
        
        return res