# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_travers(node):
            nonlocal node_count
            nonlocal kth_smallest
            
            if node is None:
                return
            
            inorder_travers(node.left)
            
            node_count += 1
            if node_count == k:
                kth_smallest = node.val
                
            inorder_travers(node.right)
            
        node_count = 0
        kth_smallest = None
        inorder_travers(root)
        return kth_smallest