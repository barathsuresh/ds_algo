from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.

        Example 1:
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Example 2:
        Input: head = [1,2]
        Output: [2,1]

        Example 3:
        Input: head = []
        Output: []

        Constraints:
        The number of nodes in the list is the range [0, 5000].
        -5000 <= Node.val <= 5000
        """
        prev = None
        curr = head
        
        while curr:
            # Save the next node so we don't lose the rest of the list
            temp = curr.next
            
            # Reverse the pointer
            curr.next = prev
            
            # Move pointers forward
            prev = curr
            curr = temp
            
        return prev

# Helper function to print the list
def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

if __name__ == "__main__":
    solver = Solution()
    
    # Create List: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    print("Original:")
    print_list(head)
    
    new_head = solver.reverseList(head)
    
    print("Reversed:")
    print_list(new_head)
    # Expected: [5, 4, 3, 2, 1]