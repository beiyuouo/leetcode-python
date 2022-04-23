"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from copy import copy

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        addr2id = {}

        q = head
        count = 0

        while q:
            addr2id[q] = count
            count += 1
            q = q.next
        
        q = head
        count = 0
        id2addr = {}

        while q:
            temp_ = copy(q)
            id2addr[count] = temp_
            count += 1
            q = q.next
        
        id2addr[count] = None
        
        q = head
        count = 0
        while q:
            id2addr[count].next = id2addr[count + 1]
            if q.random:
                id2addr[count].random = id2addr[addr2id[q.random]]
            count += 1
            q = q.next
        
        return id2addr[0]


