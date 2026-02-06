from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        A linked list of length n is given such that each node contains an additional random pointer, 
        which could point to any node in the list, or null.

        Construct a deep copy of the list.

        Example 1:
        Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
        """
        # Dictionary to map old nodes to their new copies
        # { old_node : new_node }
        oldToCopy = { None : None }

        # Pass 1: Create copies of all nodes
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # Pass 2: Connect pointers
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]       # Map old next -> new next
            copy.random = oldToCopy[cur.random]   # Map old random -> new random
            cur = cur.next

        return oldToCopy[head]

if __name__ == "__main__":
    solver = Solution()
    
    # Constructing the complex list: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # 1. Create Nodes
    n0 = Node(7)
    n1 = Node(13)
    n2 = Node(11)
    n3 = Node(10)
    n4 = Node(1)
    
    # 2. Connect Next
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    
    # 3. Connect Random (Indices based on example)
    n0.random = None
    n1.random = n0  # Index 0
    n2.random = n4  # Index 4
    n3.random = n2  # Index 2
    n4.random = n0  # Index 0
    
    new_head = solver.copyRandomList(n0)
    
    print(f"Original Head Value: {n0.val}")
    print(f"Copied Head Value: {new_head.val}")
    print(f"Original Random of 2nd Node: {n1.random.val}")
    print(f"Copied Random of 2nd Node: {new_head.next.random.val}")