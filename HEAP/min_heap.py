import heapq

minHeap = []

heapq.heapify(minHeap)

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)

print("minHeap:", minHeap)

peekNum = minHeap[0]
print("peek number: ", peekNum)

popNum = heapq.heappop(minHeap)
print("minHeap: ", minHeap)
