# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
迭代
时间复杂度：O(n)
空间复杂度：O(1)
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


"""
递归
时间复杂度：O(n)
空间复杂度：O(n)
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head):
            if not head or not head.next:
                return head
            new_head = reverse(head.next)
            head.next.next = head
            head.next = None
            return new_head
        return reverse(head)
    