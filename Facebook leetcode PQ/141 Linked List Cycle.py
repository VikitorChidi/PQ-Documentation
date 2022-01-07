class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

# Algorithm
# We go through each node one by one and record each node's reference (or memory address) in a hash table.
#  If the current node is null, we have reached the end of the list and it must not be cyclic.
#  If current node’s reference is in the hash table, then return true.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_seen = set()

        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False