# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        is_odd = True
        odd_head, odd_tail, even_head, even_tail = None, None, None, None
        while not curr is None:
            if is_odd:
                if odd_head:
                    odd_tail.next = curr
                    odd_tail = curr
                else:                    
                    odd_head = curr
                    odd_tail = curr
            else:
                if even_head:
                    even_tail.next = curr
                    even_tail = curr
                else:
                    even_head = curr
                    even_tail = curr
            is_odd = not is_odd
            curr = curr.next
        if even_head:
            odd_tail.next = even_head
            even_tail.next = None
        return odd_head
    