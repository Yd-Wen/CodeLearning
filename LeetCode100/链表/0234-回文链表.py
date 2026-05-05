# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        elem = []
        cur = head
        n = count = 0
        while cur:
            cur = cur.next
            n += 1
        cur = head
        while cur:
            if count < n // 2:
                elem.append(cur.val)
            if ((n % 2 == 0 and count >= n // 2) or (n % 2 == 1 and count > n // 2)) and elem and elem[-1] == cur.val:
                elem.pop()  
            cur = cur.next
            count += 1

        return not elem


"""
赋值
时间复杂度：O(n)
空间复杂度：O(n)
"""
class Solution:
    def isPalindrome(self, head):
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]


"""
快慢指针找中点 + 反转链表
时间复杂度：O(n)
空间复杂度：O(1)
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        def reverse(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur 
                cur = nxt
            return pre      

        def middle(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        half = middle(head)
        right = reverse(half.next)
    
        while head and right:
            if head.val != right.val:
                return False
            head = head.next
            right = right.next
        return True      
