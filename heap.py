"""
Heap Operations:
1. Heapify : Process of creating a min heap or a maxheap from a binary tree

First index of non-leaf node -> n/2 - 1
"""

class MinHeap:
    def __init__(self, arr):
        self.min_heap = arr
        self.size = len(arr)

        for i in range(self.size//2 -1 , -1, -1):
            self.heapify_minHeap(i)
    
    def heapify_minHeap(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2

        if left < self.size and self.min_heap[left] < self.min_heap[idx]:
            smallest = left
        
        if right < self.size and self.min_heap[right] < self.min_heap[smallest]:
            smallest = right
        
        if smallest != idx:
            self.min_heap[smallest],self.min_heap[idx] = self.min_heap[idx],self.min_heap[smallest]
            self.heapify_minHeap(smallest)

class MaxHeap:
    def __init__(self, arr):
        self.max_heap = arr
        self.size = len(arr)

        for i in range(self.size//2 -1 , -1, -1):
            self.heapify_maxHeap(i)
    
    def heapify_maxHeap(self, idx):
        largest = idx
        left = 2*idx + 1
        right = 2*idx + 2

        if left < self.size and self.max_heap[left] > self.max_heap[idx]:
            largest = left
        
        if right < self.size and self.max_heap[right] > self.max_heap[largest]:
            largest = right
        
        if largest != idx:
            self.max_heap[largest],self.max_heap[idx] = self.max_heap[idx],self.max_heap[largest]
            self.heapify_maxHeap(largest)

tree = [1,4,2,3,5,7,9]

heap = MinHeap(tree)
print(heap.min_heap)

tree1 = [1,4,2,3,5,7,9]
mx_heap = MaxHeap(tree1)
print(mx_heap.max_heap)