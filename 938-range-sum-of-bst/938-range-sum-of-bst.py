# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sumRange = 0
        self.DFS(root, low, high)
        return self.sumRange
    
    def DFS(self, current, low, high):
        if(not current):
            return
        if (current.val>=low) and (current.val<=high):
            self.sumRange+=current.val
        if current.val < high:
            self.DFS(current.right, low, high)
        if current.val > low:
            self.DFS(current.left, low, high)
        