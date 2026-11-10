# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        if not root: return 0

        def getHeight(root: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not root: return 0

            hL = getHeight(root.left)
            hR = getHeight(root.right)
            height = max(hL, hR) + 1
            
            diameter = hL + hR
            max_diameter = max(diameter, max_diameter)
            
            return height

        getHeight(root)
        return max_diameter



        


