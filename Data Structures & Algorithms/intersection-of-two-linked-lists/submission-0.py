# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0 
        currA = headA
        while currA:
            lenA += 1
            currA = currA.next 
        
        lenB = 0 
        currB = headB 
        while currB:
            lenB += 1
            currB = currB.next

        if lenA > lenB:
            for _ in range(abs(lenA-lenB)):
                headA = headA.next
        else:
            for _ in range(abs(lenA-lenB)):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None


        