"""
Queue Implementations - FIFO Abstract Data Type

A Queue is a First-In-First-Out (FIFO) abstract data type that supports:
- enqueue(x): Add element to rear
- dequeue(): Remove and return front element
- front(): View front element without removing
- rear(): View rear element without removing
- is_empty(): Check if queue is empty
- size(): Get number of elements

This module provides two implementations:
1. ArrayQueue: Uses circular buffer with amortized O(1) operations
2. LinkedQueue: Uses linked list with exact O(1) operations

Time Complexity Comparison:
┌─────────────┬──────────────┬──────────────┬─────────────────────────┐
│ Operation   │ ArrayQueue   │ LinkedQueue  │ Notes                   │
├─────────────┼──────────────┼──────────────┼─────────────────────────┤
│ enqueue(x)  │ O(1)*        │ O(1)         │ Array amortized         │
│ dequeue()   │ O(1)*        │ O(1)         │ Array amortized         │
│ front()     │ O(1)         │ O(1)         │                         │
│ rear()      │ O(1)         │ O(1)         │                         │
│ is_empty()  │ O(1)         │ O(1)         │                         │
│ size()      │ O(1)         │ O(1)         │                         │
│ clear()     │ O(1)         │ O(1)         │                         │
└─────────────┴──────────────┴──────────────┴─────────────────────────┘

Space Complexity:
- ArrayQueue: O(n) with potential for unused capacity (circular buffer)
- LinkedQueue: O(n) with exact memory usage plus pointer overhead

Key Implementation Details:
- ArrayQueue uses modular arithmetic for circular indexing
- LinkedQueue maintains both head and tail pointers for O(1) enqueue/dequeue
- Both implementations handle edge cases (empty queue operations)

*Amortized: Occasional O(n) operations when resizing, but O(1) on average
"""

from typing import Any, Optional, Iterable


class QNode:
    """
    Node for linked list implementation of queue.

    Uses __slots__ for memory efficiency and faster attribute access.
    """

    __slots__ = ("data", "next")

    def __init__(self, data: Any, next: Optional["QNode"] = None) -> None:
        """Initialize a queue node.

        Args:
            data: The payload/value stored in this node
            next: Reference to the next node in queue
        """
        self.data = data
        self.next = next


