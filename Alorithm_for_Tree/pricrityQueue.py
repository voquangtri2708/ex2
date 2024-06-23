import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # Using -priority to make a max-heap
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# Example usage
pq = PriorityQueue()
pq.push('task 7', 7)
pq.push('task 2', 2)
pq.push('task 1', 1)
pq.push('task 9', 9)
pq.push('task 3', 3)
pq.push('task 8', 8)
pq.push('task 5', 5)

while pq._queue:
    print(pq.pop())
