"""
Circular Singly Linked List Implementation

A circular singly linked list where the last node points back to the first node,
forming a ring. Maintains a tail pointer for O(1) operations at both ends.
"""

from typing import Any, Optional, Iterable, Iterator


class CSLLNode:
    """
    Node class for Circular Singly Linked List
    Uses __slots__ for memory optimization
    """

    __slots__ = ("data", "next")

    def __init__(self, data: Any, next_node: Optional["CSLLNode"] = None):
        self.data = data
        self.next = next_node


class CircularSinglyLinkedList:
    """
    Circular Singly Linked List implementation

    Features:
    - Circular structure: tail.next points to head
    - O(1) append and prepend operations
    - Maintains tail pointer for efficient operations
    - Careful iteration to avoid infinite loops
    """

    def __init__(self, iterable: Optional[Iterable] = None):
        """
        Initialize empty list or from iterable
        Time Complexity: O(1) for empty, O(n) for iterable
        Space Complexity: O(1) for empty, O(n) for iterable
        """
        self.tail: Optional[CSLLNode] = None
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

    @property
    def head(self) -> Optional[CSLLNode]:
        """
        Get the head node (tail.next if list is not empty)
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.tail.next if self.tail else None

    def __iter__(self) -> Iterator[Any]:
        """
        Iterator protocol support - exactly one full circle
        Time Complexity: O(n) for full iteration
        Space Complexity: O(1)
        """
        if self.is_empty():
            return

        current = self.head
        for _ in range(self._size):
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        """
        String representation for debugging
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        elements = list(self)
        return f"CircularSinglyLinkedList({elements})"

    def __str__(self) -> str:
        """
        Human-readable string representation showing circularity
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.is_empty():
            return "Empty"

        elements = []
        current = self.head
        for i in range(self._size):
            prefix = "[H]" if i == 0 else ""
            elements.append(f"{prefix}{current.data}")
            current = current.next

        return " -> ".join(elements) + " -> (back to [H])"

    def _check_index(self, index: int, allow_end: bool = False) -> None:
        """
        Validate index bounds
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        max_index = self._size if allow_end else self._size - 1
        if index < 0 or index > max_index:
            raise IndexError(f"Index {index} out of range [0, {max_index}]")

    def _node_at(self, index: int) -> CSLLNode:
        """
        Get node at specific index
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # Insertion Operations
    def prepend(self, value: Any) -> None:
        """
        Insert element at the beginning (new head)
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = CSLLNode(value)

        if self.is_empty():
            # Single node points to itself
            new_node.next = new_node
            self.tail = new_node
        else:
            # Insert between tail and head
            new_node.next = self.tail.next
            self.tail.next = new_node

        self._size += 1

    def append(self, value: Any) -> None:
        """
        Insert element at the end (new tail)
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = CSLLNode(value)

        if self.is_empty():
            # Single node points to itself
            new_node.next = new_node
            self.tail = new_node
        else:
            # Insert after current tail
            new_node.next = self.tail.next
            self.tail.next = new_node
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

        # Find node at position index-1
        prev = self._node_at(index - 1)
        new_node = CSLLNode(value, prev.next)
        prev.next = new_node
        self._size += 1

    # Deletion Operations
    def delete_at(self, index: int) -> Any:
        """
        Delete element at specific index and return its value
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        if self._size == 1:
            # Single node case
            value = self.tail.data
            self.tail = None
            self._size = 0
            return value

        # Find previous node
        if index == 0:
            # Deleting head: start from tail
            prev = self.tail
            node_to_delete = self.head
        else:
            # Find node at position index-1
            prev = self._node_at(index - 1)
            node_to_delete = prev.next

        value = node_to_delete.data
        prev.next = node_to_delete.next

        # Update tail if we deleted it
        if node_to_delete is self.tail:
            self.tail = prev

        self._size -= 1
        return value

    def delete_value(self, value: Any) -> bool:
        """
        Delete first occurrence of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        Returns: True if deleted, False if not found
        """
        if self.is_empty():
            return False

        # Special case: single node
        if self._size == 1:
            if self.tail.data == value:
                self.tail = None
                self._size = 0
                return True
            return False

        # Search for the value
        prev = self.tail  # Start with prev at tail
        current = self.head  # And current at head

        for _ in range(self._size):
            if current.data == value:
                prev.next = current.next

                # Update tail if we deleted it
                if current is self.tail:
                    self.tail = prev

                self._size -= 1
                return True

            prev = current
            current = current.next

        return False

    def pop_front(self) -> Any:
        """
        Remove and return first element
        Time Complexity: O(1) for deletion, but O(n) to find previous node
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty list")

        return self.delete_at(0)

    def pop_back(self) -> Any:
        """
        Remove and return last element
        Time Complexity: O(n) to find previous node
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty list")

        return self.delete_at(self._size - 1)

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
        if self.is_empty():
            return -1

        current = self.head
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

    def count(self, value: Any) -> int:
        """
        Count occurrences of value
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty():
            return 0

        count = 0
        current = self.head
        for _ in range(self._size):
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
        self.tail = None
        self._size = 0

    def to_list(self) -> list:
        """
        Convert to Python list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return list(self)

    def copy(self) -> "CircularSinglyLinkedList":
        """
        Create a shallow copy
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return CircularSinglyLinkedList(self)

    # Circular-specific Operations
    def rotate(self, steps: int) -> None:
        """
        Rotate the circular list by steps positions
        Positive steps rotate forward, negative steps rotate backward
        Time Complexity: O(|steps|) for small steps, O(1) for large steps
        Space Complexity: O(1)
        """
        if self.is_empty() or self._size == 1:
            return

        # Normalize steps to be within [0, size)
        steps = steps % self._size
        if steps == 0:
            return

        # Move tail pointer steps positions forward
        for _ in range(steps):
            self.tail = self.tail.next

    def split_at(
        self, index: int
    ) -> tuple["CircularSinglyLinkedList", "CircularSinglyLinkedList"]:
        """
        Split the circular list at given index into two circular lists
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self._check_index(index)

        if index == 0:
            # Return empty list and current list
            return CircularSinglyLinkedList(), self.copy()

        # Find split point
        split_prev = self._node_at(index - 1)
        split_node = split_prev.next

        # Create first list (0 to index-1)
        first_list = CircularSinglyLinkedList()
        if index > 0:
            first_list.tail = split_prev
            first_list._size = index
            split_prev.next = self.head  # Make it circular

        # Create second list (index to end)
        second_list = CircularSinglyLinkedList()
        if index < self._size:
            second_list.tail = self.tail
            second_list._size = self._size - index
            self.tail.next = split_node  # Make it circular

        return first_list, second_list

    def traverse_n_times(self, n: int) -> Iterator[Any]:
        """
        Traverse the circular list n times (useful for demonstrating circularity)
        Time Complexity: O(n * size)
        Space Complexity: O(1)
        """
        if self.is_empty():
            return

        current = self.head
        for _ in range(n * self._size):
            yield current.data
            current = current.next


