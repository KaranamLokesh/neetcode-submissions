# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        answer = dummy
        while( l1 or l2):
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            sum = carry + l1val + l2val
            
            remainder = sum%10
            carry = sum//10
            new = ListNode(remainder)
            dummy.next = new
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next


        if carry :
            new = ListNode(carry)
            dummy.next = new
            dummy = dummy.next


        return answer.next

               # while l1:
        #     if carry:
        #         sum = carry + l1.val
            
        #         remainder = sum%10
        #         carry = sum//10
        #         new = ListNode(remainder)
        #         dummy.next = new
        #         dummy = dummy.next
                
        #         l1 = l1.next
        # while l2:
        #     if carry:
        #         sum = carry + l2.val
            
        #         remainder = sum%10
        #         carry = sum//10
        #         new = ListNode(remainder)
        #         dummy.next = new
        #         dummy = dummy.next
                
        #         l2 = l2.next     


        