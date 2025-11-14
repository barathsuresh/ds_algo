# Non-Linear Structures Module 🌳

> Hierarchical data organization - beyond sequential arrangements.

## Overview

Non-linear data structures organize elements in hierarchical relationships where each element can have multiple predecessors and successors. This module focuses on **Trees** - the foundation for many advanced algorithms and data structures.

## 🎯 Core Concepts

**Non-Linear** = Elements are not arranged in a sequential manner

- Elements can have **multiple children**
- **Hierarchical relationships** (parent-child)
- **No direct successor/predecessor** like in linear structures
- Enable **efficient searching, sorting, and hierarchical modeling**

## 📁 Module Structure

```
non_linear_structures/
├── __init__.py              # Module exports and documentation
└── trees.py                # Tree implementations and algorithms
```

## 🌳 Trees - Hierarchical Organization

> "A tree is a connected acyclic graph where each node has exactly one parent (except the root)"

### Tree Terminology

```
       Root (A)
      /    |    \
   B(child)  C    D
   /   \          |
  E     F         G(leaf)
       /|\
      H I J(leaves)
```

- **Root**: Top node with no parent (A)
- **Parent**: Node with children (A, B, C, D, F)
- **Child**: Node with a parent (B, C, D, E, F, G, H, I, J)
- **Leaf**: Node with no children (E, G, H, I, J)
- **Sibling**: Nodes with same parent (B, C, D are siblings)
- **Height**: Longest path from node to leaf
- **Depth**: Distance from root to node
- **Level**: Nodes at same depth

## 📋 Tree Types

### 1. General Tree (`TreeNode`)

- **Any number of children** per node
- **Flexible structure** for hierarchical data

```python
from ds_algo.non_linear_structures import TreeNode

# Create organization chart
ceo = TreeNode("CEO")
cto = TreeNode("CTO")
cfo = TreeNode("CFO")

ceo.add_child(cto)
ceo.add_child(cfo)

cto.add_child(TreeNode("Engineering Manager"))
cto.add_child(TreeNode("Product Manager"))

print(ceo)  # Visual tree structure
```

**Applications:**

- File system directories
- Organization charts
- HTML DOM structure
- Decision trees
- Game trees

### 2. Binary Tree (`BinaryTreeNode`)

- **At most 2 children** per node (left and right)
- **Foundation for many algorithms**

```python
from ds_algo.non_linear_structures import BinaryTreeNode

# Create expression tree for: (3 + 4) * 2
multiply = BinaryTreeNode("*")
plus = BinaryTreeNode("+")
num2 = BinaryTreeNode(2)

multiply.left = plus
multiply.right = num2
plus.left = BinaryTreeNode(3)
plus.right = BinaryTreeNode(4)

# Different traversals give different expressions
print("Infix:", multiply.inorder_traversal())    # [3, '+', 4, '*', 2]
print("Prefix:", multiply.preorder_traversal())  # ['*', '+', 3, 4, 2]
print("Postfix:", multiply.postorder_traversal()) # [3, 4, '+', 2, '*']
```

**Applications:**

- Expression parsing
- Huffman coding
- Binary heaps
- Decision trees

### 3. Binary Search Tree (`BSTNode`)

- **Binary tree with ordering property**
- **Left subtree < Node < Right subtree**

```python
from ds_algo.non_linear_structures import BSTNode

# Create and populate BST
bst = BSTNode(50)
values = [30, 70, 20, 40, 60, 80]

for val in values:
    bst.insert(val)

print("Sorted order:", bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]
print("Search 40:", bst.search(40))              # "Found 40"
print("Search 25:", bst.search(25))              # "Not Found"
```

**Applications:**

- Database indexing
- Priority queues
- Expression evaluation
- File compression

## ⚡ Tree Operations & Complexity

### Time Complexity Summary

