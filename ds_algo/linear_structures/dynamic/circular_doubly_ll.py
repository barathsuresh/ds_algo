"""
Circular Doubly Linked List Implementation with Sentinel

A circular doubly linked list using a sentinel node to simplify edge cases.
The sentinel acts as both head.prev and tail.next, eliminating null checks.
"""

from typing import Any, Optional, Iterable, Iterator


class CDLLNode:
    """
    Node class for Circular Doubly Linked List
    Uses __slots__ for memory optimization
    """

    __slots__ = ("data", "prev", "next")

    def __init__(self, data: Any = None):
        self.data = data
        self.prev = self
        self.next = self


class CircularDoublyLinkedList:
    """
    Circular Doubly Linked List with Sentinel implementation

    Features:
    - Sentinel node eliminates null checks
    - O(1) operations at both ends
    - Bidirectional traversal
    - Optimized access from nearest end
    """

    def __init__(self, iterable: Optional[Iterable] = None):
        """
        Initialize empty list or from iterable
        Time Complexity: O(1) for empty, O(n) for iterable
        Space Complexity: O(1) for empty, O(n) for iterable
        """
        self.sentinel = CDLLNode()  # Sentinel with no data
        self._size = 0

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
        current = self.sentinel.next
        for _ in range(self._size):
            yield current.data
            current = current.next

    def __reversed__(self) -> Iterator[Any]:
        """
        Reverse iterator protocol support
        Time Complexity: O(n) for full iteration
        Space Complexity: O(1)
        """
        current = self.sentinel.prev
        for _ in range(self._size):
            yield current.data
            current = current.prev

    def __repr__(self) -> str:
        """
        String representation for debugging
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        elements = list(self)
        return f"CircularDoublyLinkedList({elements})"

    def __str__(self) -> str:
        """
        Human-readable string representation showing circularity
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.is_empty():
            return "Empty (Sentinel Only)"

        elements = []
        current = self.sentinel.next
        for i in range(self._size):
            prefix = "[H]" if i == 0 else ""
            elements.append(f"{prefix}{current.data}")
            current = current.next

        return " <-> ".join(elements) + " <-> (back to [H])"

    def _check_index(self, index: int, allow_end: bool = False) -> None:
        """
        Validate index bounds
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        max_index = self._size if allow_end else self._size - 1
        if index < 0 or index > max_index:
            raise IndexError(f"Index {index} out of range [0, {max_index}]")

    def _insert_between(
        self, value: Any, prev_node: CDLLNode, next_node: CDLLNode
    ) -> None:
        """
        Core insertion helper - insert new node between prev_node and next_node
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = CDLLNode(value)
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
        self._size += 1

    # Insertion Operations
    def prepend(self, value: Any) -> None:
        """
        Insert element at the beginning (after sentinel)
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._insert_between(value, self.sentinel, self.sentinel.next)

    def append(self, value: Any) -> None:
        """
        Insert element at the end (before sentinel)
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._insert_between(value, self.sentinel.prev, self.sentinel)

    def insert_at(self, index: int, value: Any) -> None:
        """
        Insert element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index, allow_end=True)

        # Find insertion point
        if index <= self._size // 2:
            # Traverse from head
            current = self.sentinel.next
            for _ in range(index):
                current = current.next
        else:
            # Traverse from tail
            current = self.sentinel
            for _ in range(self._size - index):
                current = current.prev

        self._insert_between(value, current.prev, current)

    # Deletion Operations
    def delete_at(self, index: int) -> Any:
        """
        Delete element at specific index and return its value
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        # Find node to delete
        if index <= self._size // 2:
            # Traverse from head
            current = self.sentinel.next
            for _ in range(index):
                current = current.next
        else:
            # Traverse from tail
            current = self.sentinel.prev
            for _ in range(self._size - 1 - index):
                current = current.prev

        # Remove node
        value = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self._size -= 1
        return value

    def delete_value(self, value: Any) -> bool:
        """
        Delete first occurrence of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        Returns: True if deleted, False if not found
        """
        current = self.sentinel.next

        for _ in range(self._size):
            if current.data == value:
                current.prev.next = current.next
                current.next.prev = current.prev
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

        first_node = self.sentinel.next
        value = first_node.data
        first_node.prev.next = first_node.next
        first_node.next.prev = first_node.prev
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

        last_node = self.sentinel.prev
        value = last_node.data
        last_node.prev.next = last_node.next
        last_node.next.prev = last_node.prev
        self._size -= 1
        return value

    # Access Operations
    def get(self, index: int) -> Any:
        """
        Get element at specific index (optimized to traverse from nearest end)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        if index <= self._size // 2:
            # Traverse from head
            current = self.sentinel.next
            for _ in range(index):
                current = current.next
        else:
            # Traverse from tail
            current = self.sentinel.prev
            for _ in range(self._size - 1 - index):
                current = current.prev

        return current.data

    def set(self, index: int, value: Any) -> None:
        """
        Set element at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        if index <= self._size // 2:
            # Traverse from head
            current = self.sentinel.next
            for _ in range(index):
                current = current.next
        else:
            # Traverse from tail
            current = self.sentinel.prev
            for _ in range(self._size - 1 - index):
                current = current.prev

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
        current = self.sentinel.next

        for i in range(self._size):
            if current.data == value:
                return i
            current = current.next

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

    # Utility Operations
    def clear(self) -> None:
        """
        Remove all elements (reset to sentinel-only state)
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self._size = 0

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

    def copy(self) -> "CircularDoublyLinkedList":
        """
        Create a shallow copy
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return CircularDoublyLinkedList(self)

    # Circular-specific Operations
    def rotate_forward(self, steps: int) -> None:
        """
        Rotate the list forward by steps positions
        Time Complexity: O(min(steps, n))
        Space Complexity: O(1)
        """
        if self.is_empty() or steps <= 0:
            return

        steps = steps % self._size if self._size > 0 else 0
        if steps == 0:
            return

        # Find the new head (current head + steps)
        new_head = self.sentinel.next
        for _ in range(steps):
            new_head = new_head.next

        # The new tail is the node before new head
        new_tail = new_head.prev

        # Extract the rotated portion
        self.sentinel.next = new_head
        new_head.prev = self.sentinel
        self.sentinel.prev = new_tail
        new_tail.next = self.sentinel

    def rotate_backward(self, steps: int) -> None:
        """
        Rotate the list backward by steps positions
        Time Complexity: O(min(steps, n))
        Space Complexity: O(1)
        """
        if self.is_empty() or steps <= 0:
            return

        steps = steps % self._size if self._size > 0 else 0
        if steps == 0:
            return

        # Rotating backward by k is same as rotating forward by (n-k)
        self.rotate_forward(self._size - steps)

    def is_circular_consistent(self) -> bool:
        """
        Verify the circular structure integrity
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty():
            return (
                self.sentinel.next == self.sentinel
                and self.sentinel.prev == self.sentinel
            )

        # Check forward direction
        current = self.sentinel.next
        count = 0
        while current != self.sentinel and count < self._size + 1:
            count += 1
            current = current.next

        if count != self._size or current != self.sentinel:
            return False

        # Check backward direction
        current = self.sentinel.prev
        count = 0
        while current != self.sentinel and count < self._size + 1:
            count += 1
            current = current.prev

        return count == self._size and current == self.sentinel


def demonstrate_circular_doubly_linked_list():
    """Demonstrate circular doubly linked list operations"""
    print("=== CIRCULAR DOUBLY LINKED LIST DEMONSTRATION ===\n")

    # Creation and basic operations
    print("1. CREATION AND SENTINEL STRUCTURE:")
    cdll = CircularDoublyLinkedList([1, 2, 3, 4])
    print(f"   Created from [1,2,3,4]: {cdll}")
    print(f"   Length: {len(cdll)}")
    print(f"   Is circular consistent: {cdll.is_circular_consistent()}")
    print(f"   Sentinel.next data (head): {cdll.sentinel.next.data}")
    print(f"   Sentinel.prev data (tail): {cdll.sentinel.prev.data}\n")

    # Bidirectional traversal
    print("2. BIDIRECTIONAL TRAVERSAL:")
    print(f"   Forward: {list(cdll)}")
    print(f"   Backward: {list(reversed(cdll))}\n")

    # Insertion operations (all O(1) at ends)
    print("3. INSERTION OPERATIONS:")
    cdll.prepend(0)
    print(f"   After prepend(0): {cdll}")

    cdll.append(5)
    print(f"   After append(5): {cdll}")

    cdll.insert_at(3, 99)
    print(f"   After insert_at(3, 99): {cdll}")
    print(f"   Length: {len(cdll)}\n")

    # Access operations (optimized from nearest end)
    print("4. ACCESS OPERATIONS (Optimized from nearest end):")
    print(f"   Element at index 0 (from head): {cdll.get(0)}")
    print(f"   Element at index -1 (from tail): {cdll.get(len(cdll)-1)}")
    print(f"   Element at index 3 (middle): {cdll.get(3)}")

    cdll.set(3, 100)
    print(f"   After set(3, 100): {cdll}\n")

    # Deletion operations
    print("5. DELETION OPERATIONS:")
    deleted_front = cdll.pop_front()
    print(f"   Popped front: {deleted_front}")
    print(f"   After pop_front: {cdll}")

    deleted_back = cdll.pop_back()
    print(f"   Popped back: {deleted_back}")
    print(f"   After pop_back: {cdll}")

    deleted_at = cdll.delete_at(2)
    print(f"   Deleted at index 2: {deleted_at}")
    print(f"   After delete_at(2): {cdll}")

    deleted_value = cdll.delete_value(2)
    print(f"   Delete value 2: {deleted_value}")
    print(f"   After delete_value(2): {cdll}\n")

    # Circular-specific operations
    print("6. CIRCULAR-SPECIFIC OPERATIONS:")
    print(f"   Before rotation: {cdll}")

    cdll_copy = cdll.copy()
    cdll_copy.rotate_forward(2)
    print(f"   After rotate_forward(2): {cdll_copy}")

    cdll_copy.rotate_backward(1)
    print(f"   After rotate_backward(1): {cdll_copy}")

    print(f"   Circular consistency check: {cdll.is_circular_consistent()}\n")

    # Demonstrate sentinel advantage
    print("7. SENTINEL ADVANTAGES:")
    print("   - No null checks needed for insertion/deletion")
    print("   - Simplifies edge cases (empty list operations)")
    print("   - Consistent circular structure")
    print("   - O(1) operations at both ends")


def complexity_comparison_table():
    """Compare complexities across all linked list variants"""
    print("\n=== COMPREHENSIVE LINKED LIST COMPLEXITY COMPARISON ===\n")

    operations = [
        ("Operation", "Singly", "Doubly", "Circular S", "Circular D", "Best"),
        ("-" * 12, "-" * 7, "-" * 7, "-" * 9, "-" * 9, "-" * 8),
        ("Prepend", "O(1)", "O(1)", "O(1)", "O(1)", "All equal"),
        ("Append", "O(n)", "O(1)", "O(1)", "O(1)", "✅ Not singly"),
        ("Pop front", "O(1)", "O(1)", "O(n)*", "O(1)", "✅ Non-circular"),
        ("Pop back", "O(n)", "O(1)", "O(n)", "O(1)", "✅ Doubly"),
        ("Insert middle", "O(n)", "O(n)", "O(n)", "O(n)", "Doubly (~2x faster)"),
        ("Delete middle", "O(n)", "O(n)", "O(n)", "O(n)", "Doubly (~2x faster)"),
        ("Access by index", "O(n)", "O(n)", "O(n)", "O(n)", "Doubly (~2x faster)"),
        ("Reverse traverse", "No", "O(n)", "No", "O(n)", "✅ Doubly only"),
        ("Memory/node", "2 ptr", "3 ptr", "2 ptr", "3 ptr", "Singly least"),
        ("Circular ops", "No", "No", "Yes", "Yes", "✅ Circular only"),
    ]

    for row in operations:
        print(f"{row[0]:<12} {row[1]:<7} {row[2]:<7} {row[3]:<9} {row[4]:<9} {row[5]}")

    print("\n* Circular Singly: pop_front needs O(n) to find previous node")


def practical_applications():
    """Show practical applications of circular doubly linked lists"""
    print("\n=== PRACTICAL APPLICATIONS ===\n")

    print("1. ADVANCED MUSIC PLAYLIST:")
    playlist = CircularDoublyLinkedList(["Song_A", "Song_B", "Song_C", "Song_D"])
    print(f"   Playlist: {playlist}")

    # Simulate media player operations
    print("   Media player operations:")
    print(f"   Current: {playlist.sentinel.next.data}")

    # Next song
    playlist.rotate_forward(1)
    print(f"   Next: {playlist.sentinel.next.data}")

    # Previous song
    playlist.rotate_backward(1)
    print(f"   Previous: {playlist.sentinel.next.data}")

    # Shuffle (rotate by random amount)
    playlist.rotate_forward(3)
    print(f"   After shuffle: {playlist.sentinel.next.data}")
    print()

    print("2. BROWSER TAB MANAGEMENT:")
    tabs = CircularDoublyLinkedList(["Home", "Gmail", "GitHub", "StackOverflow"])
    print(f"   Open tabs: {tabs}")

    # Add new tab at current position
    tabs.insert_at(2, "Documentation")
    print(f"   After opening new tab: {tabs}")

    # Close current tab
    current_closed = tabs.delete_at(2)
    print(f"   Closed tab: {current_closed}")
    print(f"   Remaining tabs: {tabs}")
    print()

    print("3. UNDO/REDO BUFFER (with rotation):")
    actions = CircularDoublyLinkedList(["action1", "action2", "action3", "action4"])
    print(f"   Action history: {actions}")

    # Add new action (overwrites old ones when buffer is full)
    actions.pop_back()  # Remove oldest
    actions.prepend("action5")  # Add newest
    print(f"   After new action: {actions}")

    # Undo (move backward)
    actions.rotate_backward(1)
    print(f"   After undo: Current action is {actions.sentinel.next.data}")

    # Redo (move forward)
    actions.rotate_forward(1)
    print(f"   After redo: Current action is {actions.sentinel.next.data}")


if __name__ == "__main__":
    demonstrate_circular_doubly_linked_list()
    complexity_comparison_table()
    practical_applications()
