"""
Stack Implementations - LIFO Abstract Data Type

A Stack is a Last-In-First-Out (LIFO) abstract data type that supports:
- push(x): Add element to top
- pop(): Remove and return top element
- peek(): View top element without removing
- is_empty(): Check if stack is empty
- size(): Get number of elements

This module provides two implementations:
1. ArrayStack: Uses dynamic array (Python list) with amortized O(1) operations
2. LinkedStack: Uses linked list with exact O(1) operations

Time Complexity Comparison:
┌─────────────┬──────────────┬──────────────┬─────────────────────────┐
│ Operation   │ ArrayStack   │ LinkedStack  │ Notes                   │
├─────────────┼──────────────┼──────────────┼─────────────────────────┤
│ push(x)     │ O(1)*        │ O(1)         │ Array amortized         │
│ pop()       │ O(1)*        │ O(1)         │ Array amortized         │
│ peek()      │ O(1)         │ O(1)         │                         │
│ is_empty()  │ O(1)         │ O(1)         │                         │
│ size()      │ O(1)         │ O(1)         │                         │
│ clear()     │ O(1)         │ O(1)         │                         │
└─────────────┴──────────────┴──────────────┴─────────────────────────┘

Space Complexity:
- ArrayStack: O(n) with potential for unused capacity
- LinkedStack: O(n) with exact memory usage (no wasted space)

*Amortized: Occasional O(n) operations when resizing, but O(1) on average
"""

from typing import Any, Optional, Iterable


class StackNode:
    """
    Node for linked list implementation of stack.

    Uses __slots__ for memory efficiency and faster attribute access.
    """

    __slots__ = ("data", "next")

    def __init__(self, data: Any, next: Optional["StackNode"] = None) -> None:
        """Initialize a stack node.

        Args:
            data: The payload/value stored in this node
            next: Reference to the next node (towards old head)
        """
        self.data = data
        self.next = next


class ArrayStack:
    """
    Array-based stack implementation using Python's dynamic list.

    Pros:
    - Memory locality (better cache performance)
    - Lower per-element memory overhead
    - Simple implementation

    Cons:
    - Amortized time complexity (occasional O(n) resizing)
    - May waste memory due to capacity > size
    """

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """Initialize stack with optional initial values.

        Args:
            iterable: Optional sequence of values to push onto stack

        Example:
            >>> stack = ArrayStack([1, 2, 3])  # 3 is on top
            >>> stack.peek()
            3
        """
        self._a = []  # Underlying dynamic Python list
        if iterable is not None:
            for x in iterable:
                self.push(x)  # Use push for uniform behavior

    def push(self, x: Any) -> None:
        """Push element onto top of stack.

        Time: O(1) amortized - occasional O(n) when list grows
        Space: O(1)

        Args:
            x: Element to add to stack
        """
        self._a.append(x)  # Python list append is amortized O(1)

    def pop(self) -> Any:
        """Remove and return top element from stack.

        Time: O(1) amortized
        Space: O(1)

        Returns:
            Top element that was removed

        Raises:
            IndexError: If stack is empty
        """
        if not self._a:
            raise IndexError("pop from empty stack")
        return self._a.pop()  # Remove and return last element

    def peek(self) -> Any:
        """View top element without removing it.

        Time: O(1)
        Space: O(1)

        Returns:
            Top element (without removing)

        Raises:
            IndexError: If stack is empty
        """
        if not self._a:
            raise IndexError("peek from empty stack")
        return self._a[-1]  # Last element is the top

    def is_empty(self) -> bool:
        """Check if stack has no elements.

        Time: O(1)
        Space: O(1)

        Returns:
            True if stack is empty, False otherwise
        """
        return len(self._a) == 0

    def size(self) -> int:
        """Get number of elements in stack.

        Time: O(1)
        Space: O(1)

        Returns:
            Number of elements currently in stack
        """
        return len(self._a)

    def clear(self) -> None:
        """Remove all elements from stack.

        Time: O(1)
        Space: O(1)
        """
        self._a.clear()  # Python list clear is O(1)

    def __repr__(self) -> str:
        """Developer-friendly string representation."""
        return f"ArrayStack({self._a})"


class LinkedStack:
    """
    Linked list-based stack implementation.

    Pros:
    - Exact O(1) time complexity (no amortization)
    - No wasted memory (allocates exactly what's needed)
    - No capacity limits

    Cons:
    - Higher per-element memory overhead (pointer storage)
    - Potentially worse cache locality
    - More complex memory management
    """

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """Initialize linked stack with optional initial values.

        Args:
            iterable: Optional sequence of values to push onto stack
        """
        self.head = None  # Top of stack (None if empty)
        self._size = 0  # Size counter for O(1) size queries
        if iterable is not None:
            for x in iterable:
                self.push(x)

    def push(self, x: Any) -> None:
        """Push element onto top of stack.

        Time: O(1) exact
        Space: O(1)

        Args:
            x: Element to add to stack
        """
        self.head = StackNode(x, self.head)  # Create node and link to old head
        self._size += 1

    def pop(self) -> Any:
        """Remove and return top element from stack.

        Time: O(1) exact
        Space: O(1)

        Returns:
            Top element that was removed

        Raises:
            IndexError: If stack is empty
        """
        if not self.head:
            raise IndexError("pop from empty stack")
        x = self.head.data  # Capture top value
        self.head = self.head.next  # Move head to next node
        self._size -= 1
        return x

    def peek(self) -> Any:
        """View top element without removing it.

        Time: O(1)
        Space: O(1)

        Returns:
            Top element (without removing)

        Raises:
            IndexError: If stack is empty
        """
        if not self.head:
            raise IndexError("peek from empty stack")
        return self.head.data

    def is_empty(self) -> bool:
        """Check if stack has no elements.

        Time: O(1)
        Space: O(1)

        Returns:
            True if stack is empty, False otherwise
        """
        return self._size == 0

    def size(self) -> int:
        """Get number of elements in stack.

        Time: O(1)
        Space: O(1)

        Returns:
            Number of elements currently in stack
        """
        return self._size

    def clear(self) -> None:
        """Remove all elements from stack.

        Time: O(1)
        Space: O(1)
        """
        self.head = None  # Drop head reference (GC will clean up)
        self._size = 0

    def __repr__(self) -> str:
        """Debug-friendly string representation showing top->bottom order."""
        vals = []
        cur = self.head
        while cur is not None:
            vals.append(cur.data)
            cur = cur.next
        return f"LinkedStack(top-> {vals})"


