# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## there are two ways to solve this
        ## 1. iterate through the array, find the length N, then N - n becomes the nth node to be deleted, delete it
        ## 2. take two lists, initiate them to head, iterate one list to n, then start iterating the second list from n, 
        ## so when the first list reaches the end, we are at nth index from the end
        length = 0
        l1 = head
        while(l1):
            length+=1
            l1 = l1.next
        count = 1
        dummy = head
        if length - n ==0:
            return head.next
        while count!=length-n:
            count+=1
            head = head.next
        if head:
            head.next = head.next.next
        return dummy






        