def demonstrate_circular_singly_linked_list():
    """Demonstrate circular singly linked list operations"""
    print("=== CIRCULAR SINGLY LINKED LIST DEMONSTRATION ===\n")

    # Creation and basic operations
    print("1. CREATION AND CIRCULAR STRUCTURE:")
    csll = CircularSinglyLinkedList([1, 2, 3, 4])
    print(f"   Created from [1,2,3,4]: {csll}")
    print(f"   Length: {len(csll)}")
    print(f"   Head data: {csll.head.data}")
    print(f"   Tail data: {csll.tail.data}")
    print(f"   Tail.next data (should be head): {csll.tail.next.data}\n")

    # Demonstrate circularity
    print("2. CIRCULARITY DEMONSTRATION:")
    print("   Traversing 2.5 times around the circle:")
    circle_data = list(csll.traverse_n_times(2.5))[:10]  # Show first 10 elements
    print(f"   {' -> '.join(map(str, circle_data))} -> ...")
    print()

    # Insertion operations
    print("3. INSERTION OPERATIONS:")
    csll.prepend(0)
    print(f"   After prepend(0): {csll}")

    csll.append(5)
    print(f"   After append(5): {csll}")

    csll.insert_at(3, 99)
    print(f"   After insert_at(3, 99): {csll}")
    print(f"   Length: {len(csll)}\n")

    # Access operations
    print("4. ACCESS OPERATIONS:")
    print(f"   Element at index 0: {csll.get(0)}")
    print(f"   Element at index 3: {csll.get(3)}")

    csll.set(3, 100)
    print(f"   After set(3, 100): {csll}")
    print(f"   Element at index 3: {csll[3]}\n")  # Using [] syntax

    # Search operations
    print("5. SEARCH OPERATIONS:")
    print(f"   Find 100: index {csll.find(100)}")
    print(f"   Find 999: index {csll.find(999)}")
    print(f"   Contains 5: {5 in csll}")
    print(f"   Count of 1: {csll.count(1)}\n")

    # Circular-specific operations
    print("6. CIRCULAR-SPECIFIC OPERATIONS:")
    print(f"   Before rotation: {csll}")

    csll_copy = csll.copy()
    csll_copy.rotate(2)
    print(f"   After rotate(2): {csll_copy}")

    csll_copy.rotate(-1)
    print(f"   After rotate(-1): {csll_copy}")
    print()

    # Split operation
    print("7. SPLIT OPERATION:")
    first_half, second_half = csll.split_at(3)
    print(f"   Original: {csll}")
    print(f"   Split at index 3:")
    print(f"   First half: {first_half}")
    print(f"   Second half: {second_half}\n")

    # Deletion operations
    print("8. DELETION OPERATIONS:")
    deleted = csll.delete_at(0)
    print(f"   Deleted at index 0: {deleted}")
    print(f"   After deletion: {csll}")

    success = csll.delete_value(100)
    print(f"   Delete value 100: {success}")
    print(f"   After deletion: {csll}")

    # Verify circularity is maintained
    print(f"   Tail.next still points to head: {csll.tail.next.data == csll.head.data}")


