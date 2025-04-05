# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root):
        sum = 0
        if root is None:
            return 0
        if root.left:
            tmp = root.left
            if tmp.left is None and tmp.right is None:
                sum += tmp.val
            else:
                sum += self.inorder(tmp)
        if root.right:
            tmp = root.right
            sum+= self.inorder(tmp)
        return sum

    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.inorder(root)

            

        