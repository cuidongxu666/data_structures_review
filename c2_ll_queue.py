class LinkedListQueue:
    class _Node:
        def __init__(self,e=None):
            self.e=e
            self.next=None

    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def enqueue(self,e):
        if self._tail==None:
            self._tail=self._Node(e)
            self._head=self._tail

        else:
            self._tail.next=self._Node(e)
            self._tail=self._tail.next
            self._size+=1

    def dequque(self):
        ret=self._head
        self._head=ret.next
        ret.next=None

        if not self._head:
            self._tail=None
        self._size-=1

        return ret.e

