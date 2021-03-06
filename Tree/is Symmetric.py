# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # symmetric tree has entire outer left subtree the same and vice versa

        def isMirror(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (node1.val == node2.val) and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

        return isMirror(root, root)