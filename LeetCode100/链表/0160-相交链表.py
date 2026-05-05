# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
哈希集合
时间复杂度：O(m+n)
空间复杂度：O(m)
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hashmap  = set()
        cur = headA
        while cur:
            hashmap.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in hashmap:
                return cur
            cur = cur.next
        return None
    
    
"""
双指针
时间复杂度：O(m+n)
空间复杂度：O(1)
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        n = m = 1
        cur = headA
        while cur.next:
            cur = cur.next
            n += 1
        cur = headB
        while cur.next:
            cur = cur.next
            m += 1
        
        a = headA
        b = headB
        diff = abs(n - m)
        while diff > 0:
            if n > m:
                a = a.next 
            else:
                b = b.next
            diff -= 1
        if a == b:
            return a
        while a.next and a.next != b.next:
            a = a.next
            b = b.next
        if not a.next:
            return None
        elif a.next == b.next:
            return a.next


# 简化写法
class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        # 核心逻辑：两个指针不断遍历，走到头就切换到另一条链表
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        # 相遇时就是交点（无交点则都为 None，也会退出循环）
        return pA
    