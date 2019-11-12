from c4_max_heap import MaxHeap
class PriorityQueue:
    def __init__(self):
        self._max_heap=MaxHeap()
    def get_size(self):
        self._max_heap.get_size()
    def is_empty(self):
        self._max_heap.is_empty()
    def get_max(self):
        return self._max_heap.find_max()
    def enqueue(self,e):
        self._max_heap.add(e)
    def dequeue(self):
        return self._max_heap.extract_max()
