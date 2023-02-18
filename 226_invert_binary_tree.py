from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.right, root.left = root.left, root.right
        
        #swap children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
def main():
    sol = Solution()
    root = [4,2,7,1,3,6,9]
    print(sol.invertTree(root))