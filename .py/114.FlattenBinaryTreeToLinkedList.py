# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        def flat(node: Optional[TreeNode]):
            if not node:
                return None

            left = node.left
            right = node.right

            if left:
                node.right = left
                node.left = None  
                current = node.right
                while current.right:
                    current = current.right
                current.right = right
            flat(node.right)

        flat(root)