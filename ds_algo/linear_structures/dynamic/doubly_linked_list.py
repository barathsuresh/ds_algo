"""
Doubly Linked List Implementation

A comprehensive implementation of a doubly linked list with bidirectional traversal,
optimized operations at both ends, and detailed complexity analysis.
"""

from typing import Any, Optional, Iterable, Iterator


class DLLNode:
    """
    Node class for Doubly Linked List
    Uses __slots__ for memory optimization
    """

    __slots__ = ("data", "prev", "next")

    def __init__(
        self,
        data: Any,
        prev_node: Optional["DLLNode"] = None,
        next_node: Optional["DLLNode"] = None,
    ):
        self.data = data
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList:
    """
    Doubly Linked List implementation with comprehensive operations

    Features:
    - O(1) insert/delete at both ends
    - Bidirectional traversal
    - Optimized access from nearest end
    - Comprehensive error handling
    """

    def __init__(self, iterable: Optional[Iterable] = None):
        """
        Initialize empty list or from iterable
        Time Complexity: O(1) for empty, O(n) for iterable
        Space Complexity: O(1) for empty, O(n) for iterable
        """
        self.head: Optional[DLLNode] = None
        self.tail: Optional[DLLNode] = None
        self._size: int = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self) -> int:
        """
        Return the number of elements
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size

    def __bool__(self) -> bool:
        """
        Return True if list is not empty
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size > 0

    def is_empty(self) -> bool:
        """
        Check if the list is empty
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size == 0

    def __iter__(self) -> Iterator[Any]:
        """
        Forward iterator protocol support
        Time Complexity: O(n) for full iteration
        Space Complexity: O(1)
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __reversed__(self) -> Iterator[Any]:
        """
        Reverse iterator protocol support
        Time Complexity: O(n) for full iteration
        Space Complexity: O(1)
        """
        current = self.tail
        while current:
            yield current.data
            current = current.prev

    def __repr__(self) -> str:
        """
        String representation for debugging
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        elements = list(self)
        return f"DoublyLinkedList({elements})"

    def __str__(self) -> str:
        """
        Human-readable string representation
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.is_empty():
            return "Empty"
        return "None <- " + " <-> ".join(str(item) for item in self) + " -> None"

    def _check_index(self, index: int, allow_end: bool = False) -> None:
        """
        Validate index bounds
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        max_index = self._size if allow_end else self._size - 1
        if index < 0 or index > max_index:
            raise IndexError(f"Index {index} out of range [0, {max_index}]")

    def _node_at(self, index: int) -> DLLNode:
        """
        Get node at specific index (optimized to traverse from nearest end)
        Time Complexity: O(n/2) average, O(n) worst
        Space Complexity: O(1)
        """
        self._check_index(index)

        # Choose the closer end to start traversal
        if index <= self._size // 2:
            # Traverse from head
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev

        return current

    # Insertion Operations
    def prepend(self, value: Any) -> None:
        """
        Insert element at the beginning
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DLLNode(value, None, self.head)

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node
        self._size += 1

    def append(self, value: Any) -> None:
        """
        Insert element at the end
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DLLNode(value, self.tail, None)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self._size += 1

    def insert_at(self, index: int, value: Any) -> None:
        """
        Insert element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index, allow_end=True)

        if index == 0:
            self.prepend(value)
            return

        if index == self._size:
            self.append(value)
            return

        # Insert in middle
        current = self._node_at(index)
        new_node = DLLNode(value, current.prev, current)
        current.prev.next = new_node
        current.prev = new_node
        self._size += 1

    # Deletion Operations
    def delete_at(self, index: int) -> Any:
        """
        Delete element at specific index and return its value
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        node_to_delete = self._node_at(index)
        value = node_to_delete.data

        # Update prev node's next pointer
        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.head = node_to_delete.next

        # Update next node's prev pointer
        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev
        else:
            self.tail = node_to_delete.prev

        self._size -= 1
        return value

    def delete_value(self, value: Any) -> bool:
        """
        Delete first occurrence of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        Returns: True if deleted, False if not found
        """
        current = self.head

        while current:
            if current.data == value:
                # Update prev node's next pointer
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                # Update next node's prev pointer
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self._size -= 1
                return True

            current = current.next

        return False

    def pop_front(self) -> Any:
        """
        Remove and return first element
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty list")

        value = self.head.data
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self._size -= 1
        return value

    def pop_back(self) -> Any:
        """
        Remove and return last element
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty list")

        value = self.tail.data
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self._size -= 1
        return value

    # Access Operations
    def get(self, index: int) -> Any:
        """
        Get element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return self._node_at(index).data

    def set(self, index: int, value: Any) -> None:
        """
        Set element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._node_at(index).data = value

    def __getitem__(self, index: int) -> Any:
        """Support for list[index] syntax"""
        return self.get(index)

    def __setitem__(self, index: int, value: Any) -> None:
        """Support for list[index] = value syntax"""
        self.set(index, value)

    # Search Operations
    def find(self, value: Any) -> int:
        """
        Find index of first occurrence of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        Returns: index if found, -1 if not found
        """
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def find_reverse(self, value: Any) -> int:
        """
        Find index of last occurrence of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        Returns: index if found, -1 if not found
        """
        current = self.tail
        index = self._size - 1

        while current:
            if current.data == value:
                return index
            current = current.prev
            index -= 1

        return -1

    def contains(self, value: Any) -> bool:
        """
        Check if value exists in the list
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return self.find(value) != -1

    def __contains__(self, value: Any) -> bool:
        """Support for 'value in list' syntax"""
        return self.contains(value)

    def count(self, value: Any) -> int:
        """
        Count occurrences of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        current = self.head

        while current:
            if current.data == value:
                count += 1
            current = current.next

        return count

    # Utility Operations
    def clear(self) -> None:
        """
        Remove all elements
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = self.tail = None
        self._size = 0

    def reverse(self) -> None:
        """
        Reverse the list in-place
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        self.tail = current if current else None

        while current:
            # Swap next and prev pointers
            current.prev, current.next = current.next, current.prev
            # Move to the original next node (now in prev)
            current = current.prev

        # Swap head and tail
        self.head, self.tail = self.tail, self.head

    def to_list(self) -> list:
        """
        Convert to Python list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return list(self)

    def to_list_reverse(self) -> list:
        """
        Convert to Python list in reverse order
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return list(reversed(self))

    def copy(self) -> "DoublyLinkedList":
        """
        Create a shallow copy
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return DoublyLinkedList(self)

    # Specialized Operations
    def rotate_left(self, k: int) -> None:
        """
        Rotate list k positions to the left
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty() or k <= 0:
            return

        k = k % self._size  # Handle k > size
        if k == 0:
            return

        # Find the new tail (at position k-1)
        new_tail = self._node_at(k - 1)
        new_head = new_tail.next

        # Break the connection
        new_tail.next = None
        new_head.prev = None

        # Connect old tail to old head
        self.tail.next = self.head
        self.head.prev = self.tail

        # Update head and tail
        self.head = new_head
        self.tail = new_tail

    def rotate_right(self, k: int) -> None:
        """
        Rotate list k positions to the right
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty() or k <= 0:
            return

        k = k % self._size  # Handle k > size
        if k == 0:
            return

        self.rotate_left(self._size - k)


