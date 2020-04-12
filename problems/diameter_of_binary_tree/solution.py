# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from math import log, pow

class Solution(object):
    def __init__(self):
        self.max = 0
    
    def inorderTraversal(self, node, depth=0):
        if node.left == None:
            left = 0
        else:
            left = max(self.inorderTraversal(node.left)) + 1
            
        if node.right == None:
            right = 0
        else:
            right = max(self.inorderTraversal(node.right)) + 1
            
        # print("%s %s %s" % (node.val, left, right))
        potential_max = left + right
        if (potential_max > self.max):
            self.max = potential_max
        return (left, right)
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.inorderTraversal(root)
        return self.max

