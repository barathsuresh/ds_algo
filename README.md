# Data Structures and Algorithms Learning Project 📚

> A comprehensive, educational implementation of fundamental data structures and algorithms in Python, designed for learning and reference.

## 🎯 Project Overview

This project transforms a monolithic Jupyter notebook into a well-structured Python package containing implementations of essential data structures and algorithms. Each implementation includes:

- **Detailed documentation** with complexity analysis
- **Educational examples** and use cases
- **Comprehensive test suites** with visual demonstrations
- **Type hints** for better code understanding
- **Performance comparisons** between different approaches

## 📋 Table of Contents

- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Data Structures](#-data-structures)
- [Complexity Analysis](#-complexity-analysis)
- [Examples and Usage](#-examples-and-usage)
- [Testing](#-testing)
- [Learning Resources](#-learning-resources)
- [Contributing](#-contributing)

## 📁 Project Structure

```
ds_algo/
├── __init__.py                     # Main package initialization
├── complexity_analysis/            # Time and space complexity foundations
│   ├── __init__.py
│   ├── time_complexity.py         # Big O analysis and examples
│   ├── space_complexity.py        # Space complexity analysis
│   └── asymptotic_notation.py     # Big O, Omega, Theta notations
├── linear_structures/              # Sequential data organization
│   ├── static/                    # Fixed-size structures
│   │   ├── __init__.py
│   │   ├── arrays.py             # Array operations and analysis
│   │   ├── lists.py              # Python list operations
│   │   ├── dictionaries.py       # Hash table operations
│   │   └── tuples.py             # Immutable sequence operations
│   └── dynamic/                   # Variable-size linked structures
│       ├── __init__.py
│       ├── singly_linked_list.py  # SLL implementation
│       ├── doubly_linked_list.py  # DLL implementation
│       ├── circular_singly_linked_list.py  # CSLL
│       └── circular_doubly_linked_list.py  # CDLL with sentinel
├── abstract_data_types/           # Interface-focused implementations
│   ├── __init__.py
│   ├── stacks.py                 # LIFO implementations (array & linked)
│   └── queues.py                 # FIFO implementations (array & linked)
├── non_linear_structures/         # Hierarchical data organization
│   ├── __init__.py
│   └── trees.py                  # Tree implementations (general, binary, BST)
├── algorithms/                    # Algorithm implementations (future)
│   └── __init__.py
└── utils/                        # Utility functions and helpers
    └── __init__.py
```

## 🚀 Installation

### Prerequisites

- Python 3.7+
- Optional: `matplotlib` and `numpy` for visualization (complexity analysis)

### Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd DS_ALGO

# Install in development mode
pip install -e .

# Optional: Install visualization dependencies
pip install matplotlib numpy
```

### Import and Use

```python
# Import specific data structures
from ds_algo.linear_structures.dynamic import SinglyLinkedList
from ds_algo.abstract_data_types import ArrayStack, LinkedQueue
from ds_algo.non_linear_structures import BSTNode

# Import entire modules
from ds_algo import complexity_analysis
from ds_algo.linear_structures import static, dynamic
```

## 🎯 Quick Start

### Basic Examples

```python
# Stack operations (LIFO)
from ds_algo.abstract_data_types import ArrayStack

stack = ArrayStack([1, 2, 3])
stack.push(4)
print(stack.pop())  # 4
print(stack.peek()) # 3

# Queue operations (FIFO)
from ds_algo.abstract_data_types import LinkedQueue

queue = LinkedQueue()
queue.enqueue("first")
queue.enqueue("second")
print(queue.dequeue())  # "first"

# Binary Search Tree
from ds_algo.non_linear_structures import BSTNode

bst = BSTNode(50)
bst.insert(30)
bst.insert(70)
print(bst.search(30))  # "Found 30"
print(bst.inorder_traversal())  # [30, 50, 70] - sorted!

# Linked List operations
from ds_algo.linear_structures.dynamic import DoublyLinkedList

dll = DoublyLinkedList([1, 2, 3])
dll.append(4)
dll.prepend(0)
print(list(dll))  # [0, 1, 2, 3, 4]
```

## 📊 Data Structures

### Linear Structures

#### Static (Built-in Python Types)

- **Arrays** - Fixed-size collections with O(1) access
- **Lists** - Dynamic arrays with amortized O(1) append
- **Dictionaries** - Hash tables with O(1) average lookup
- **Tuples** - Immutable sequences

#### Dynamic (Linked Implementations)

- **Singly Linked List** - Forward traversal, O(1) prepend
- **Doubly Linked List** - Bidirectional traversal, O(1) operations at both ends
- **Circular Singly Linked List** - No null pointers, circular traversal
- **Circular Doubly Linked List** - Sentinel node, efficient deque operations

### Abstract Data Types

#### Stacks (LIFO - Last In, First Out)

- **ArrayStack** - Dynamic array implementation
- **LinkedStack** - Linked list implementation
- Applications: Function calls, expression evaluation, undo operations

#### Queues (FIFO - First In, First Out)

- **ArrayQueue** - Circular buffer implementation
- **LinkedQueue** - Linked list implementation
- Applications: BFS, task scheduling, producer-consumer

### Non-Linear Structures

#### Trees

- **TreeNode** - General tree with arbitrary children
- **BinaryTreeNode** - Binary tree with left/right children
- **BSTNode** - Binary Search Tree with ordering property
- Applications: File systems, expression parsing, searching

## ⚡ Complexity Analysis

### Time Complexity Examples

| Data Structure | Access   | Search   | Insertion | Deletion |
| -------------- | -------- | -------- | --------- | -------- |
| Array          | O(1)     | O(n)     | O(n)      | O(n)     |
| Linked List    | O(n)     | O(n)     | O(1)\*    | O(1)\*   |
| Stack          | O(1)     | O(n)     | O(1)      | O(1)     |
| Queue          | O(1)     | O(n)     | O(1)      | O(1)     |
| BST (balanced) | O(log n) | O(log n) | O(log n)  | O(log n) |
| BST (skewed)   | O(n)     | O(n)     | O(n)      | O(n)     |

\*At head/tail when reference available

### Space Complexity

- **Arrays**: O(n) - contiguous memory
- **Linked Lists**: O(n) - additional pointer overhead
- **Trees**: O(n) - nodes + pointers, O(h) recursion depth

## 📚 Examples and Usage

### Comprehensive Demonstrations

Each module includes detailed examples:

```python
# Run built-in demonstrations
from ds_algo.complexity_analysis.time_complexity import demonstrate_time_complexities
from ds_algo.abstract_data_types.stacks import demonstrate_stack_applications
from ds_algo.non_linear_structures.trees import demonstrate_bst_operations

demonstrate_time_complexities()    # Visualize performance patterns
demonstrate_stack_applications()   # Real-world stack usage
demonstrate_bst_operations()       # Tree manipulation
```

### Educational Features

- **Visual Representations**: ASCII art for data structure states
- **Step-by-step Tracing**: Watch operations modify structures
- **Performance Comparison**: Side-by-side algorithm analysis
- **Real-world Applications**: Practical usage examples

## 🧪 Testing

Each module includes comprehensive test suites:

```python
# Run individual module tests
from ds_algo.abstract_data_types.stacks import run_stack_tests
from ds_algo.linear_structures.dynamic.doubly_linked_list import run_dll_tests

run_stack_tests()  # Test both ArrayStack and LinkedStack
run_dll_tests()    # Test DoublyLinkedList operations

# Or run tests directly
python -m ds_algo.abstract_data_types.stacks
python -m ds_algo.non_linear_structures.trees
```

### Test Coverage

- ✅ **Functional Testing**: All operations work correctly
- ✅ **Edge Case Testing**: Empty structures, single elements
- ✅ **Error Handling**: Proper exceptions for invalid operations
- ✅ **Performance Verification**: Complexity assertions
- ✅ **Integration Testing**: Multiple operations in sequence

## 📖 Learning Resources

### Understanding Complexity

```python
from ds_algo.complexity_analysis import time_complexity

# Learn about different complexity classes
time_complexity.demonstrate_constant_time()     # O(1)
time_complexity.demonstrate_linear_time()       # O(n)
time_complexity.demonstrate_logarithmic_time()  # O(log n)
time_complexity.demonstrate_quadratic_time()    # O(n²)
```

### Algorithm Patterns

- **Divide and Conquer**: Tree traversals, binary search
- **Two Pointers**: Linked list operations
- **Stack-based**: Expression evaluation, balanced parentheses
- **Queue-based**: Level-order traversal, BFS

### Best Practices

1. **Choose appropriate data structure** for your use case
2. **Understand amortized vs worst-case** complexity
3. **Consider space-time tradeoffs**
4. **Use built-in Python collections** when possible
5. **Implement custom structures** only when needed

## 📈 Performance Tips

### When to Use What

#### Use Arrays/Lists when:

- Random access needed
- Iterating through all elements
- Memory efficiency important

#### Use Linked Lists when:

- Frequent insertions/deletions at known positions
- Size varies dramatically
- Don't need random access

#### Use Stacks when:

- LIFO order required
- Recursive algorithm conversion
- Undo/redo functionality

#### Use Queues when:

- FIFO order required
- Producer-consumer scenarios
- Breadth-first processing

#### Use BST when:

- Sorted data maintenance
- Range queries needed
- Logarithmic search required

## 🤝 Contributing

This is an educational project! Contributions are welcome:

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/new-algorithm`
3. **Add your implementation** with documentation and tests
4. **Follow the existing patterns**: type hints, complexity analysis, examples
5. **Submit pull request**

### Contribution Guidelines

- Include comprehensive docstrings
- Add time/space complexity analysis
- Provide usage examples
- Write test cases
- Follow Python conventions (PEP 8)

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and learn from the code.

## 🔗 Related Resources

- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Algorithm Visualizations](https://visualgo.net/)
- [Interactive Data Structures](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

---

## 🎓 Learning Journey

This project represents a transformation from a single notebook to a structured learning resource. Each implementation balances:

- **Educational Value**: Clear explanations and examples
- **Production Quality**: Proper error handling and edge cases
- **Performance Awareness**: Complexity analysis and optimization
- **Practical Application**: Real-world usage patterns

Start with the complexity analysis modules to build foundational understanding, then explore data structures that interest you most!

**Happy Learning! 🚀**
