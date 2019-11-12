from c2_linkedlist import LinkedList
class LinkedListStack:
    def __init__(self):
        self._stack=LinkedList()

    def push(self,e):
        self._stack.add_first(e)
    def pop(self):
        self._stack.remove_first()
