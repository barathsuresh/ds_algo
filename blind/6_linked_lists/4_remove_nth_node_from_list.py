from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the nth node from the end of the list 
        and return its head.

        Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

        Example 2:
        Input: head = [1], n = 1
        Output: []

        Example 3:
        Input: head = [1,2], n = 1
        Output: [1]

        Constraints:
        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz
        """
        # Dummy node handles edge cases (like removing the head itself)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Step 1: Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # Step 2: Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Step 3: Delete the node
        # left is now just before the node to be deleted
        left.next = left.next.next
        
        return dummy.next

# Helper to print
def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(vals)

if __name__ == "__main__":
    solver = Solution()
    
    # List: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    
    print(f"Original (n={n}):")
    print_list(head)
    
    new_head = solver.removeNthFromEnd(head, n)
    
    print("Modified:")
    print_list(new_head)
    # Expected: [1, 2, 3, 5]