# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node:Optional[TreeNode]) -> int:
            if not node: return 0
            left, right = map(balanced,(node.left, node.right))
            if abs(left-right) > 1:
                raise ValueError("too long")
            return max(left,right)+1
        try:
            balanced(root)
        except ValueError:
            return False
        return True