# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return
        
        seen_dict = {}

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            if node.val in seen_dict:
                seen_dict[node.val] += 1
            else:
                seen_dict[node.val] = 1

            inorder(node.right)
        
        inorder(root)

        if not seen_dict:
            return

        max_freq = 0
        res = []

        for val in seen_dict.values():
            max_freq = max(max_freq, val)
        
        for key, val in seen_dict.items():
            if val == max_freq:
                res.append(key)

        return res
        
    
        


        