# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        # Slight inefficency with double-checking. Better solution is to have a separate recursive call
        if root.val != arr[0]:
            return False
        
        
        if not root.left and not root.right and not arr[1:]:
            return True
        elif (not root.left and not root.right) or not arr[1:]:
            return False
        
        if root.left and root.left.val == arr[1]:
            left = self.isValidSequence(root.left, arr[1:])
        else:
            left = False
        if root.right and root.right.val == arr[1]:
            right = self.isValidSequence(root.right, arr[1:])
        else:
            right = False
        return left or right
        
        """
        target = root
        length = len(arr)
        i = 0
        if target.val != arr[i]:
            return False
        while True:
            i += 1
            if i == length:
                if not target.left and not target.right:
                    return True
                return False
            print("%s: %s %s" %(target.val, target.left and target.left.val, target.right and target.right.val))
            if target.left and target.left.val == arr[i]:
                target = target.left
            elif target.right and target.right.val == arr[i]:
                target = target.right
            else:
                return False
        """