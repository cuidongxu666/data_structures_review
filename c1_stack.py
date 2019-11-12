from c1_array import Array
class Stack:
    def __init__(self,capacity=0):
        self._stack=Array(capacity=capacity)

    def is_empty(self):
        return self._stack.is_empty()

    def get_capacity(self):
        return self._stack.get_capacity()

    def get_size(self):
        return self._stack.get_size()

    def push(self,e):
        self._stack.add_last(e)

    def pop(self):
        return self._stack.remove_last()

    def peek(self):
        return self._stack.get_last()


