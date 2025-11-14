"""
Interactive testing playground for the Data Structures and Algorithms package.

This module provides an interactive environment where users can experiment
with different data structures, test their understanding, and explore
edge cases in a guided way.
"""

from typing import Any, Dict, List, Optional
import time
import traceback


class InteractivePlayground:
    """Interactive playground for exploring data structures and algorithms."""

    def __init__(self):
        self.session_data: Dict[str, Any] = {}
        self.history: List[str] = []

    def start(self):
        """Start the interactive playground session."""
        print("🎪 Welcome to the Interactive DS & Algorithms Playground!")
        print("=" * 55)
        print("Type 'help' for available commands, 'quit' to exit.")
        print()

        while True:
            try:
                command = input("playground> ").strip()

                if command.lower() in ["quit", "exit", "q"]:
                    print("\n👋 Thanks for playing! Keep learning!")
                    break
                elif command.lower() == "help":
                    self.show_help()
                elif command.lower() == "clear":
                    self.clear_session()
                elif command.lower() == "history":
                    self.show_history()
                elif command.lower().startswith("create"):
                    self.handle_create_command(command)
                elif command.lower().startswith("test"):
                    self.handle_test_command(command)
                elif command.lower().startswith("compare"):
                    self.handle_compare_command(command)
                elif command:
                    self.execute_python_code(command)

            except KeyboardInterrupt:
                print("\n\n👋 Exiting playground...")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                print("Type 'help' for available commands.")

    def show_help(self):
        """Display help information."""
        print("\n🆘 PLAYGROUND COMMANDS:")
        print("=" * 25)
        print("📝 General:")
        print("  help           - Show this help")
        print("  quit/exit/q    - Exit playground")
        print("  clear          - Clear session data")
        print("  history        - Show command history")
        print()
        print("🏗️  Creation Commands:")
        print("  create list <values>     - Create a list")
        print("  create stack <values>    - Create a stack")
        print("  create queue <values>    - Create a queue")
        print("  create bst <values>      - Create a binary search tree")
        print("  create linked <values>   - Create a linked list")
        print()
        print("🧪 Testing Commands:")
        print("  test performance <structure> - Performance test")
        print("  test operations <structure>  - Test basic operations")
        print()
        print("⚖️  Comparison Commands:")
        print("  compare <struct1> <struct2> - Compare two structures")
        print()
        print("🐍 Python Code:")
        print("  Any valid Python expression using created structures")
        print()
        print("💡 Examples:")
        print("  create stack 1,2,3")
        print("  my_stack.push(4)")
        print("  test performance my_stack")
        print("  compare my_stack my_list")

    def clear_session(self):
        """Clear all session data."""
        self.session_data.clear()
        self.history.clear()
        print("✅ Session cleared!")

    def show_history(self):
        """Show command history."""
        if not self.history:
            print("📜 No command history yet.")
            return

        print("\n📜 COMMAND HISTORY:")
        for i, cmd in enumerate(self.history, 1):
            print(f"  {i:2d}. {cmd}")

    def handle_create_command(self, command: str):
        """Handle structure creation commands."""
        parts = command.split()
        if len(parts) < 3:
            print("❌ Usage: create <type> <values>")
            print("   Example: create stack 1,2,3")
            return

        struct_type = parts[1].lower()
        values_str = " ".join(parts[2:])

        try:
            # Parse values
            if "," in values_str:
                values = [self._parse_value(v.strip()) for v in values_str.split(",")]
            else:
                values = [self._parse_value(v) for v in values_str.split()]

            # Create the structure
            structure = self._create_structure(struct_type, values)

            # Generate a unique name
            var_name = f"my_{struct_type}"
            counter = 1
            while var_name in self.session_data:
                var_name = f"my_{struct_type}_{counter}"
                counter += 1

            self.session_data[var_name] = structure
            print(f"✅ Created {struct_type}: {var_name} = {structure}")
            self.history.append(command)

        except Exception as e:
            print(f"❌ Error creating {struct_type}: {e}")

    def _parse_value(self, value_str: str) -> Any:
        """Parse a string value to appropriate type."""
        value_str = value_str.strip()

        # Try integer
        try:
            return int(value_str)
        except ValueError:
            pass

        # Try float
        try:
            return float(value_str)
        except ValueError:
            pass

        # Try boolean
        if value_str.lower() in ["true", "false"]:
            return value_str.lower() == "true"

        # Return as string (remove quotes if present)
        if (value_str.startswith('"') and value_str.endswith('"')) or (
            value_str.startswith("'") and value_str.endswith("'")
        ):
            return value_str[1:-1]

        return value_str

    def _create_structure(self, struct_type: str, values: List[Any]):
        """Create a data structure of the specified type."""
        try:
            if struct_type == "list":
                return list(values)

            elif struct_type == "stack":
                from ds_algo.abstract_data_types import ArrayStack

                return ArrayStack(values)

            elif struct_type == "queue":
                from ds_algo.abstract_data_types import ArrayQueue

                return ArrayQueue(values)

            elif struct_type == "linked":
                from ds_algo.linear_structures.dynamic import SinglyLinkedList

                return SinglyLinkedList(values)

            elif struct_type == "bst":
                from ds_algo.non_linear_structures import BSTNode

                if not values:
                    raise ValueError("BST requires at least one value")

                bst = BSTNode(values[0])
                for val in values[1:]:
                    bst.insert(val)
                return bst

            else:
                raise ValueError(f"Unknown structure type: {struct_type}")

        except ImportError:
            raise ValueError(f"Module for {struct_type} not available")

    def handle_test_command(self, command: str):
        """Handle testing commands."""
        parts = command.split()
        if len(parts) < 3:
            print("❌ Usage: test <type> <structure_name>")
            return

        test_type = parts[1].lower()
        struct_name = parts[2]

        if struct_name not in self.session_data:
            print(f"❌ Structure '{struct_name}' not found.")
            print(f"Available: {list(self.session_data.keys())}")
            return

        structure = self.session_data[struct_name]

        try:
            if test_type == "performance":
                self._test_performance(struct_name, structure)
            elif test_type == "operations":
                self._test_operations(struct_name, structure)
            else:
                print(f"❌ Unknown test type: {test_type}")

        except Exception as e:
            print(f"❌ Error testing {struct_name}: {e}")

    def _test_performance(self, name: str, structure):
        """Test performance of a data structure."""
        print(f"\n⏱️  PERFORMANCE TEST: {name}")
        print("=" * 30)

        # Test different operations based on type
        if hasattr(structure, "append"):  # List-like
            self._time_operation(lambda: structure.append(999), "Append operation")

        if hasattr(structure, "push"):  # Stack-like
            self._time_operation(lambda: structure.push(999), "Push operation")
            self._time_operation(
                lambda: structure.pop() if structure else None, "Pop operation"
            )

        if hasattr(structure, "enqueue"):  # Queue-like
            self._time_operation(lambda: structure.enqueue(999), "Enqueue operation")
            self._time_operation(
                lambda: structure.dequeue() if structure else None, "Dequeue operation"
            )

        if hasattr(structure, "search"):  # Tree-like
            self._time_operation(lambda: structure.search(999), "Search operation")

    def _time_operation(self, operation, description: str):
        """Time a single operation."""
        try:
            start_time = time.perf_counter()
            result = operation()
            end_time = time.perf_counter()

            duration = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"  {description}: {duration:.4f} ms")

        except Exception as e:
            print(f"  {description}: ❌ {e}")

    def _test_operations(self, name: str, structure):
        """Test basic operations of a data structure."""
        print(f"\n🧪 OPERATIONS TEST: {name}")
        print("=" * 30)

        # Test based on structure type
        if hasattr(structure, "append"):  # List-like
            print(f"Current: {structure}")
            structure.append(42)
            print(f"After append(42): {structure}")

        if hasattr(structure, "push"):  # Stack-like
            print(f"Current: {structure}")
            structure.push(42)
            print(f"After push(42): {structure}")
            if structure:
                popped = structure.pop()
                print(f"Popped: {popped}, Remaining: {structure}")

        if hasattr(structure, "enqueue"):  # Queue-like
            print(f"Current: {structure}")
            structure.enqueue(42)
            print(f"After enqueue(42): {structure}")
            if structure:
                dequeued = structure.dequeue()
                print(f"Dequeued: {dequeued}, Remaining: {structure}")

    def handle_compare_command(self, command: str):
        """Handle structure comparison commands."""
        parts = command.split()
        if len(parts) < 3:
            print("❌ Usage: compare <struct1> <struct2>")
            return

        name1, name2 = parts[1], parts[2]

        if name1 not in self.session_data:
            print(f"❌ Structure '{name1}' not found.")
            return

        if name2 not in self.session_data:
            print(f"❌ Structure '{name2}' not found.")
            return

        struct1 = self.session_data[name1]
        struct2 = self.session_data[name2]

        print(f"\n⚖️  COMPARISON: {name1} vs {name2}")
        print("=" * 40)
        print(f"  {name1}: {struct1}")
        print(f"  {name2}: {struct2}")
        print(f"  Type {name1}: {type(struct1).__name__}")
        print(f"  Type {name2}: {type(struct2).__name__}")

        # Size comparison if available
        try:
            size1 = len(struct1)
            size2 = len(struct2)
            print(f"  Size {name1}: {size1}")
            print(f"  Size {name2}: {size2}")
        except:
            pass

        # Memory comparison (rough estimate)
        try:
            import sys

            mem1 = sys.getsizeof(struct1)
            mem2 = sys.getsizeof(struct2)
            print(f"  Memory {name1}: {mem1} bytes")
            print(f"  Memory {name2}: {mem2} bytes")
        except:
            pass

    def execute_python_code(self, code: str):
        """Execute Python code with access to session data."""
        try:
            # Make session data available as local variables
            local_vars = self.session_data.copy()

            # Add common imports
            exec(
                """
from ds_algo.abstract_data_types import ArrayStack, LinkedStack, ArrayQueue, LinkedQueue
from ds_algo.linear_structures.dynamic import SinglyLinkedList, DoublyLinkedList
from ds_algo.non_linear_structures import BSTNode, TreeNode
            """,
                local_vars,
            )

            result = eval(code, {}, local_vars)

            if result is not None:
                print(f"Result: {result}")

            # Update session data with any new variables
            for name, value in local_vars.items():
                if not name.startswith("_"):  # Ignore private variables
                    self.session_data[name] = value

            self.history.append(code)

        except SyntaxError:
            try:
                # Try executing as statement instead of expression
                local_vars = self.session_data.copy()
                exec(code, {}, local_vars)

                # Update session data
                for name, value in local_vars.items():
                    if not name.startswith("_"):
                        self.session_data[name] = value

                self.history.append(code)
                print("✅ Executed successfully")

            except Exception as e:
                print(f"❌ Execution error: {e}")

        except Exception as e:
            print(f"❌ Evaluation error: {e}")


def main():
    """Main entry point for the interactive playground."""
    playground = InteractivePlayground()
    playground.start()


if __name__ == "__main__":
    main()
