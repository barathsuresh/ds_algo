"""
Tree Data Structures - Hierarchical Non-Linear Data Types

Trees are hierarchical data structures consisting of nodes connected by edges.
Each tree has a root node, and every other node has exactly one parent and
zero or more children. Trees model hierarchical relationships efficiently.

This module provides implementations for:
1. TreeNode: General tree with arbitrary number of children
2. BinaryTreeNode: Binary tree with left and right children only
3. BSTNode: Binary Search Tree with ordering properties

Tree Terminology:
- Root: Top node with no parent
- Leaf: Node with no children
- Parent: Node with children
- Sibling: Nodes with same parent
- Height: Longest path from node to leaf
- Depth: Distance from root to node
- Level: Nodes at same depth

Tree Types:
- Full Binary Tree: Every node has 0 or 2 children
- Complete Binary Tree: All levels filled except possibly last (filled left-right)
- Perfect Binary Tree: All internal nodes have 2 children, all leaves same level
- Balanced Binary Tree: Height difference ≤ 1 for all nodes

Time Complexities:
┌─────────────────┬──────────┬──────────┬──────────┬─────────────────────┐
│ Operation       │ Tree     │ Binary   │ BST Avg  │ BST Worst           │
├─────────────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ Search          │ O(n)     │ O(n)     │ O(log n) │ O(n) skewed         │
│ Insert          │ O(1)*    │ O(n)     │ O(log n) │ O(n) skewed         │
│ Delete          │ O(n)     │ O(n)     │ O(log n) │ O(n) skewed         │
│ Traversal       │ O(n)     │ O(n)     │ O(n)     │ O(n)                │
└─────────────────┴──────────┴──────────┴──────────┴─────────────────────┘

*O(1) for general tree assumes you have direct reference to parent
"""

from typing import Any, Optional, List, Union
from collections import deque


class TreeNode:
    """
    General tree node that can have any number of children.

    Suitable for modeling hierarchical data like:
    - File system directories
    - Organization charts
    - HTML DOM elements
    - Decision trees
    """

    def __init__(self, data: Any, children: Optional[List["TreeNode"]] = None) -> None:
        """Initialize a tree node.

        Args:
            data: The value stored in this node
            children: List of child nodes (empty list if None)
        """
        self.data = data
        self.children = children if children is not None else []

    def add_child(self, child_node: "TreeNode") -> None:
        """Add a child node.

        Time: O(1)
        Space: O(1)

        Args:
            child_node: TreeNode to add as child
        """
        self.children.append(child_node)

    def is_leaf(self) -> bool:
        """Check if node is a leaf (has no children).

        Returns:
            True if node has no children
        """
        return len(self.children) == 0

    def get_height(self) -> int:
        """Calculate height of subtree rooted at this node.

        Height is defined as the longest path from this node to any leaf.
        A leaf node has height 0.

        Time: O(n) where n is number of nodes in subtree
        Space: O(h) where h is height (recursion stack)

        Returns:
            Height of subtree
        """
        if self.is_leaf():
            return 0
        return 1 + max(child.get_height() for child in self.children)

    def count_nodes(self) -> int:
        """Count total number of nodes in subtree.

        Time: O(n)
        Space: O(h) recursion depth

        Returns:
            Number of nodes in subtree rooted at this node
        """
        count = 1  # Count this node
        for child in self.children:
            count += child.count_nodes()
        return count

    def find(self, target: Any) -> Optional["TreeNode"]:
        """Search for a node with given value using DFS.

        Time: O(n)
        Space: O(h) recursion depth

        Args:
            target: Value to search for

        Returns:
            TreeNode with target value, or None if not found
        """
        if self.data == target:
            return self

        for child in self.children:
            result = child.find(target)
            if result is not None:
                return result

        return None

    def traverse_preorder(self) -> List[Any]:
        """Traverse tree in preorder (root, children).

        Time: O(n)
        Space: O(n) for result list + O(h) for recursion

        Returns:
            List of node values in preorder
        """
        result = [self.data]
        for child in self.children:
            result.extend(child.traverse_preorder())
        return result

    def traverse_postorder(self) -> List[Any]:
        """Traverse tree in postorder (children, root).

        Time: O(n)
        Space: O(n) for result list + O(h) for recursion

        Returns:
            List of node values in postorder
        """
        result = []
        for child in self.children:
            result.extend(child.traverse_postorder())
        result.append(self.data)
        return result

    def traverse_level_order(self) -> List[Any]:
        """Traverse tree level by level using BFS.

        Time: O(n)
        Space: O(w) where w is maximum width of tree

        Returns:
            List of node values in level order
        """
        result = []
        queue = deque([self])

        while queue:
            node = queue.popleft()
            result.append(node.data)
            queue.extend(node.children)

        return result

    def __str__(self, level: int = 0) -> str:
        """Create a visual string representation of the tree.

        Args:
            level: Current indentation level

        Returns:
            Multi-line string showing tree structure
        """
        ret = "  " * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"TreeNode({self.data}, {len(self.children)} children)"


