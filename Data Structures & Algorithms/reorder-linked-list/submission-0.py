# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## go to the middle of the list to split the list into 2 parts
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ## reverse the second part of the list, this will help in maintaining structure of answer
        second = slow.next
        prev = slow.next=None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        ## join the first part and the reversed part, to get the answer
        first,second = head,prev
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2


        