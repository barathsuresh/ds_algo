from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        PROBLEM: Reverse a singly linked list.
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# --- Test Runner ---
def create_list(values):
    dummy = ListNode(0)
    ptr = dummy
    for v in values:
        ptr.next = ListNode(v)
        ptr = ptr.next
    return dummy.next

def list_to_array(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

if __name__ == "__main__":
    solver = Solution()
    
    # Test 1
    head = create_list([1, 2, 3, 4, 5])
    print(f"Original: {list_to_array(head)}")
    
    # Re-create because traversal consumes the pointer references in the printer
    head = create_list([1, 2, 3, 4, 5]) 
    new_head = solver.reverseList(head)
    print(f"Reversed: {list_to_array(new_head)}")
    
    print("-" * 30)
    
    # Test 2 (Empty)
    head = create_list([])
    new_head = solver.reverseList(head)
    print(f"Input: [] -> Output: {list_to_array(new_head)}")
    
    # Test 3 (Single Node)
    head = create_list([1])
    new_head = solver.reverseList(head)
    print(f"Input: [1] -> Output: {list_to_array(new_head)}")