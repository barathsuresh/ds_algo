from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists in a one sorted list. The list should be made by splicing together 
        the nodes of the first two lists.

        Return the head of the merged linked list.

        Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

        Example 2:
        Input: list1 = [], list2 = []
        Output: []

        Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]
        """
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach the remaining part of the list that isn't empty
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
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
    
    # List 1: 1 -> 2 -> 4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    
    # List 2: 1 -> 3 -> 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    merged = solver.mergeTwoLists(l1, l2)
    print("Merged List:")
    print_list(merged)
    # Expected: [1, 1, 2, 3, 4, 4]