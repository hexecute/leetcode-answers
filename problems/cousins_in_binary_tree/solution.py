# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        next_layer = [(None, root)]
        layer_dict = {}
        while next_layer:
            tmp = []
            for parent, node in next_layer:
                layer_dict[node.val] = parent
                if node.left:
                    tmp.append((node, node.left))
                if node.right:
                    tmp.append((node, node.right))
            keys = layer_dict.keys()
            if x in keys and y in keys:
                if layer_dict[x] is layer_dict[y]:
                    return False
                return True
            elif x in keys or y in keys:
                return False
            next_layer = tmp
            layer_values = {}
        return False
            