| Operation     | General Tree | Binary Tree | BST (Balanced) | BST (Skewed) |
| ------------- | ------------ | ----------- | -------------- | ------------ |
| **Search**    | O(n)         | O(n)        | O(log n)       | O(n)         |
| **Insert**    | O(1)\*       | O(n)        | O(log n)       | O(n)         |
| **Delete**    | O(n)         | O(n)        | O(log n)       | O(n)         |
| **Traversal** | O(n)         | O(n)        | O(n)           | O(n)         |
| **Height**    | O(n)         | O(n)        | O(n)           | O(n)         |

\* O(1) for general tree assumes direct parent reference

### Space Complexity

- **Storage**: O(n) for n nodes
- **Traversal**: O(h) where h is height (recursion stack)
- **Balanced tree**: h = O(log n)
- **Skewed tree**: h = O(n)

## 🚀 Tree Traversal Algorithms

### Depth-First Search (DFS)

#### 1. Preorder: Root → Left → Right

```python
def preorder_traversal(root):
    if root is None:
        return []

    result = [root.data]
    if hasattr(root, 'left') and root.left:
        result.extend(preorder_traversal(root.left))
    if hasattr(root, 'right') and root.right:
        result.extend(preorder_traversal(root.right))

    return result

# Use case: Copy tree, prefix expressions
```

#### 2. Inorder: Left → Root → Right

```python
def inorder_traversal(root):
    result = []
    if hasattr(root, 'left') and root.left:
        result.extend(inorder_traversal(root.left))

    result.append(root.data)

    if hasattr(root, 'right') and root.right:
        result.extend(inorder_traversal(root.right))

    return result

# Use case: BST sorted output, infix expressions
```

#### 3. Postorder: Left → Right → Root

```python
def postorder_traversal(root):
    result = []
    if hasattr(root, 'left') and root.left:
        result.extend(postorder_traversal(root.left))
    if hasattr(root, 'right') and root.right:
        result.extend(postorder_traversal(root.right))

    result.append(root.data)
    return result

# Use case: Delete tree, postfix expressions, calculate directory sizes
```

### Breadth-First Search (BFS)

#### Level-Order Traversal

```python
from collections import deque

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        # Add children to queue
        if hasattr(node, 'children'):  # General tree
            queue.extend(node.children)
        else:  # Binary tree
            if hasattr(node, 'left') and node.left:
                queue.append(node.left)
            if hasattr(node, 'right') and node.right:
                queue.append(node.right)

    return result

# Use case: Level-by-level processing, shortest path in unweighted trees
```

## 🎯 Tree Applications

### 1. File System Navigation

```python
def create_file_system():
    root = TreeNode("/")
    home = TreeNode("home")
    usr = TreeNode("usr")
    var = TreeNode("var")

    root.add_child(home)
    root.add_child(usr)
    root.add_child(var)

    user_dir = TreeNode("user")
    home.add_child(user_dir)
    user_dir.add_child(TreeNode("documents"))
    user_dir.add_child(TreeNode("downloads"))

    return root

def find_file(root, filename):
    """Find file in directory tree."""
    if root.data == filename:
        return root

    for child in root.children:
        result = find_file(child, filename)
        if result:
            return result

    return None
```

### 2. Expression Evaluation

```python
def evaluate_expression_tree(root):
    """Evaluate mathematical expression tree."""
    if root.is_leaf():
        return float(root.data)  # Number

    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)
    operator = root.data

    if operator == '+':
        return left_val + right_val
    elif operator == '-':
        return left_val - right_val
    elif operator == '*':
        return left_val * right_val
    elif operator == '/':
        return left_val / right_val

    raise ValueError(f"Unknown operator: {operator}")

# Example: ((3 + 4) * 2) = 14
```

### 3. Decision Tree

