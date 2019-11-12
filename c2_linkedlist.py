class LinkedList:
    class _Node:
        def __init__(self,e=None):
            self.e=e
            self.next=None

    def __init__(self):
        self._dummy_node=self._Node()
        self._size=0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def add(self,index,e):
        prev=self._dummy_node
        for i in range(index):
            prev=prev.next

        node=self._Node(e)
        node.next=prev.next
        prev.next=node
        self._size+=1

    def add_first(self,e):
        self.add(0,e)

    def get_element(self,index):
        curr=self._dummy_node.next
        for i in range(index):
            curr=curr.next
        return curr.e

    def get_first(self):
        return self.get_element(0)

    def get_last(self):
        return self.get_element(self._size-1)

    def set(self,index,e):
        curr=self._dummy_node.next
        for i in range(index):
            curr=curr.next
        curr.e=e

    def contains(self,e):
        curr=self._dummy_node.next
        while curr:
           if curr.e==e:
               return True
           else:
               curr=curr.next
        return False

    def remove(self,index):
        prev=self._dummy_node
        for i in range(index):
            prev=prev.next

        node=prev.next
        prev.next=node.next
        node.next=None
        self._size-=1
        return node.e

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size-1)