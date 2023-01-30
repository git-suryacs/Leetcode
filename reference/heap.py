import heapq

L = []
heapq.heapify(L)
heapq.heappush(L, 3)
heapq.heappush(L, 2)
print(heapq.heappop(L))