```python
class DecisionNode:
    def __init__(self, question):
        self.question = question
        self.yes_child = None
        self.no_child = None

    def add_children(self, yes_node, no_node):
        self.yes_child = yes_node
        self.no_child = no_node

def build_animal_classifier():
    """Simple animal classification tree."""
    root = DecisionNode("Does it have fur?")

    has_fur = DecisionNode("Does it bark?")
    no_fur = DecisionNode("Does it swim?")

    root.add_children(has_fur, no_fur)

    # Leaf nodes (classifications)
    dog = TreeNode("Dog")
    cat = TreeNode("Cat")
    fish = TreeNode("Fish")
    bird = TreeNode("Bird")

    has_fur.add_children(dog, cat)
    no_fur.add_children(fish, bird)

    return root
```

### 4. Binary Search Operations

```python
def range_query(bst, min_val, max_val):
    """Find all values in BST within range [min_val, max_val]."""
    result = []

    def inorder_range(node):
        if node is None:
            return

        # Only traverse left if there might be values in range
        if node.data > min_val:
            inorder_range(node.left)

        # Add current node if in range
        if min_val <= node.data <= max_val:
            result.append(node.data)

        # Only traverse right if there might be values in range
        if node.data < max_val:
            inorder_range(node.right)

    inorder_range(bst)
    return result

# Example: Find all values between 25 and 75
# Only visits relevant parts of tree (pruning)
```

## 🔍 Tree Properties & Validation

### Tree Type Identification

```python
def classify_binary_tree(root):
    """Determine binary tree type."""

    def check_full(node):
        """Full: Every node has 0 or 2 children."""
        if node is None:
            return True

        # Leaf node is okay
        if node.left is None and node.right is None:
            return True

        # Both children must exist
        if node.left and node.right:
            return check_full(node.left) and check_full(node.right)

        return False  # Only one child

    def check_complete(node, index, node_count):
        """Complete: All levels filled except possibly last."""
        if node is None:
            return True

        if index >= node_count:
            return False

        return (check_complete(node.left, 2*index + 1, node_count) and
                check_complete(node.right, 2*index + 2, node_count))

    def check_perfect(node):
        """Perfect: All internal nodes have 2 children, leaves at same level."""
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def is_perfect(node, level, leaf_level):
            if node is None:
                return True

            if node.left is None and node.right is None:
                return level == leaf_level

            if node.left is None or node.right is None:
                return False

            return (is_perfect(node.left, level + 1, leaf_level) and
                    is_perfect(node.right, level + 1, leaf_level))

        h = height(root)
        return is_perfect(node, 1, h)

    node_count = count_nodes(root)

    return {
        'full': check_full(root),
        'complete': check_complete(root, 0, node_count),
        'perfect': check_perfect(root)
    }
```

### BST Validation

```python
def validate_bst(root, min_val=None, max_val=None):
    """Verify tree satisfies BST property."""
    if root is None:
        return True

    # Check current node against bounds
    if min_val is not None and root.data <= min_val:
        return False
    if max_val is not None and root.data >= max_val:
        return False

    # Recursively validate subtrees with updated bounds
    return (validate_bst(root.left, min_val, root.data) and
            validate_bst(root.right, root.data, max_val))
```

### Tree Balance Analysis

```python
def analyze_balance(root):
    """Analyze tree balance and suggest improvements."""

    def height(node):
        if node is None:
            return -1
        return 1 + max(height(node.left), height(node.right))

    def balance_factor(node):
        if node is None:
            return 0
        return height(node.left) - height(node.right)

    h = height(root)
    n = count_nodes(root)
    optimal_height = math.ceil(math.log2(n + 1)) - 1

    print(f"Tree Analysis:")
    print(f"  Nodes: {n}")
    print(f"  Actual height: {h}")
    print(f"  Optimal height: {optimal_height}")
    print(f"  Balance efficiency: {optimal_height/h:.2%}")

    # Check if severely unbalanced
    if h > 2 * optimal_height:
        print("  ⚠️  Tree is severely unbalanced!")
        print("  💡 Consider rebalancing or using AVL/Red-Black tree")
```

