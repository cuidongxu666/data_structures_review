from c1_array import Array
class ArrayQueue:
    def __init__(self,capacity=0):
        self._queue=Array(capacity=capacity)

    def get_size(self):
        self._queue.get_size()
    def is_empty(self):
        return self.get_size()==0

    def get_capacity(self):
        return self._queue.get_capacity()

    def enquque(self,e):
        self._queue.add_last(e)

    def dequque(self,e):
        return self._queue.remove_first()

    def check_front(self):
        return self._queue.get_first()



