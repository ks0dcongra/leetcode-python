class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = map(self.invertTree, (root.right, root.left))
        return root