## 🧪 Testing & Demonstration

### Comprehensive Testing

```python
from ds_algo.non_linear_structures.trees import (
    create_sample_trees,
    print_tree_comparison,
    demonstrate_bst_operations
)

# Create and explore different tree types
create_sample_trees()

# Compare traversal methods
print_tree_comparison()

# Interactive BST operations
demonstrate_bst_operations()
```

### Visual Tree Display

```python
def print_tree_structure(root, prefix="", is_last=True):
    """Print tree with connecting lines."""
    if root is None:
        return

    print(prefix + ("└── " if is_last else "├── ") + str(root.data))

    children = []
    if hasattr(root, 'children'):
        children = root.children
    else:
        if hasattr(root, 'left') and root.left:
            children.append(root.left)
        if hasattr(root, 'right') and root.right:
            children.append(root.right)

    for i, child in enumerate(children):
        is_last_child = i == len(children) - 1
        extension = "    " if is_last else "│   "
        print_tree_structure(child, prefix + extension, is_last_child)
```

## 🎯 Performance Optimization

### BST Optimization Tips

1. **Keep Trees Balanced**

```python
def is_balanced(root):
    """Check if tree height difference ≤ 1 for all nodes."""
    def check_balance(node):
        if node is None:
            return True, -1

        left_balanced, left_height = check_balance(node.left)
        if not left_balanced:
            return False, 0

        right_balanced, right_height = check_balance(node.right)
        if not right_balanced:
            return False, 0

        balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)

        return balanced, height

    balanced, _ = check_balance(root)
    return balanced
```

2. **Insertion Order Matters**

```python
# Bad: sorted input creates skewed tree (O(n) operations)
bad_bst = BSTNode(1)
for i in range(2, 101):
    bad_bst.insert(i)  # Creates linked list!

# Good: randomized or balanced input
import random
values = list(range(1, 101))
random.shuffle(values)

good_bst = BSTNode(values[0])
for val in values[1:]:
    good_bst.insert(val)  # More balanced tree
```

3. **Memory-Efficient Trees**

```python
# Use __slots__ to reduce memory overhead
class OptimizedBSTNode:
    __slots__ = ('data', 'left', 'right')

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

## 📚 Advanced Tree Concepts

### 1. Tree Rotations (AVL Tree Preview)

```python
def rotate_right(root):
    """Right rotation for tree balancing."""
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root

def rotate_left(root):
    """Left rotation for tree balancing."""
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root
```

### 2. Tree Serialization

```python
def serialize_tree(root):
    """Convert tree to string representation."""
    if root is None:
        return "None"

    return f"{root.data},{serialize_tree(root.left)},{serialize_tree(root.right)}"

def deserialize_tree(data):
    """Reconstruct tree from string."""
    def build():
        val = next(vals)
        if val == "None":
            return None

        node = BinaryTreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    vals = iter(data.split(','))
    return build()
```

### 3. Path Finding

```python
def find_path(root, target):
    """Find path from root to target node."""
    if root is None:
        return None

    if root.data == target:
        return [root.data]

    # Try left subtree
    if hasattr(root, 'left') and root.left:
        left_path = find_path(root.left, target)
        if left_path:
            return [root.data] + left_path

    # Try right subtree
    if hasattr(root, 'right') and root.right:
        right_path = find_path(root.right, target)
        if right_path:
            return [root.data] + right_path

    return None  # Target not found
```

---

## 🎯 Next Steps

After mastering basic trees:

- **Self-Balancing Trees**: AVL, Red-Black, B-trees
- **Heap Data Structures**: Priority queues, heap sort
- **Trie (Prefix Tree)**: String searching and autocomplete
- **Segment Trees**: Range queries and updates
- **Graph Theory**: Trees are special cases of graphs

Trees form the foundation for understanding hierarchical algorithms! 🌳
