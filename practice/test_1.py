import heapq

def is_delivery_possible(truck_capacities, package_weights):
    # 1. Sort packages heaviest to lightest
    package_weights.sort(reverse=True)
    
    # 2. Create a Max-Heap for trucks. 
    # Python's heapq is a Min-Heap by default, so we store negative values
    # to simulate a Max-Heap.
    truck_heap = [-c for c in truck_capacities]
    heapq.heapify(truck_heap)
    print(truck_heap)  # Debug: Show initial truck heap
    # 3. Process each package
    for pkg in package_weights:
        # If no trucks are left (or we ran out of valid trucks), fail
        if not truck_heap:
            return 0
        
        # Get the strongest truck available (convert back to positive)
        current_max_capacity = -heapq.heappop(truck_heap)
        
        # Check if this truck can carry the package
        if current_max_capacity < pkg:
            return 0 # Strongest truck is too weak, fail.
            
        # Deliver package, reduce capacity, and put truck back in pool
        new_capacity = current_max_capacity // 2
        heapq.heappush(truck_heap, -new_capacity)
        
    # If we finished the loop, all packages were delivered
    return 1

def solve_scenarios(scenarios):
    results = []
    for truck_caps, pkg_weights in scenarios:
        results.append(is_delivery_possible(truck_caps, pkg_weights))
    return results

# --- Test with the Example from Image ---
# Scenario 1: Trucks=[7], Packages=[4, 3]
scenarios = [
    ([7,1,2,2,5,68,8], [4, 3])
]

print(f"Results: {solve_scenarios(scenarios)}")