def circular_vs_linear_comparison():
    """Compare circular and linear linked lists"""
    print("\n=== CIRCULAR vs LINEAR LINKED LIST COMPARISON ===\n")

    comparisons = [
        ("Aspect", "Linear SLL", "Circular SLL", "Notes"),
        ("-" * 15, "-" * 10, "-" * 12, "-" * 25),
        ("Last->Next", "None", "Points to Head", "Key difference"),
        ("Append", "O(n)", "O(1)", "✅ Tail pointer advantage"),
        ("Prepend", "O(1)", "O(1)", "Same performance"),
        ("Iteration", "Natural end", "Must count steps", "Risk of infinite loop"),
        ("Memory", "n nodes", "n nodes", "Same memory usage"),
        ("Use Cases", "Linear data", "Round-robin", "Different applications"),
        ("Split/Merge", "Natural", "Requires care", "Circular maintenance"),
    ]

    for row in comparisons:
        print(f"{row[0]:<15} {row[1]:<10} {row[2]:<12} {row[3]}")


def use_cases():
    """Demonstrate practical use cases for circular linked lists"""
    print("\n=== PRACTICAL USE CASES ===\n")

    print("1. ROUND-ROBIN SCHEDULING:")
    processes = CircularSinglyLinkedList(["Process_A", "Process_B", "Process_C"])
    print("   CPU Time allocation:")

    current_process = processes.head
    for i in range(8):  # Simulate 8 time slices
        print(f"   Time slice {i+1}: {current_process.data}")
        current_process = current_process.next
    print()

    print("2. CIRCULAR BUFFER SIMULATION:")
    buffer = CircularSinglyLinkedList(["slot1", "slot2", "slot3"])
    print(f"   Buffer: {buffer}")
    print("   Writing data in circular fashion...")

    data_to_write = ["data_A", "data_B", "data_C", "data_D", "data_E"]
    slot = buffer.head

    for i, data in enumerate(data_to_write):
        print(f"   Write '{data}' to {slot.data}")
        slot = slot.next  # Move to next slot in circular fashion
    print()

    print("3. GAME TURN MANAGEMENT:")
    players = CircularSinglyLinkedList(["Alice", "Bob", "Charlie", "Diana"])
    print("   Turn order for multiple rounds:")

    current_player = players.head
    for turn in range(12):  # Simulate 12 turns
        round_num = turn // len(players) + 1
        turn_in_round = turn % len(players) + 1
        print(f"   Round {round_num}, Turn {turn_in_round}: {current_player.data}")
        current_player = current_player.next


if __name__ == "__main__":
    demonstrate_circular_singly_linked_list()
    circular_vs_linear_comparison()
    use_cases()
