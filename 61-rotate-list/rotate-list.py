# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or k == 0:
            return head

        # Find the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k %= length
        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head