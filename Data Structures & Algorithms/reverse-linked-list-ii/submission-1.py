# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        beforeLeft = dummy

        for _ in range(left - 1):
            beforeLeft = beforeLeft.next

        curr = beforeLeft.next
        reverseHead = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = reverseHead
            reverseHead = curr
            curr = temp 

        beforeLeft.next.next = curr
        beforeLeft.next = reverseHead

        return dummy.next