# ========== Visualization Utilities ==========


def _stack_items(stack):
    """Extract items from stack in TOP to BOTTOM order as a list.

    Args:
        stack: Either ArrayStack or LinkedStack instance

    Returns:
        List of items from top to bottom
    """
    # Array-backed: top is at end of the list -> reverse to show top first
    if hasattr(stack, "_a"):
        return list(reversed(stack._a))

    # Linked-backed: head is the top -> traverse forward
    vals, cur = [], getattr(stack, "head", None)
    while cur is not None:
        vals.append(cur.data)
        cur = cur.next
    return vals


def print_stack_vertical(stack):
    """Print stack in vertical format showing LIFO structure.

    Output format:
        TOP
        │ x │
        │ y │
        │ z │
        BOTTOM

    Args:
        stack: Stack instance to visualize
    """
    items = _stack_items(stack)
    if not items:
        print("Stack is Empty\n")
        return

    print("TOP")
    for item in items:
        print(f"│ {item} │")
    print("BOTTOM\n")


def show_stack(stage: str, stack):
    """Display stack state with label, visualization, and metadata.

    Args:
        stage: Description label for current operation
        stack: Stack instance to display
    """
    print(f"{stage}")
    print_stack_vertical(stack)
    print(f"(len={stack.size()})\n")


# ========== Test Suite ==========


def run_stack_tests():
    """Comprehensive test suite for both stack implementations."""
    print("=== Stack Tests (ArrayStack) ===")

    # Test ArrayStack
    a = ArrayStack([10, 20, 30])
    show_stack("Init ArrayStack [10,20,30]", a)

    a.push(40)
    show_stack("After push(40)", a)

    # Test peek
    assert a.peek() == 40
    print(f"peek() -> {a.peek()}\n")

    # Test pop
    assert a.pop() == 40
    show_stack("After pop()", a)

    # Test clear
    a.clear()
    show_stack("After clear()", a)

    # Test error handling
    try:
        a.pop()
    except IndexError as e:
        print(f"pop() on empty -> IndexError: {e}\n")

    print("=== Stack Tests (LinkedStack) ===")

    # Test LinkedStack
    l = LinkedStack([1, 2, 3])
    show_stack("Init LinkedStack [1,2,3]", l)

    l.push(4)
    show_stack("After push(4)", l)

    # Test peek
    assert l.peek() == 4
    print(f"peek() -> {l.peek()}\n")

    # Test pop
    assert l.pop() == 4
    show_stack("After pop()", l)

    # Test clear
    l.clear()
    show_stack("After clear()", l)

    # Test error handling
    try:
        l.peek()
    except IndexError as e:
        print(f"peek() on empty -> IndexError: {e}\n")

    print("✅ Stack tests passed!\n")


def demonstrate_stack_applications():
    """Demonstrate real-world applications of stacks."""
    print("=== Stack Applications Demo ===\n")

    # 1. Parentheses matching
    def is_balanced_parentheses(expression: str) -> bool:
        """Check if parentheses are balanced using a stack."""
        stack = ArrayStack()
        opening = {"(", "[", "{"}
        closing = {")", "]", "}"}
        pairs = {"(": ")", "[": "]", "{": "}"}

        for char in expression:
            if char in opening:
                stack.push(char)
            elif char in closing:
                if stack.is_empty():
                    return False
                if pairs[stack.pop()] != char:
                    return False

        return stack.is_empty()

    print("1. Balanced Parentheses Checker:")
    test_expressions = ["()", "()[]{}", "((()))", "([)]", "((", "))"]
    for expr in test_expressions:
        result = is_balanced_parentheses(expr)
        print(f"   '{expr}' -> {'✓ Balanced' if result else '✗ Not balanced'}")

    # 2. Reverse string
    def reverse_string(s: str) -> str:
        """Reverse a string using a stack."""
        stack = LinkedStack(s)  # Push each character
        result = ""
        while not stack.is_empty():
            result += stack.pop()
        return result

    print(f"\n2. String Reversal:")
    original = "HELLO"
    reversed_str = reverse_string(original)
    print(f"   '{original}' -> '{reversed_str}'")

    # 3. Function call simulation
    def simulate_function_calls():
        """Simulate function call stack."""
        call_stack = ArrayStack()

        print(f"\n3. Function Call Stack Simulation:")
        print("   Calling: main() -> func1() -> func2()")

        call_stack.push("main()")
        print(f"   Call stack: {call_stack}")

        call_stack.push("func1()")
        print(f"   Call stack: {call_stack}")

        call_stack.push("func2()")
        print(f"   Call stack: {call_stack}")

        print("   Returning from functions...")
        while not call_stack.is_empty():
            returned = call_stack.pop()
            print(f"   Returned from: {returned}, stack: {call_stack}")

    simulate_function_calls()
    print()


if __name__ == "__main__":
    """Run tests and demonstrations when file is executed directly."""
    run_stack_tests()
    demonstrate_stack_applications()