class BinaryTreeNode:
    """
    Binary tree node with at most two children (left and right).

    Binary trees are fundamental for many algorithms:
    - Expression trees
    - Decision trees
    - Huffman coding trees
    - Binary heaps
    """

    def __init__(self, data: Any) -> None:
        """Initialize a binary tree node.

        Args:
            data: The value stored in this node
        """
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self) -> bool:
        """Check if node is a leaf."""
        return self.left is None and self.right is None

    def get_height(self) -> int:
        """Calculate height of subtree.

        Time: O(n)
        Space: O(h) recursion depth

        Returns:
            Height of subtree rooted at this node
        """
        if self.is_leaf():
            return 0

        left_height = self.left.get_height() if self.left else -1
        right_height = self.right.get_height() if self.right else -1

        return 1 + max(left_height, right_height)

    def count_nodes(self) -> int:
        """Count nodes in subtree.

        Returns:
            Total number of nodes in subtree
        """
        count = 1
        if self.left:
            count += self.left.count_nodes()
        if self.right:
            count += self.right.count_nodes()
        return count

    def search(self, target: Any) -> bool:
        """Search for value in tree using DFS.

        Time: O(n)
        Space: O(h) recursion depth

        Args:
            target: Value to find

        Returns:
            True if found, False otherwise
        """
        if self.data == target:
            return True

        left_found = self.left.search(target) if self.left else False
        right_found = self.right.search(target) if self.right else False

        return left_found or right_found

    def insert_level_order(self, value: Any) -> None:
        """Insert value at first available position (level-order).

        Time: O(n) worst case
        Space: O(w) where w is width of tree

        Args:
            value: Value to insert
        """
        queue = deque([self])

        while queue:
            current = queue.popleft()

            if not current.left:
                current.left = BinaryTreeNode(value)
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = BinaryTreeNode(value)
                return
            else:
                queue.append(current.right)

    def preorder_traversal(self) -> List[Any]:
        """Preorder traversal: Root -> Left -> Right.

        Returns:
            List of values in preorder
        """
        result = [self.data]
        if self.left:
            result.extend(self.left.preorder_traversal())
        if self.right:
            result.extend(self.right.preorder_traversal())
        return result

    def inorder_traversal(self) -> List[Any]:
        """Inorder traversal: Left -> Root -> Right.

        For BST, this gives sorted order.

        Returns:
            List of values in inorder
        """
        result = []
        if self.left:
            result.extend(self.left.inorder_traversal())
        result.append(self.data)
        if self.right:
            result.extend(self.right.inorder_traversal())
        return result

    def postorder_traversal(self) -> List[Any]:
        """Postorder traversal: Left -> Right -> Root.

        Returns:
            List of values in postorder
        """
        result = []
        if self.left:
            result.extend(self.left.postorder_traversal())
        if self.right:
            result.extend(self.right.postorder_traversal())
        result.append(self.data)
        return result

    def level_order_traversal(self) -> List[Any]:
        """Level-order traversal using BFS.

        Returns:
            List of values in level order
        """
        result = []
        queue = deque([self])

        while queue:
            current = queue.popleft()
            result.append(current.data)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def __str__(self, level: int = 0) -> str:
        """Visual representation of binary tree."""
        ret = "  " * level + repr(self.data) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret

    def __repr__(self) -> str:
        return f"BinaryTreeNode({self.data})"


