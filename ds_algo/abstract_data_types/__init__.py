"""
Abstract Data Types (ADT) Module

This module contains implementations of fundamental Abstract Data Types that provide
a clean interface while hiding implementation details. ADTs focus on WHAT operations
are available rather than HOW they are implemented.

Available ADTs:
- Stack: LIFO (Last In, First Out) operations with push, pop, peek
- Queue: FIFO (First In, First Out) operations with enqueue, dequeue, front, rear

Each ADT is implemented with both array-based and linked-list-based backends to
demonstrate different performance trade-offs and design patterns.
"""

from .stacks import ArrayStack, LinkedStack, StackNode
from .queues import ArrayQueue, LinkedQueue, QNode

__all__ = [
    "ArrayStack",
    "LinkedStack",
    "StackNode",
    "ArrayQueue",
    "LinkedQueue",
    "QNode",
]

__version__ = "1.0.0"
__author__ = "DSA Learning Project"