def demonstrate_doubly_linked_list():
    """Demonstrate doubly linked list operations"""
    print("=== DOUBLY LINKED LIST DEMONSTRATION ===\n")

    # Creation and basic operations
    print("1. CREATION AND BASIC OPERATIONS:")
    dll = DoublyLinkedList([1, 2, 3, 4, 5])
    print(f"   Created from [1,2,3,4,5]: {dll}")
    print(f"   Length: {len(dll)}")
    print(f"   Is empty: {dll.is_empty()}\n")

    # Bidirectional traversal
    print("2. BIDIRECTIONAL TRAVERSAL:")
    print(f"   Forward: {list(dll)}")
    print(f"   Backward: {list(reversed(dll))}\n")

    # Insertion operations
    print("3. INSERTION OPERATIONS:")
    dll.prepend(0)
    print(f"   After prepend(0): {dll}")

    dll.append(6)
    print(f"   After append(6): {dll}")

    dll.insert_at(3, 99)
    print(f"   After insert_at(3, 99): {dll}")
    print(f"   Length: {len(dll)}\n")

    # Access operations (optimized from nearest end)
    print("4. ACCESS OPERATIONS:")
    print(f"   Element at index 3: {dll.get(3)}")
    print(f"   Element at index 0: {dll[0]}")
    print(f"   Element at index -1 (from end): {dll[len(dll)-1]}")

    dll.set(3, 100)
    print(f"   After set(3, 100): {dll}\n")

    # Search operations
    print("5. SEARCH OPERATIONS:")
    print(f"   Find 100 (forward): index {dll.find(100)}")
    print(f"   Find 100 (reverse): index {dll.find_reverse(100)}")
    print(f"   Contains 100: {100 in dll}")
    print(f"   Count of 1: {dll.count(1)}\n")

    # Deletion operations
    print("6. DELETION OPERATIONS:")
    deleted = dll.delete_at(3)
    print(f"   Deleted at index 3: {deleted}")
    print(f"   After deletion: {dll}")

    success = dll.delete_value(6)
    print(f"   Delete value 6: {success}")
    print(f"   After deletion: {dll}")

    popped_front = dll.pop_front()
    print(f"   Popped front: {popped_front}")
    print(f"   After pop_front: {dll}")

    popped_back = dll.pop_back()
    print(f"   Popped back: {popped_back}")
    print(f"   After pop_back: {dll}\n")

    # Utility operations
    print("7. UTILITY OPERATIONS:")
    print(f"   Original: {dll}")

    dll_copy = dll.copy()
    print(f"   Copy: {dll_copy}")

    dll.reverse()
    print(f"   After reverse: {dll}")

    dll.rotate_left(2)
    print(f"   After rotate_left(2): {dll}")

    dll.rotate_right(1)
    print(f"   After rotate_right(1): {dll}")


def complexity_comparison():
    """Compare complexities between singly and doubly linked lists"""
    print("\n=== DOUBLY vs SINGLY LINKED LIST COMPLEXITY ===\n")

    operations = [
        ("Operation", "Singly LL", "Doubly LL", "DLL Advantage"),
        ("-" * 15, "-" * 10, "-" * 11, "-" * 25),
        ("Prepend", "O(1)", "O(1)", "Same"),
        ("Append", "O(n)", "O(1)", "✅ Much faster"),
        ("Pop front", "O(1)", "O(1)", "Same"),
        ("Pop back", "O(n)", "O(1)", "✅ Much faster"),
        ("Insert at index", "O(n)", "O(n)", "✅ ~2x faster (bidirectional)"),
        ("Access by index", "O(n)", "O(n)", "✅ ~2x faster (nearest end)"),
        ("Delete by index", "O(n)", "O(n)", "✅ ~2x faster (bidirectional)"),
        ("Reverse traversal", "Not supported", "O(n)", "✅ Native support"),
        ("Memory per node", "2 pointers", "3 pointers", "❌ 50% more memory"),
    ]

    for row in operations:
        print(f"{row[0]:<15} {row[1]:<10} {row[2]:<11} {row[3]}")


if __name__ == "__main__":
    demonstrate_doubly_linked_list()
    complexity_comparison()
