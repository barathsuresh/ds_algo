"""
Singly Linked List Implementation

A comprehensive implementation of a singly linked list with all standard operations,
optimizations, and detailed complexity analysis.
"""

from typing import Any, Optional, Iterable, Iterator


class SLLNode:
    """
    Node class for Singly Linked List
    Uses __slots__ for memory optimization
    """

    __slots__ = ("data", "next")

    def __init__(self, data: Any, next_node: Optional["SLLNode"] = None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    """
    Singly Linked List implementation with comprehensive operations

    Features:
    - O(1) prepend, O(n) append
    - O(1) length check with size counter
    - Support for iteration and built-in functions
    - Comprehensive error handling
    """

    def __init__(self, iterable: Optional[Iterable] = None):
        """
        Initialize empty list or from iterable
        Time Complexity: O(1) for empty, O(n) for iterable
        Space Complexity: O(1) for empty, O(n) for iterable
        """
        self.head: Optional[SLLNode] = None
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
        Iterator protocol support
        Time Complexity: O(n) for full iteration
        Space Complexity: O(1)
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        """
        String representation for debugging
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        elements = list(self)
        return f"SinglyLinkedList({elements})"

    def __str__(self) -> str:
        """
        Human-readable string representation
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.is_empty():
            return "Empty"
        return " -> ".join(str(item) for item in self)

    def _check_index(self, index: int, allow_end: bool = False) -> None:
        """
        Validate index bounds
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        max_index = self._size if allow_end else self._size - 1
        if index < 0 or index > max_index:
            raise IndexError(f"Index {index} out of range [0, {max_index}]")

    # Insertion Operations
    def prepend(self, value: Any) -> None:
        """
        Insert element at the beginning
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = SLLNode(value, self.head)
        self.head = new_node
        self._size += 1

    def append(self, value: Any) -> None:
        """
        Insert element at the end
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = SLLNode(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

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

        # Walk to position index-1
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node = SLLNode(value, current.next)
        current.next = new_node
        self._size += 1

    # Deletion Operations
    def delete_at(self, index: int) -> Any:
        """
        Delete element at specific index and return its value
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        if index == 0:
            # Delete head
            value = self.head.data
            self.head = self.head.next
            self._size -= 1
            return value

        # Walk to position index-1
        current = self.head
        for _ in range(index - 1):
            current = current.next

        # Remove the next node
        node_to_delete = current.next
        value = node_to_delete.data
        current.next = node_to_delete.next
        self._size -= 1
        return value

    def delete_value(self, value: Any) -> bool:
        """
        Delete first occurrence of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        Returns: True if deleted, False if not found
        """
        if not self.head:
            return False

        # Check if head contains the value
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return True

        # Search for the value in the rest of the list
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
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
        self._size -= 1
        return value

    def pop_back(self) -> Any:
        """
        Remove and return last element
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty list")

        if self._size == 1:
            value = self.head.data
            self.head = None
            self._size = 0
            return value

        # Find second-to-last node
        current = self.head
        while current.next.next:
            current = current.next

        value = current.next.data
        current.next = None
        self._size -= 1
        return value

    # Access Operations
    def get(self, index: int) -> Any:
        """
        Get element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set(self, index: int, value: Any) -> None:
        """
        Set element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

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
        self.head = None
        self._size = 0

    def reverse(self) -> None:
        """
        Reverse the list in-place
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def to_list(self) -> list:
        """
        Convert to Python list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return list(self)

    def copy(self) -> "SinglyLinkedList":
        """
        Create a shallow copy
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return SinglyLinkedList(self)

    # Statistical Operations
    def min(self) -> Any:
        """
        Find minimum element
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise ValueError("min() arg is an empty list")

        min_value = self.head.data
        current = self.head.next

        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next

        return min_value

    def max(self) -> Any:
        """
        Find maximum element
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise ValueError("max() arg is an empty list")

        max_value = self.head.data
        current = self.head.next

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


def demonstrate_singly_linked_list():
    """Demonstrate singly linked list operations"""
    print("=== SINGLY LINKED LIST DEMONSTRATION ===\\n")

    # Creation and basic operations
    print("1. CREATION AND BASIC OPERATIONS:")
    sll = SinglyLinkedList([1, 2, 3, 4, 5])
    print(f"   Created from [1,2,3,4,5]: {sll}")
    print(f"   Length: {len(sll)}")
    print(f"   Is empty: {sll.is_empty()}\\n")

    # Insertion operations
    print("2. INSERTION OPERATIONS:")
    sll.prepend(0)
    print(f"   After prepend(0): {sll}")

    sll.append(6)
    print(f"   After append(6): {sll}")

    sll.insert_at(3, 99)
    print(f"   After insert_at(3, 99): {sll}")
    print(f"   Length: {len(sll)}\\n")

    # Access operations
    print("3. ACCESS OPERATIONS:")
    print(f"   Element at index 3: {sll.get(3)}")
    print(f"   Element at index 0: {sll[0]}")  # Using [] syntax

    sll.set(3, 100)
    print(f"   After set(3, 100): {sll}")

    sll[0] = -1  # Using [] syntax
    print(f"   After sll[0] = -1: {sll}\\n")

    # Search operations
    print("4. SEARCH OPERATIONS:")
    print(f"   Find 100: index {sll.find(100)}")
    print(f"   Find 999: index {sll.find(999)}")
    print(f"   Contains 100: {100 in sll}")  # Using 'in' syntax
    print(f"   Count of 1: {sll.count(1)}\\n")

    # Deletion operations
    print("5. DELETION OPERATIONS:")
    deleted = sll.delete_at(0)
    print(f"   Deleted at index 0: {deleted}")
    print(f"   After deletion: {sll}")

    success = sll.delete_value(100)
    print(f"   Delete value 100: {success}")
    print(f"   After deletion: {sll}")

    popped = sll.pop_front()
    print(f"   Popped front: {popped}")
    print(f"   After pop_front: {sll}")

    popped = sll.pop_back()
    print(f"   Popped back: {popped}")
    print(f"   After pop_back: {sll}\\n")

    # Utility operations
    print("6. UTILITY OPERATIONS:")
    print(f"   Original: {sll}")

    sll_copy = sll.copy()
    print(f"   Copy: {sll_copy}")

    sll.reverse()
    print(f"   After reverse: {sll}")

    print(f"   Min element: {sll.min()}")
    print(f"   Max element: {sll.max()}")

    print(f"   As Python list: {sll.to_list()}")


def complexity_analysis():
    """Analyze time complexities of operations"""
    print("\\n=== SINGLY LINKED LIST COMPLEXITY ANALYSIS ===\\n")

    operations = [
        ("Access by index", "O(n)", "Must traverse from head"),
        ("Search", "O(n)", "Linear search required"),
        ("Prepend", "O(1)", "Insert at head"),
        ("Append", "O(n)", "Must traverse to tail"),
        ("Insert at index", "O(n)", "Must traverse to position"),
        ("Delete at index", "O(n)", "Must traverse to position"),
        ("Delete by value", "O(n)", "Must search then delete"),
        ("Length", "O(1)", "Maintained size counter"),
        ("Is empty", "O(1)", "Check size counter"),
        ("Clear", "O(1)", "Drop references"),
        ("Reverse", "O(n)", "Single pass pointer reversal"),
        ("Min/Max", "O(n)", "Must examine all elements"),
    ]

    print(f"{'Operation':<20} {'Time Complexity':<15} {'Notes'}")
    print("-" * 60)
    for op, complexity, notes in operations:
        print(f"{op:<20} {complexity:<15} {notes}")


if __name__ == "__main__":
    demonstrate_singly_linked_list()
    complexity_analysis()
