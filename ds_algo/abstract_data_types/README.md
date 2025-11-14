# Abstract Data Types Module 🎭

> Interface-focused data structures - what matters is what they do, not how they do it.

## Overview

Abstract Data Types (ADTs) define a set of operations and their behavior without specifying implementation details. This module implements the fundamental ADTs that form the building blocks of many algorithms: **Stacks** (LIFO) and **Queues** (FIFO).

## 🎯 Core Concepts

**Abstract Data Type** = Interface + Behavior Specification (not implementation)

- **Stack**: Last In, First Out (LIFO) - think of a stack of plates
- **Queue**: First In, First Out (FIFO) - think of a line of people

Each ADT can be implemented with different underlying data structures, offering various performance characteristics and trade-offs.

## 📁 Module Structure

```
abstract_data_types/
├── __init__.py              # ADT exports and documentation
├── stacks.py               # LIFO implementations
└── queues.py              # FIFO implementations
```

## 📚 Stacks - LIFO Operations

> "The last item added is the first one to be removed"

### Stack Interface

```python
push(item)    # Add item to top
pop()         # Remove and return top item
peek()        # View top item without removing
is_empty()    # Check if stack has no items
size()        # Get number of items
clear()       # Remove all items
```

### Two Implementations

#### ArrayStack (Dynamic Array)

```python
from ds_algo.abstract_data_types import ArrayStack

stack = ArrayStack([1, 2, 3])  # Initialize with items
stack.push(4)                  # [1, 2, 3, 4] (4 on top)
print(stack.pop())             # 4 (removed from top)
print(stack.peek())            # 3 (top item, not removed)
print(stack.size())            # 3
```

**Characteristics:**

- ✅ Memory locality (better cache performance)
- ✅ Lower per-element overhead
- ❌ Amortized O(1) operations (occasional O(n) resizing)
- ❌ May waste memory (capacity > size)

#### LinkedStack (Linked List)

```python
from ds_algo.abstract_data_types import LinkedStack

stack = LinkedStack([10, 20, 30])  # 30 on top
stack.push(40)                     # [10, 20, 30, 40]
print(stack.pop())                 # 40
print(stack)                       # LinkedStack(top-> [30, 20, 10])
```

**Characteristics:**