class BSTNode:
    """
    Binary Search Tree node with ordering property.

    BST Property: For any node:
    - All values in left subtree < node's value
    - All values in right subtree > node's value

    This property enables efficient O(log n) search, insert, and delete
    operations in balanced trees.
    """

    def __init__(self, data: Any) -> None:
        """Initialize a BST node.

        Args:
            data: The value stored in this node (must be comparable)
        """
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value: Any) -> str:
        """Insert value maintaining BST property.

        Time: O(log n) average, O(n) worst case (skewed tree)
        Space: O(log n) average (recursion depth)

        Args:
            value: Value to insert

        Returns:
            Confirmation message
        """
        if self.data is None:
            self.data = value
            return f"Inserted {value}"

        if value < self.data:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)
        else:  # value >= self.data
            if self.right is None:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)

        return f"Inserted {value}"

    def search(self, value: Any) -> str:
        """Search for value in BST.

        Time: O(log n) average, O(n) worst case
        Space: O(log n) recursion depth

        Args:
            value: Value to find

        Returns:
            Success or failure message
        """
        if self.data == value:
            return f"Found {value}"
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return "Not Found"
        else:
            if self.right:
                return self.right.search(value)
            else:
                return "Not Found"

    def find_min(self) -> "BSTNode":
        """Find node with minimum value (leftmost node).

        Returns:
            Node with minimum value
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find_max(self) -> "BSTNode":
        """Find node with maximum value (rightmost node).

        Returns:
            Node with maximum value
        """
        current = self
        while current.right is not None:
            current = current.right
        return current

    def delete(self, value: Any) -> Optional["BSTNode"]:
        """Delete value from BST maintaining BST property.

        Three cases:
        1. Node has no children: Simply remove
        2. Node has one child: Replace with child
        3. Node has two children: Replace with inorder successor

        Time: O(log n) average, O(n) worst case
        Space: O(log n) recursion depth

        Args:
            value: Value to delete

        Returns:
            Root of modified subtree
        """
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:  # Found node to delete
            # Case 1: No left child
            if self.left is None:
                return self.right
            # Case 2: No right child
            elif self.right is None:
                return self.left
            # Case 3: Two children - replace with inorder successor
            else:
                # Find smallest in right subtree
                temp = self.right.find_min()
                # Replace current data with successor's data
                self.data = temp.data
                # Delete the successor
                self.right = self.right.delete(temp.data)

        return self

    def preorder_traversal(self) -> List[Any]:
        """Preorder traversal: Root -> Left -> Right."""
        result = [self.data]
        if self.left:
            result.extend(self.left.preorder_traversal())
        if self.right:
            result.extend(self.right.preorder_traversal())
        return result

    def inorder_traversal(self) -> List[Any]:
        """Inorder traversal: Left -> Root -> Right.

        For BST, this returns values in sorted order.
        """
        result = []
        if self.left:
            result.extend(self.left.inorder_traversal())
        result.append(self.data)
        if self.right:
            result.extend(self.right.inorder_traversal())
        return result

    def postorder_traversal(self) -> List[Any]:
        """Postorder traversal: Left -> Right -> Root."""
        result = []
        if self.left:
            result.extend(self.left.postorder_traversal())
        if self.right:
            result.extend(self.right.postorder_traversal())
        result.append(self.data)
        return result

    def level_order_traversal(self) -> List[Any]:
        """Level-order traversal using BFS."""
        result = []
        queue = deque([self])

        while queue:
            current = queue.popleft()
            result.append(current.data)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def validate_bst(self, min_val: Any = None, max_val: Any = None) -> bool:
        """Validate that tree maintains BST property.

        Args:
            min_val: Minimum allowed value for this subtree
            max_val: Maximum allowed value for this subtree

        Returns:
            True if valid BST, False otherwise
        """
        # Check current node against bounds
        if min_val is not None and self.data <= min_val:
            return False
        if max_val is not None and self.data >= max_val:
            return False

        # Recursively validate subtrees with updated bounds
        left_valid = True
        if self.left:
            left_valid = self.left.validate_bst(min_val, self.data)

        right_valid = True
        if self.right:
            right_valid = self.right.validate_bst(self.data, max_val)

        return left_valid and right_valid

    def get_height(self) -> int:
        """Calculate height of BST."""
        if self.left is None and self.right is None:
            return 0

        left_height = self.left.get_height() if self.left else -1
        right_height = self.right.get_height() if self.right else -1

        return 1 + max(left_height, right_height)

    def is_balanced(self) -> bool:
        """Check if BST is height-balanced.

        A tree is balanced if height difference between left and right
        subtrees is at most 1 for every node.

        Returns:
            True if balanced, False otherwise
        """

        def check_height(node: Optional["BSTNode"]) -> int:
            """Return height if balanced, -1 if unbalanced."""
            if node is None:
                return 0

            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return check_height(self) != -1

    def __repr__(self) -> str:
        return f"BSTNode({self.data})"


# ========== Utility Functions ==========


def print_tree_comparison():
    """Demonstrate different tree traversals and their outputs."""
    print("=== Tree Traversal Comparison ===\n")

    # Create a sample BST
    bst = BSTNode(50)
    values = [30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)

    print("BST with values: 50, 30, 70, 20, 40, 60, 80")
    print("Tree structure:")
    print("       50")
    print("      /  \\")
    print("     30   70")
    print("    / \\  / \\")
    print("   20 40 60 80")
    print()

    print(f"Preorder (Root->Left->Right): {bst.preorder_traversal()}")
    print(f"Inorder (Left->Root->Right):  {bst.inorder_traversal()}")  # Sorted!
    print(f"Postorder (Left->Right->Root): {bst.postorder_traversal()}")
    print(f"Level-order (BFS):           {bst.level_order_traversal()}")
    print()


def demonstrate_bst_operations():
    """Demonstrate BST search, insert, delete operations."""
    print("=== BST Operations Demo ===\n")

    # Create BST and insert values
    bst = BSTNode(40)
    values = [20, 60, 10, 30, 50, 70, 15, 5]

    print("Inserting values: 40, 20, 60, 10, 30, 50, 70, 15, 5")
    for val in values:
        result = bst.insert(val)
        print(f"  {result}")

    print(f"\nInorder traversal (sorted): {bst.inorder_traversal()}")
    print(f"Tree height: {bst.get_height()}")
    print(f"Is balanced: {bst.is_balanced()}")
    print(f"Is valid BST: {bst.validate_bst()}")

    # Search operations
    print("\nSearch operations:")
    search_values = [40, 25, 70, 100]
    for val in search_values:
        result = bst.search(val)
        print(f"  Search {val}: {result}")

    # Delete operations
    print("\nDelete operations:")
    delete_values = [5, 10, 20]  # Leaf, one child, two children
    for val in delete_values:
        print(f"  Deleting {val}...")
        bst = bst.delete(val)
        print(f"  Inorder after deletion: {bst.inorder_traversal()}")

    print()


def create_sample_trees():
    """Create example trees for testing and demonstration."""
    print("=== Sample Tree Creation ===\n")

    # 1. General tree (organization chart)
    print("1. Organization Chart (General Tree):")
    ceo = TreeNode("CEO")
    cto = TreeNode("CTO")
    cfo = TreeNode("CFO")
    vp_eng = TreeNode("VP Engineering")
    vp_product = TreeNode("VP Product")

    ceo.add_child(cto)
    ceo.add_child(cfo)
    cto.add_child(vp_eng)
    cto.add_child(vp_product)

    vp_eng.add_child(TreeNode("Senior Engineer"))
    vp_eng.add_child(TreeNode("Junior Engineer"))
    vp_product.add_child(TreeNode("Product Manager"))

    print(ceo)
    print(f"Total employees: {ceo.count_nodes()}")
    print(f"Organization depth: {ceo.get_height()}")

    # 2. File system (general tree)
    print("2. File System (General Tree):")
    root_dir = TreeNode("/")
    home = TreeNode("home")
    usr = TreeNode("usr")
    var = TreeNode("var")

    root_dir.add_child(home)
    root_dir.add_child(usr)
    root_dir.add_child(var)

    user_dir = TreeNode("user")
    home.add_child(user_dir)
    user_dir.add_child(TreeNode("documents"))
    user_dir.add_child(TreeNode("downloads"))
    user_dir.add_child(TreeNode("pictures"))

    print(root_dir)

    # 3. Expression tree (binary tree)
    print("3. Expression Tree: (3 + 4) * 2")
    # Represents: (3 + 4) * 2
    multiply = BinaryTreeNode("*")
    plus = BinaryTreeNode("+")
    num2 = BinaryTreeNode(2)
    num3 = BinaryTreeNode(3)
    num4 = BinaryTreeNode(4)

    multiply.left = plus
    multiply.right = num2
    plus.left = num3
    plus.right = num4

    print(multiply)
    print(f"Inorder: {multiply.inorder_traversal()}")  # 3 + 4 * 2 (infix)
    print(f"Preorder: {multiply.preorder_traversal()}")  # * + 3 4 2 (prefix)
    print(f"Postorder: {multiply.postorder_traversal()}")  # 3 4 + 2 * (postfix)
    print()


if __name__ == "__main__":
    """Run demonstrations when file is executed directly."""
    create_sample_trees()
    print_tree_comparison()
    demonstrate_bst_operations()
