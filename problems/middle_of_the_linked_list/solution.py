# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 1
        pointer = head
        while pointer.next != None:
            pointer = pointer.next
            length += 1
        
        pointer = head
        for i in range(length/2):
            pointer = pointer.next
        return pointer
        