- ✅ Exact O(1) operations (no amortization)
- ✅ No wasted memory (allocates exactly what's needed)
- ❌ Higher per-element memory overhead (pointer storage)
- ❌ Potentially worse cache locality

### Stack Applications

#### 1. Balanced Parentheses Checker

```python
def is_balanced_parentheses(expression):
    stack = ArrayStack()
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in pairs:           # Opening bracket
            stack.push(char)
        elif char in pairs.values(): # Closing bracket
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False

    return stack.is_empty()

# Test cases
print(is_balanced_parentheses("()"))        # True
print(is_balanced_parentheses("([{}])"))    # True
print(is_balanced_parentheses("([)]"))      # False
```

#### 2. Function Call Stack Simulation

```python
def simulate_function_calls():
    call_stack = ArrayStack()

    print("Calling: main() -> func1() -> func2()")
    call_stack.push("main()")
    call_stack.push("func1()")
    call_stack.push("func2()")

    print("Returning from functions...")
    while not call_stack.is_empty():
        returned = call_stack.pop()
        print(f"Returned from: {returned}")
```

#### 3. Undo Functionality

```python
class TextEditor:
    def __init__(self):
        self.content = ""
        self.undo_stack = ArrayStack()

    def type_text(self, text):
        self.undo_stack.push(self.content)  # Save state
        self.content += text

    def undo(self):
        if not self.undo_stack.is_empty():
            self.content = self.undo_stack.pop()

    def get_text(self):
        return self.content
```

## 🚶 Queues - FIFO Operations

> "The first item added is the first one to be removed"

### Queue Interface

```python
enqueue(item)  # Add item to rear
dequeue()      # Remove and return front item
front()        # View front item without removing
rear()         # View rear item without removing
is_empty()     # Check if queue has no items
size()         # Get number of items
clear()        # Remove all items
```

### Two Implementations

#### ArrayQueue (Circular Buffer)

```python
from ds_algo.abstract_data_types import ArrayQueue

queue = ArrayQueue(capacity=4)
queue.enqueue("first")      # [first, _, _, _]
queue.enqueue("second")     # [first, second, _, _]
print(queue.dequeue())      # "first" → [_, second, _, _]
queue.enqueue("third")      # [_, second, third, _]
```

**Characteristics:**

- ✅ Memory locality and cache efficiency
- ✅ Predictable memory usage patterns
- ❌ Amortized O(1) operations (resizing)
- ❌ More complex circular buffer logic

#### LinkedQueue (Linked List)

```python
from ds_algo.abstract_data_types import LinkedQueue

queue = LinkedQueue([1, 2, 3])  # 1 at front, 3 at rear
queue.enqueue(4)                # [1, 2, 3, 4]
print(queue.dequeue())          # 1 (from front)
print(queue.front())            # 2 (new front)
print(queue.rear())             # 4 (at rear)
```

**Characteristics:**

- ✅ Exact O(1) operations
- ✅ No capacity limits
- ✅ Simple logic (no modular arithmetic)
- ❌ Higher memory overhead per element

### Queue Applications

#### 1. Breadth-First Search (BFS) Simulation

```python
def bfs_traversal(graph, start):
    queue = ArrayQueue()
    visited = set()
    result = []

    queue.enqueue(start)
    visited.add(start)

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)

    return result

# Example graph traversal
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
print(bfs_traversal(graph, 'A'))  # ['A', 'B', 'C', 'D']
```

#### 2. Round-Robin Task Scheduler

```python
def round_robin_scheduler(tasks, time_slice=2):
    task_queue = LinkedQueue()

    # Initialize queue with tasks (name, remaining_time)
    for name, time in tasks:
        task_queue.enqueue((name, time))

    completed = []
    time_elapsed = 0

    while not task_queue.is_empty():
        task_name, remaining_time = task_queue.dequeue()

        # Execute for time slice
        execution_time = min(time_slice, remaining_time)
        time_elapsed += execution_time
        remaining_time -= execution_time

        print(f"Time {time_elapsed}: Executed {task_name}")

        if remaining_time > 0:
            task_queue.enqueue((task_name, remaining_time))  # Re-queue
        else:
            completed.append(task_name)  # Task completed

    return completed
```

#### 3. Producer-Consumer Buffer

```python
class ProducerConsumerBuffer:
    def __init__(self, capacity=5):
        self.buffer = ArrayQueue(capacity)
        self.capacity = capacity

    def produce(self, item):
        if self.buffer.size() < self.capacity:
            self.buffer.enqueue(item)
            return True
        return False  # Buffer full

    def consume(self):
        if not self.buffer.is_empty():
            return self.buffer.dequeue()
        return None  # Buffer empty
```

## ⚡ Performance Comparison

### Time Complexity

| Operation           | ArrayStack | LinkedStack | ArrayQueue | LinkedQueue |
| ------------------- | ---------- | ----------- | ---------- | ----------- |
| **Push/Enqueue**    | O(1)\*     | O(1)        | O(1)\*     | O(1)        |
| **Pop/Dequeue**     | O(1)\*     | O(1)        | O(1)       | O(1)        |
| **Peek/Front/Rear** | O(1)       | O(1)        | O(1)       | O(1)        |
| **Size/IsEmpty**    | O(1)       | O(1)        | O(1)       | O(1)        |
| **Clear**           | O(1)       | O(1)        | O(1)       | O(1)        |

\* Amortized due to occasional resizing

### Space Complexity

| Implementation  | Space per Element | Additional Overhead      |
| --------------- | ----------------- | ------------------------ |
| **ArrayStack**  | Size of data      | ~25% extra capacity      |
| **LinkedStack** | Data + 1 pointer  | Node allocation overhead |
| **ArrayQueue**  | Size of data      | Fixed capacity buffer    |
| **LinkedQueue** | Data + 1 pointer  | Head/tail pointers       |

## 🎯 When to Choose What

### Use ArrayStack/ArrayQueue when:

- ✅ **Memory efficiency** is important
- ✅ **Cache performance** matters
- ✅ **Predictable memory usage** needed
- ✅ Working with **numerical data**

### Use LinkedStack/LinkedQueue when:

- ✅ **Exact memory usage** required
- ✅ **No capacity limits** needed
- ✅ **Consistent O(1)** operations required
- ✅ **Frequent size changes**

### Real-world Guidelines

```python
# Choose based on your use case
def choose_implementation(use_case):
    if use_case == "web_browser_history":
        return "ArrayStack (bounded history)"
    elif use_case == "function_call_stack":
        return "LinkedStack (unknown depth)"
    elif use_case == "printer_queue":
        return "ArrayQueue (bounded buffer)"
    elif use_case == "bfs_exploration":
        return "LinkedQueue (unknown size)"
```

## 🧪 Testing and Visualization

### Comprehensive Testing

```python
from ds_algo.abstract_data_types.stacks import run_stack_tests
from ds_algo.abstract_data_types.queues import run_queue_tests

# Test all implementations
run_stack_tests()    # Tests both ArrayStack and LinkedStack
run_queue_tests()    # Tests both ArrayQueue and LinkedQueue
```

### Visual Representations

```python
# Stack visualization
stack = ArrayStack([10, 20, 30])
print_stack_vertical(stack)
# Output:
# TOP
# │ 30 │
# │ 20 │
# │ 10 │
# BOTTOM

# Queue visualization
queue = LinkedQueue(['A', 'B', 'C'])
print_queue_vertical(queue)
# Output:
# FRONT
# │ A │
# │ B │
# │ C │
# REAR
```

## 🔍 Advanced Concepts

### Stack Memory vs Heap Memory

```python
def understand_memory_types():
    # Stack memory: function calls, local variables
    # - Fast allocation/deallocation
    # - Limited size
    # - Automatic cleanup

    # Heap memory: dynamic allocation
    # - Flexible size
    # - Manual management (Python has GC)
    # - Slower allocation

    # Our Stack ADT uses heap memory to store data
    # But simulates stack-like behavior
```

### Double-Ended Queue (Deque) Preview

```python
# Future extension: deque combines stack and queue
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)    # Add to front (like stack push)
d.append(4)        # Add to rear (like queue enqueue)
d.popleft()        # Remove from front (like queue dequeue)
d.pop()            # Remove from rear (like stack pop)
```

### Stack Overflow and Queue Overflow

```python
def handle_overflow_conditions():
    # Stack overflow: too many function calls
    # def recursive_function(n):
    #     return recursive_function(n+1)  # Will cause stack overflow

    # Queue overflow: producer faster than consumer
    buffer = ArrayQueue(capacity=10)
    # If enqueue rate > dequeue rate, buffer fills up
```

## 📊 Real-World Performance

### Benchmark Results (Example)

```
Operation: 100,000 pushes/pops
ArrayStack:   45ms (amortized resizing)
LinkedStack:  62ms (allocation overhead)

Operation: 100,000 enqueues/dequeues
ArrayQueue:   38ms (circular buffer efficiency)
LinkedQueue:  71ms (pointer manipulation)

Memory Usage (1,000 integers):
ArrayStack:   ~32KB (compact storage)
LinkedStack:  ~48KB (pointer overhead)
```

## 🚀 Performance Tips

### Optimization Strategies

1. **Pre-size when possible**

```python
# If you know approximate size
stack = ArrayStack()
stack._a.reserve(expected_size)  # Avoid early resizing
```

2. **Choose based on access patterns**

```python
# Frequent size checking → use implementation with O(1) size
# Memory-constrained → use array-based
# Unknown maximum size → use linked-based
```

3. **Batch operations when applicable**

```python
# Instead of many individual pushes
items = [1, 2, 3, 4, 5]
stack = ArrayStack(items)  # More efficient initialization
```

## 📚 Study Exercises

### Exercise 1: Implement Calculator

```python
def evaluate_postfix(expression):
    """Evaluate postfix expression using stack."""
    stack = ArrayStack()

    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(a, b, token)
            stack.push(result)

    return stack.pop()

# Test: "3 4 + 2 *" = (3 + 4) * 2 = 14
print(evaluate_postfix("3 4 + 2 *"))  # 14
```

### Exercise 2: Implement Undo/Redo

```python
class UndoRedoSystem:
    def __init__(self):
        self.undo_stack = ArrayStack()
        self.redo_stack = ArrayStack()
        self.current_state = ""

    def execute_command(self, command):
        self.undo_stack.push(self.current_state)
        self.current_state = command(self.current_state)
        self.redo_stack.clear()  # Clear redo on new command

    def undo(self):
        if not self.undo_stack.is_empty():
            self.redo_stack.push(self.current_state)
            self.current_state = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack.is_empty():
            self.undo_stack.push(self.current_state)
            self.current_state = self.redo_stack.pop()
```

### Exercise 3: Multi-Queue System

```python
class PriorityQueueSystem:
    def __init__(self):
        self.high_priority = LinkedQueue()
        self.normal_priority = LinkedQueue()
        self.low_priority = LinkedQueue()

    def enqueue(self, item, priority='normal'):
        if priority == 'high':
            self.high_priority.enqueue(item)
        elif priority == 'low':
            self.low_priority.enqueue(item)
        else:
            self.normal_priority.enqueue(item)

    def dequeue(self):
        # Always serve high priority first
        if not self.high_priority.is_empty():
            return self.high_priority.dequeue()
        elif not self.normal_priority.is_empty():
            return self.normal_priority.dequeue()
        elif not self.low_priority.is_empty():
            return self.low_priority.dequeue()
        return None
```

---

## 🎯 Next Steps

After mastering ADTs:

- **Specialized Queues**: Priority queues, circular queues
- **Advanced Stacks**: Min/max stacks with O(1) queries
- **Deques**: Double-ended queues for more flexibility
- **Trees**: Build upon stack concepts for tree traversals

ADTs teach you to think about interfaces before implementation - a crucial programming skill! 🎭
