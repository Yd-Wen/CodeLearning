# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
哈希
时间复杂度：O(n)
空间复杂度：O(n)
"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hashmap = set()
        cur = head
        while cur:
            if cur in hashmap:
                return cur
            hashmap.add(cur)
            cur = cur.next
        return None
    

"""
快慢指针
时间复杂度：O(n)
空间复杂度：O(1)
"""
class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # 先跑再判断
        # 此处如果用 while (fast != slow)，则在一开始时就违背了条件
        # 也可用 do while, 但以下代码更符合 repeat until (重复直到) 的思考习惯
        while True:
            # 指向空节点，说明无环。
            if not fast or not fast.next:
                return None

            # fast 和 slow 异速前进
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break  # fast 和 slow 相遇
  
        # ptr 和 slow 同速前进，直至相遇在入口
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next

        return ptr # 返回入口节点
    