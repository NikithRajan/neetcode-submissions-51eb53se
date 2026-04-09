# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        dummy = ListNode(0,head)
        count = 0
        if head is None or head.next is None:
            return None
        while temp:
            count += 1
            temp = temp.next
        print(count)
        k = count - n
        i = 0
        temp = dummy
        while i<k:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        return dummy.next
