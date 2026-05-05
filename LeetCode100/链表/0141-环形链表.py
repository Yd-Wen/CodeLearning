# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
快慢指针
时间复杂度：O(n)
空间复杂度：O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while True:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


"""
哈希
时间复杂度：O(n)
空间复杂度：O(n)
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashmap = set()
        cur = head
        while cur:
            if cur in hashmap:
                return True
            hashmap.add(cur)
            cur = cur.next
        return False   
