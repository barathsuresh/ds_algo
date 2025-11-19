
````markdown
# Python Algorithm Interview Cheat Sheet 🚀

A curated collection of Python templates for the most common algorithmic patterns found in technical interviews (Google, Meta, Amazon, etc.).

## 🛠️ Essential Imports

Copy this block at the start of every solution to ensure you have the necessary tools.

```python
from typing import List, Optional, Dict, Set
from collections import deque, defaultdict, Counter
import heapq
import math
import functools
````

-----

## 1\. Two Pointers

**Use for:** Sorted arrays, finding pairs, removing duplicates, reversing.
**Complexity:** Time $O(N)$, Space $O(1)$.

```python
def two_pointers(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return []
```

-----

## 2\. Sliding Window

**Use for:** Longest/shortest substring or subarray satisfying a condition.
**Complexity:** Time $O(N)$, Space $O(K)$ (where K is window content).

```python
def sliding_window(s: str):
    window_data = defaultdict(int) # or set(), or Counter()
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        window_data[char] += 1
        
        # Shrink window WHILE condition is broken
        while (CONDITION_IS_BROKEN):
            remove_char = s[left]
            window_data[remove_char] -= 1
            if window_data[remove_char] == 0:
                del window_data[remove_char]
            left += 1
        
        # Update result (Window is valid here)
        max_len = max(max_len, right - left + 1)

    return max_len
```

-----

## 3\. Binary Search

**Use for:** Sorted arrays, searching for a value, finding boundaries.
**Complexity:** Time $O(\log N)$, Space $O(1)$.

```python
def binary_search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid # Found
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1 # Not found
```

-----

## 4\. BFS (Breadth-First Search)

**Use for:** Shortest path in unweighted graphs, level-order tree traversal.
**Complexity:** Time $O(V+E)$, Space $O(V)$.

```python
def bfs(root):
    if not root: return []
    
    queue = deque([root])
    visited = set([root])
    levels = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft() # O(1) operation
            current_level.append(node.val)

            for neighbor in [node.left, node.right]: # or graph[node]
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        levels.append(current_level)
    return levels
```

-----

## 5\. DFS (Depth-First Search) - Recursive

**Use for:** Exploring paths, backtracking, connectivity (Islands problems).
**Complexity:** Time $O(V+E)$, Space $O(V)$ (recursion stack).

```python
def dfs_recursive(grid: List[List[str]]):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        # Base Cases: Out of bounds, visited, or invalid cell
        if (r < 0 or c < 0 or r >= rows or c >= cols or
            (r, c) in visited or grid[r][c] == '0'):
            return

        visited.add((r, c))
        
        # Visit 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
```

-----

## 6\. Backtracking

**Use for:** Permutations, combinations, subsets, Sudoku.
**Complexity:** Exponential (e.g., $O(2^N)$ or $O(N!)$).

```python
def backtracking(nums: List[int]):
    result = []
    
    def backtrack(start_index, current_path):
        # 1. Goal Case
        result.append(current_path[:]) # Deep copy
        
        # 2. Iterate Choices
        for i in range(start_index, len(nums)):
            # (Optional) Constraint check
            
            # A. Make choice
            current_path.append(nums[i])
            
            # B. Recurse
            backtrack(i + 1, current_path)
            
            # C. Undo choice (Backtrack)
            current_path.pop()

    backtrack(0, [])
    return result
```

-----

## 7\. Priority Queue (Heaps)

**Use for:** Top K elements, merging sorted lists, dynamic median.
**Note:** Python's `heapq` is a **Min-Heap** by default. To use as Max-Heap, negate numbers (`-val`).
**Complexity:** Insertion/Pop $O(\log N)$.

```python
import heapq

def k_closest(points: List[List[int]], k: int):
    min_heap = []
    
    for x, y in points:
        dist = x**2 + y**2
        # Tuple format: (priority, data)
        heapq.heappush(min_heap, (dist, [x, y]))

    # If Top K Logic (Max Heap):
    # 1. Push item
    # 2. If len(heap) > k: heapq.heappop(heap)
    
    res = []
    for _ in range(k):
        dist, point = heapq.heappop(min_heap)
        res.append(point)
    return res
```

-----

## 8\. Dynamic Programming

### A. Top-Down (Memoization)

**Best for:** Intuitive translation of recursion to efficient code.

```python
def dp_memo(n: int, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    
    memo[n] = dp_memo(n - 1, memo) + dp_memo(n - 2, memo)
    return memo[n]
```

### B. Bottom-Up (Tabulation)

**Best for:** Iterative approach, saving stack space.

```python
def dp_tabulation(n: int):
    if n <= 1: return n
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]
```

-----

## ⚡ Quick Collection Reference

| Collection | Import | Why use it? |
| :--- | :--- | :--- |
| **Deque** | `from collections import deque` | $O(1)$ append/pop from both ends. Essential for BFS. |
| **DefaultDict** | `from collections import defaultdict` | Auto-initializes keys. Great for Graphs (`adj = defaultdict(list)`). |
| **Counter** | `from collections import Counter` | Instant frequency map. `Counter(string)` gives `{'a': 2, 'b': 1}`. |
| **Heap** | `import heapq` | $O(\log N)$ priority queue. |
| **Set** | Built-in `set()` | $O(1)$ lookup. Essential for `visited` tracking. |

```
```