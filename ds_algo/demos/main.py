"""
Main demonstration script for the Data Structures and Algorithms Learning Project.

This script provides an interactive menu to explore different modules and
their demonstrations, making it easy for learners to discover and understand
the various data structures and algorithms implemented in this package.
"""

import sys
from typing import Dict, Callable


def main():
    """Main entry point for the demonstration script."""
    print("🎓 Welcome to Data Structures and Algorithms Learning Project!")
    print("=" * 60)
    print()

    while True:
        display_main_menu()
        choice = get_user_choice()

        if choice == "0":
            print("\n👋 Thank you for using the DSA Learning Project!")
            print("Happy learning! 🚀")
            break

        try:
            execute_demo(choice)
        except Exception as e:
            print(f"\n❌ Error executing demo: {e}")
            print("Please try again or report this issue.")

        input("\nPress Enter to continue...")


def display_main_menu():
    """Display the main menu options."""
    print("\n🏠 MAIN MENU")
    print("-" * 30)
    print("1. 📊 Complexity Analysis Demos")
    print("2. 📐 Linear Structures Demos")
    print("3. 🎭 Abstract Data Types Demos")
    print("4. 🌳 Non-Linear Structures Demos")
    print("5. 🎯 Quick Tour (All Highlights)")
    print("6. 📚 Learning Resources")
    print("0. 🚪 Exit")
    print()


def get_user_choice() -> str:
    """Get and validate user menu choice."""
    while True:
        choice = input("Enter your choice (0-6): ").strip()
        if choice in ["0", "1", "2", "3", "4", "5", "6"]:
            return choice
        print("❌ Invalid choice. Please enter a number from 0-6.")


def execute_demo(choice: str):
    """Execute the selected demonstration."""
    demo_functions: Dict[str, Callable] = {
        "1": demo_complexity_analysis,
        "2": demo_linear_structures,
        "3": demo_abstract_data_types,
        "4": demo_non_linear_structures,
        "5": demo_quick_tour,
        "6": show_learning_resources,
    }

    if choice in demo_functions:
        demo_functions[choice]()
    else:
        print("❌ Demo not implemented yet.")


def demo_complexity_analysis():
    """Demonstrate complexity analysis concepts."""
    print("\n📊 COMPLEXITY ANALYSIS DEMONSTRATIONS")
    print("=" * 45)

    try:
        from ds_algo.complexity_analysis.time_complexity import (
            demonstrate_constant_time,
            demonstrate_linear_time,
            demonstrate_logarithmic_time,
            demonstrate_quadratic_time,
        )

        print("\n1. O(1) - Constant Time Operations")
        demonstrate_constant_time()

        print("\n2. O(n) - Linear Time Operations")
        demonstrate_linear_time([100, 500, 1000])

        print("\n3. O(log n) - Logarithmic Time Operations")
        demonstrate_logarithmic_time()

        print("\n4. O(n²) - Quadratic Time Operations")
        demonstrate_quadratic_time()

        print("\n✅ Complexity analysis demos completed!")
        print("💡 Notice how different complexities scale with input size.")

    except ImportError:
        print("❌ Complexity analysis module not available.")
        print("Make sure all modules are properly installed.")


def demo_linear_structures():
    """Demonstrate linear data structures."""
    print("\n📐 LINEAR STRUCTURES DEMONSTRATIONS")
    print("=" * 40)

    try:
        # Arrays and Lists
        from ds_algo.linear_structures.static.lists import PythonListOperations

        print("\n1. Python List Operations")
        ops = PythonListOperations()
        ops.demonstrate_growth_pattern()
        ops.analyze_append_performance()

        # Linked Lists
        from ds_algo.linear_structures.dynamic import SinglyLinkedList, DoublyLinkedList

        print("\n2. Singly Linked List")
        sll = SinglyLinkedList([1, 2, 3, 4, 5])
        sll.prepend(0)
        sll.append(6)
        print(f"   SLL: {list(sll)}")

        print("\n3. Doubly Linked List")
        dll = DoublyLinkedList([10, 20, 30])
        dll.prepend(5)
        dll.append(40)
        print(f"   DLL Forward: {list(dll)}")
        print(f"   DLL Backward: {list(dll.reverse_iterator())}")

        print("\n✅ Linear structures demos completed!")
        print("💡 Compare the different access patterns and use cases.")

    except ImportError:
        print("❌ Linear structures module not available.")


def demo_abstract_data_types():
    """Demonstrate abstract data types."""
    print("\n🎭 ABSTRACT DATA TYPES DEMONSTRATIONS")
    print("=" * 42)

    try:
        # Stack Demo
        from ds_algo.abstract_data_types import ArrayStack, LinkedQueue
        from ds_algo.abstract_data_types.stacks import demonstrate_stack_applications

        print("\n1. Stack (LIFO) Operations")
        stack = ArrayStack([1, 2, 3])
        print(f"   Initial: {stack}")
        stack.push(4)
        print(f"   After push(4): {stack}")
        print(f"   Popped: {stack.pop()}")
        print(f"   Peek top: {stack.peek()}")

        print("\n2. Stack Applications")
        demonstrate_stack_applications()

        print("\n3. Queue (FIFO) Operations")
        queue = LinkedQueue(["first", "second", "third"])
        print(f"   Initial: {queue}")
        queue.enqueue("fourth")
        print(f"   After enqueue: {queue}")
        print(f"   Dequeued: {queue.dequeue()}")
        print(f"   Front: {queue.front()}, Rear: {queue.rear()}")

        print("\n✅ Abstract data types demos completed!")
        print("💡 LIFO vs FIFO - different ordering strategies for different needs.")

    except ImportError:
        print("❌ Abstract data types module not available.")


