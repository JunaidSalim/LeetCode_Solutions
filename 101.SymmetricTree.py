# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def search(left,right):
            if not left or not right:
                return left==right
            if left.val!=right.val:
                return False
            return search(left.left,right.right) and search(left.right,right.left)
        return search(root.left,root.right)