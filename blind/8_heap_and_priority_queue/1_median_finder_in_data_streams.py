import heapq

class MedianFinder:

    def __init__(self):
        # Max-Heap for the lower half (store negatives to simulate max-heap)
        self.small = []  
        # Min-Heap for the upper half
        self.large = []  

    def addNum(self, num: int) -> None:
        # 1. Push to small heap (max-heap)
        # We push -num because Python only has min-heaps
        heapq.heappush(self.small, -num)
        
        # 2. Ensure every element in small is <= every element in large
        # Pop the max from small and push to large
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        # 3. Balance sizes: small heap can have at most 1 more element than large
        if len(self.small) < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If small heap is larger, the median is its top
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        # If sizes are equal, average the two tops
        return (-self.small[0] + self.large[0]) / 2.0

if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)    # arr = [1]
    medianFinder.addNum(2)    # arr = [1, 2]
    print(f"Median (1, 2): {medianFinder.findMedian()}") 
    # Expected: 1.5
    
    medianFinder.addNum(3)    # arr = [1, 2, 3]
    print(f"Median (1, 2, 3): {medianFinder.findMedian()}") 
    # Expected: 2.0