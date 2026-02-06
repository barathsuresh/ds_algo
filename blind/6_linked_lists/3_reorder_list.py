from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        You are given the head of a singly linked-list. The list can be represented as:
        L0 -> L1 -> ... -> Ln - 1 -> Ln

        Reorder the list to be on the following form:
        L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...

        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        # Step 1: Find middle using Slow/Fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Split the list into two halves
        second = slow.next
        slow.next = None # Cut off the first half
        prev = None
        
        # Step 2: Reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2

# Helper to print
def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(vals)

if __name__ == "__main__":
    solver = Solution()
    
    # 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print("Original:")
    print_list(head)
    
    solver.reorderList(head)
    
    print("Reordered:")
    print_list(head)
    # Expected: [1, 4, 2, 3]