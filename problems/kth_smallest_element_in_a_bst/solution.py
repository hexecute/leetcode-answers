# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.nth_smallest = 0
        self.k = k
        self.traverse(root)
        return self.rv
    
    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
        self.nth_smallest += 1
        if (self.nth_smallest == self.k):
            self.rv = node.val
        if node.right:
            self.traverse(node.right)
        
        
        