def demo_non_linear_structures():
    """Demonstrate non-linear data structures."""
    print("\n🌳 NON-LINEAR STRUCTURES DEMONSTRATIONS")
    print("=" * 44)

    try:
        from ds_algo.non_linear_structures import BSTNode, TreeNode

        print("\n1. General Tree Structure")
        root = TreeNode("CEO")
        cto = TreeNode("CTO")
        cfo = TreeNode("CFO")
        root.add_child(cto)
        root.add_child(cfo)
        cto.add_child(TreeNode("Engineering"))
        cto.add_child(TreeNode("Product"))
        print("   Organization Chart:")
        print(str(root))

        print("\n2. Binary Search Tree Operations")
        bst = BSTNode(50)
        values = [30, 70, 20, 40, 60, 80]

        print(f"   Inserting values: {values}")
        for val in values:
            bst.insert(val)

        print(f"   Inorder (sorted): {bst.inorder_traversal()}")
        print(f"   Preorder: {bst.preorder_traversal()}")
        print(f"   Level-order: {bst.level_order_traversal()}")

        print(f"\n   Search Results:")
        for search_val in [40, 25, 80]:
            result = bst.search(search_val)
            print(f"   Search {search_val}: {result}")

        print("\n✅ Non-linear structures demos completed!")
        print("💡 Trees enable efficient hierarchical organization and searching.")

    except ImportError:
        print("❌ Non-linear structures module not available.")


def demo_quick_tour():
    """Provide a quick tour of all main features."""
    print("\n🎯 QUICK TOUR - DSA HIGHLIGHTS")
    print("=" * 35)

    print("\n🚀 Running abbreviated demos of all modules...")

    # Quick complexity demo
    print("\n📊 Complexity Analysis Sample:")
    try:
        from ds_algo.complexity_analysis.time_complexity import (
            demonstrate_constant_time,
        )

        demonstrate_constant_time()
    except ImportError:
        print("   ❌ Module not available")

    # Quick linear structure demo
    print("\n📐 Linear Structure Sample:")
    try:
        from ds_algo.linear_structures.dynamic import SinglyLinkedList

        sll = SinglyLinkedList([1, 2, 3])
        sll.append(4)
        print(f"   Singly Linked List: {list(sll)}")
    except ImportError:
        print("   ❌ Module not available")

    # Quick ADT demo
    print("\n🎭 Abstract Data Type Sample:")
    try:
        from ds_algo.abstract_data_types import ArrayStack

        stack = ArrayStack([10, 20])
        stack.push(30)
        print(f"   Stack operations: push(30) → {stack}")
        print(f"   Peek top: {stack.peek()}")
    except ImportError:
        print("   ❌ Module not available")

    # Quick tree demo
    print("\n🌳 Tree Structure Sample:")
    try:
        from ds_algo.non_linear_structures import BSTNode

        bst = BSTNode(50)
        bst.insert(30)
        bst.insert(70)
        print(f"   BST inorder traversal: {bst.inorder_traversal()}")
    except ImportError:
        print("   ❌ Module not available")

    print("\n✅ Quick tour completed!")
    print("💡 Explore individual modules for detailed demonstrations.")


def show_learning_resources():
    """Display learning resources and guidance."""
    print("\n📚 LEARNING RESOURCES AND GUIDANCE")
    print("=" * 42)

    print("\n🎓 LEARNING PATHS:")
    print("   1. Beginner: Start with complexity analysis, then linear structures")
    print("   2. Intermediate: Master ADTs, then move to trees")
    print("   3. Advanced: Implement custom algorithms using these structures")

    print("\n📖 DOCUMENTATION:")
    print("   • README.md - Main project overview and quick start")
    print("   • ds_algo/complexity_analysis/README.md - Algorithm analysis")
    print("   • ds_algo/linear_structures/README.md - Sequential data")
    print("   • ds_algo/abstract_data_types/README.md - LIFO/FIFO concepts")
    print("   • ds_algo/non_linear_structures/README.md - Hierarchical data")

    print("\n🔧 INTERACTIVE EXPLORATION:")
    print("   • Import modules directly in Python REPL")
    print("   • Run module tests: python -m ds_algo.module_name")
    print("   • Explore source code for implementation details")

    print("\n🌐 EXTERNAL RESOURCES:")
    print("   • Big O Cheat Sheet: https://www.bigocheatsheet.com/")
    print("   • Visualizations: https://visualgo.net/")
    print("   • Interactive DS: https://www.cs.usfca.edu/~galles/visualization/")

    print("\n💡 TIPS:")
    print("   • Start with understanding complexity before implementation")
    print("   • Practice with small examples before large datasets")
    print("   • Compare different implementations for the same problem")
    print("   • Focus on understanding trade-offs between approaches")

    print("\n🎯 RECOMMENDED EXERCISES:")
    print("   1. Implement basic algorithms using provided structures")
    print("   2. Compare performance of different data structures")
    print("   3. Solve problems that require multiple data structures")
    print("   4. Create visualizations of algorithm execution")


if __name__ == "__main__":
    main()
