"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ## the idea is to create a hashmap and map every node in the list to a new node
        ## initialize the map to None, because there is a mapping from some nodes to null,
        ## if we reach it, then it will result in error if None is not defined
        old_to_copy = {None:None}
        cur = head
        ## in the first pass, add all the nodes to a map and map the corresponding node to its copy
        while cur:
            ## ceate a copy of the cur node val
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        ## in the second pass, as we already have the mapping available we can create the new list
        cur = head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next
        return old_to_copy[head]

        


        