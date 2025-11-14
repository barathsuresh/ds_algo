"""
Non-Linear Data Structures Module

This module contains implementations of non-linear data structures where elements
are not arranged in a sequential manner. These structures are hierarchical and
allow for complex relationships between elements.

Available Structures:
- Trees: General tree, binary tree, binary search tree
- Future: Graphs, heaps, hash tables

Non-linear structures are essential for:
- Hierarchical data representation (file systems, DOM)
- Efficient searching and sorting (BST, heaps)
- Network modeling (graphs)
- Database indexing (B-trees)
"""

from .trees import TreeNode, BinaryTreeNode, BSTNode

__all__ = ["TreeNode", "BinaryTreeNode", "BSTNode"]

__version__ = "1.0.0"
__author__ = "DSA Learning Project"