class ArrayQueue:
    """
    Array-based queue implementation using circular buffer.

    Uses modular arithmetic to wrap head/tail pointers, avoiding the need
    to shift elements. When capacity is reached, the buffer doubles in size.

    Pros:
    - Memory locality (better cache performance)
    - Lower per-element memory overhead
    - Predictable memory usage patterns

    Cons:
    - Amortized time complexity (occasional O(n) resizing)
    - May waste memory due to capacity > size
    - More complex circular buffer logic
    """

    def __init__(self, capacity: int = 8) -> None:
        """Initialize queue with specified capacity.

        Args:
            capacity: Initial buffer size (must be positive)

        Raises:
            ValueError: If capacity <= 0
        """
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._a = [None] * capacity  # Fixed-size list holding elements
        self._head = 0  # Index of current front element
        self._tail = 0  # Index of next insertion position
        self._size = 0  # Number of elements in queue

    def _grow(self) -> None:
        """Double the buffer capacity and reorganize elements.

        Copies elements in logical order (front to rear) to new buffer,
        resetting head to 0 and tail to current size.

        Time: O(n) - must copy all elements
        Space: O(n) - allocates new buffer
        """
        new_cap = len(self._a) * 2
        new_a = [None] * new_cap

        # Copy elements in logical order (front -> rear)
        for i in range(self._size):
            new_a[i] = self._a[(self._head + i) % len(self._a)]

        self._a = new_a  # Switch to new buffer
        self._head = 0  # Reset head to beginning
        self._tail = self._size  # Tail points to next free slot

    def enqueue(self, x: Any) -> None:
        """Add element to rear of queue.

        Time: O(1) amortized - occasional O(n) when buffer grows
        Space: O(1)

        Args:
            x: Element to add to queue
        """
        if self._size == len(self._a):  # Buffer is full
            self._grow()

        self._a[self._tail] = x
        self._tail = (self._tail + 1) % len(self._a)  # Circular increment
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return front element from queue.

        Time: O(1)
        Space: O(1)

        Returns:
            Front element that was removed

        Raises:
            IndexError: If queue is empty
        """
        if self._size == 0:
            raise IndexError("dequeue from empty queue")

        x = self._a[self._head]
        self._a[self._head] = None  # Help garbage collector
        self._head = (self._head + 1) % len(self._a)  # Circular increment
        self._size -= 1
        return x

    def front(self) -> Any:
        """View front element without removing it.

        Time: O(1)
        Space: O(1)

        Returns:
            Front element (without removing)

        Raises:
            IndexError: If queue is empty
        """
        if self._size == 0:
            raise IndexError("front from empty queue")
        return self._a[self._head]

    def rear(self) -> Any:
        """View rear element without removing it.

        Time: O(1)
        Space: O(1)

        Returns:
            Rear element (without removing)

        Raises:
            IndexError: If queue is empty
        """
        if self._size == 0:
            raise IndexError("rear from empty queue")
        return self._a[(self._tail - 1) % len(self._a)]

    def is_empty(self) -> bool:
        """Check if queue has no elements.

        Time: O(1)
        Space: O(1)

        Returns:
            True if queue is empty, False otherwise
        """
        return self._size == 0

    def size(self) -> int:
        """Get number of elements in queue.

        Time: O(1)
        Space: O(1)

        Returns:
            Number of elements currently in queue
        """
        return self._size

    def clear(self) -> None:
        """Remove all elements from queue.

        Time: O(1)
        Space: O(1)
        """
        self._a = [None] * 8  # Reset to default capacity
        self._head = self._tail = self._size = 0

    def __repr__(self) -> str:
        """Developer-friendly string representation."""
        if self._size == 0:
            return "ArrayQueue([])"

        # Rebuild logical order from head to tail
        data = [self._a[(self._head + i) % len(self._a)] for i in range(self._size)]
        return f"ArrayQueue({data})"


class LinkedQueue:
    """
    Linked list-based queue implementation.

    Maintains separate head (front) and tail (rear) pointers for O(1)
    operations at both ends. Each node points to the next node towards rear.

    Pros:
    - Exact O(1) time complexity (no amortization)
    - No wasted memory (allocates exactly what's needed)
    - No capacity limits
    - Simpler logic (no modular arithmetic)

    Cons:
    - Higher per-element memory overhead (pointer storage)
    - Potentially worse cache locality
    - More complex memory management
    """

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """Initialize linked queue with optional initial values.

        Args:
            iterable: Optional sequence of values to enqueue
        """
        self.head = None  # Points to front of queue
        self.tail = None  # Points to rear of queue
        self._size = 0  # Count for O(1) size queries

        if iterable is not None:
            for x in iterable:
                self.enqueue(x)

    def enqueue(self, x: Any) -> None:
        """Add element to rear of queue.

        Time: O(1) exact
        Space: O(1)

        Args:
            x: Element to add to queue
        """
        node = QNode(x)

        if self.tail:  # Non-empty queue
            self.tail.next = node  # Link old tail to new node
        else:  # Empty queue
            self.head = node  # New node is both head and tail

        self.tail = node  # Update tail to new node
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return front element from queue.

        Time: O(1) exact
        Space: O(1)

        Returns:
            Front element that was removed

        Raises:
            IndexError: If queue is empty
        """
        if not self.head:
            raise IndexError("dequeue from empty queue")

        x = self.head.data
        self.head = self.head.next

        # If we just removed the last element, tail should be None too
        if not self.head:
            self.tail = None

        self._size -= 1
        return x

    def front(self) -> Any:
        """View front element without removing it.

        Time: O(1)
        Space: O(1)

        Returns:
            Front element (without removing)

        Raises:
            IndexError: If queue is empty
        """
        if not self.head:
            raise IndexError("front from empty queue")
        return self.head.data

    def rear(self) -> Any:
        """View rear element without removing it.

        Time: O(1)
        Space: O(1)

        Returns:
            Rear element (without removing)

        Raises:
            IndexError: If queue is empty
        """
        if not self.tail:
            raise IndexError("rear from empty queue")
        return self.tail.data

    def is_empty(self) -> bool:
        """Check if queue has no elements.

        Time: O(1)
        Space: O(1)

        Returns:
            True if queue is empty, False otherwise
        """
        return self._size == 0

    def size(self) -> int:
        """Get number of elements in queue.

        Time: O(1)
        Space: O(1)

        Returns:
            Number of elements currently in queue
        """
        return self._size

    def clear(self) -> None:
        """Remove all elements from queue.

        Time: O(1)
        Space: O(1)
        """
        self.head = self.tail = None  # Drop all references
        self._size = 0

    def __repr__(self) -> str:
        """Debug-friendly string representation showing front->rear order."""
        vals = []
        cur = self.head
        while cur is not None:
            vals.append(cur.data)
            cur = cur.next
        return f"LinkedQueue({vals})"


# ========== Visualization Utilities ==========


def _queue_items(queue):
    """Extract items from queue in FRONT to REAR order as a list.

    Args:
        queue: Either ArrayQueue or LinkedQueue instance

    Returns:
        List of items from front to rear
    """
    # LinkedQueue: traverse from head to tail
    if hasattr(queue, "head"):
        vals, cur = [], queue.head
        while cur is not None:
            vals.append(cur.data)
            cur = cur.next
        return vals

    # ArrayQueue: respect circular order from head to head+size-1
    vals = []
    cap = len(queue._a)
    for i in range(queue._size):
        vals.append(queue._a[(queue._head + i) % cap])
    return vals


def print_queue_vertical(queue):
    """Print queue in vertical format showing FIFO structure.

    Output format:
        FRONT
        │ x │
        │ y │
        │ z │
        REAR

    Args:
        queue: Queue instance to visualize
    """
    items = _queue_items(queue)
    if not items:
        print("Queue is Empty\n")
        return

    print("FRONT")
    for item in items:
        print(f"│ {item} │")
    print("REAR\n")


def show_queue(stage: str, queue):
    """Display queue state with label, visualization, and metadata.

    Args:
        stage: Description label for current operation
        queue: Queue instance to display
    """
    print(stage)
    print_queue_vertical(queue)

    # Guard front()/rear() calls since they raise on empty
    f = queue.front() if not queue.is_empty() else None
    r = queue.rear() if not queue.is_empty() else None
    print(f"(len={queue.size()}, front={f}, rear={r})\n")


# ========== Test Suite ==========


def run_queue_tests():
    """Comprehensive test suite for both queue implementations."""
    print("=== Queue Tests (ArrayQueue) ===")

    # Test ArrayQueue with small capacity to exercise _grow()
    aq = ArrayQueue(capacity=2)
    show_queue("Init ArrayQueue (cap=2)", aq)

    aq.enqueue(10)
    show_queue("After enqueue(10)", aq)

    aq.enqueue(20)
    show_queue("After enqueue(20)", aq)

    aq.enqueue(30)  # This should trigger _grow()
    show_queue("After enqueue(30)  # triggers grow", aq)

    # Test peek operations
    assert aq.front() == 10 and aq.rear() == 30

    # Test dequeue
    dequeued = aq.dequeue()
    print(f"dequeue() -> {dequeued}")
    show_queue("After dequeue()", aq)
    assert aq.front() == 20

    # Test clear
    aq.clear()
    show_queue("After clear()", aq)

    # Test error handling
    try:
        aq.dequeue()
    except IndexError as e:
        print(f"dequeue() on empty -> IndexError: {e}\n")

    print("=== Queue Tests (LinkedQueue) ===")

    # Test LinkedQueue
    lq = LinkedQueue([1, 2, 3])
    show_queue("Init LinkedQueue [1,2,3]", lq)

    lq.enqueue(4)
    show_queue("After enqueue(4)", lq)

    # Test peek operations
    assert lq.front() == 1 and lq.rear() == 4

    # Test dequeue
    dequeued = lq.dequeue()
    print(f"dequeue() -> {dequeued}")
    show_queue("After dequeue()", lq)

    # Test clear
    lq.clear()
    show_queue("After clear()", lq)

    # Test error handling
    try:
        lq.front()
    except IndexError as e:
        print(f"front() on empty -> IndexError: {e}\n")

    print("✅ Queue tests passed!\n")


def demonstrate_queue_applications():
    """Demonstrate real-world applications of queues."""
    print("=== Queue Applications Demo ===\n")

    # 1. Breadth-First Search simulation
    def bfs_simulation():
        """Simulate BFS traversal using a queue."""
        # Simple graph representation: adjacency list
        graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F"],
            "D": [],
            "E": ["F"],
            "F": [],
        }

        print("1. Breadth-First Search Simulation:")
        print("   Graph: A -> [B,C], B -> [D,E], C -> [F], E -> [F]")

        queue = ArrayQueue()
        visited = set()

        # Start BFS from 'A'
        queue.enqueue("A")
        visited.add("A")
        traversal_order = []

        print("   BFS Traversal:")
        while not queue.is_empty():
            node = queue.dequeue()
            traversal_order.append(node)
            print(f"   Visiting: {node}, Queue: {queue}")

            # Add unvisited neighbors to queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)

        print(f"   Final order: {' -> '.join(traversal_order)}")

    bfs_simulation()

    # 2. Task scheduling simulation
    def task_scheduler_simulation():
        """Simulate round-robin task scheduling."""
        print(f"\n2. Round-Robin Task Scheduler:")

        # Tasks with remaining execution time
        tasks = [("Task1", 5), ("Task2", 3), ("Task3", 8), ("Task4", 2)]

        task_queue = LinkedQueue()
        for name, time in tasks:
            task_queue.enqueue((name, time))

        print(f"   Initial tasks: {[f'{name}({time})' for name, time in tasks]}")
        print(f"   Time slice: 2 units")

        completed = []
        time_elapsed = 0

        while not task_queue.is_empty():
            task_name, remaining_time = task_queue.dequeue()

            # Execute for time slice (max 2 units)
            execution_time = min(2, remaining_time)
            time_elapsed += execution_time
            remaining_time -= execution_time

            print(
                f"   Time {time_elapsed}: Executed {task_name} for {execution_time} units"
            )

            if remaining_time > 0:
                # Task not finished, put back in queue
                task_queue.enqueue((task_name, remaining_time))
                print(f"   {task_name} has {remaining_time} units left, re-queued")
            else:
                # Task completed
                completed.append(task_name)
                print(f"   {task_name} completed!")

        print(f"   All tasks completed in order: {completed}")

    task_scheduler_simulation()

    # 3. Buffer/Producer-Consumer simulation
    def buffer_simulation():
        """Simulate producer-consumer buffer."""
        print(f"\n3. Producer-Consumer Buffer Simulation:")

        buffer = ArrayQueue(capacity=3)  # Small buffer
        print(f"   Buffer capacity: 3")

        # Producer adds items
        items_to_produce = ["item1", "item2", "item3", "item4"]
        print(f"   Producer adding: {items_to_produce}")

        for item in items_to_produce:
            try:
                if buffer.size() < 3:  # Check capacity manually for demo
                    buffer.enqueue(item)
                    print(f"   Produced: {item}, Buffer: {buffer}")
                else:
                    print(f"   Buffer full! Cannot produce {item}")
                    break
            except:
                break

        # Consumer processes items
        print(f"   Consumer processing items:")
        while not buffer.is_empty():
            item = buffer.dequeue()
            print(f"   Consumed: {item}, Buffer: {buffer}")

    buffer_simulation()
    print()


if __name__ == "__main__":
    """Run tests and demonstrations when file is executed directly."""
    run_queue_tests()
    demonstrate_queue_applications()
