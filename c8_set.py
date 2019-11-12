from c3_bst import BST
from c2_linkedlist import LinkedList
class BSTSet:
    def __init__(self):
        self._set=BST()

    def get_size(self):
        return self._set._size()

    def is_empty(self):
        return self._set.is_empty()

    def add(self,e):
        self._set.add(e)

    def contains(self,e):
        return self._set.contain(e)

    def remove(self,e):
        return self._set.remove(e)

class LinkedlistSet:
    def __init__(self):
        self._list=LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def contains(self, e):
        return self._list.contains(e)

    def add(self, e):
        if self.contains(e):
            return
        self._list.add_first()

    def remove(self, e):
        self._list.remove(e)