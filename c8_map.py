#链表映射没有索引，添加要么改值，要么从头添加，删除注意取到前面一个
class LinkedListMap:
    class _Node:
        def __init__(self,key=None,value=None,next=None):
            self.key=key
            self.value=value
            self.next=next

    def __init__(self):
        self._dummy_node=self._Node()
        self._size=0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def _get_node(self,key):
        curr=self._dummy_node.next
        while curr:
            if curr.key==key:
                return curr
            curr=curr.next

    def add(self,key,value):
        node=self._get_node(key)
        if not node:
            self._dummy_node.next=self._Node(key,value,self._dummy_node.next)
            self._size+=1
        else:
            node.value=value
    def contains(self,key):
        return self._get_node(key) is not None

    def getter(self,key):
        node=self._get_node(key)
        if node:
            return node.value
        else:
            return

    def setter(self,key,value):
        node = self._get_node(key)
        node.value = value


    def remove(self,key):

        prev=self._dummy_node
        while prev.next:
            if prev.next.key==key:
                break
            prev=prev.next
        if prev.next:
            del_node=prev.next
            prev.next=del_node.next
            del_node.next=None
            self._size-=1
            return del_node.value


class BSTMap:
    class _Node:
        def __init__(self,key=None,value=None):
            self.key=key
            self.value=value
            self.left=None
            self.right=None

    def __init__(self):
        self._root=None
        self._size=0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self,key,value):
        self._root=self._add(self._root,key,value)

    def _add(self,node,key,value):
        if not node:
            self._size+=1
            return self._Node(key,value)
        if node.key==key:
            node.value=value

        elif node.key>key:
            node.left=self._add(node.left,key,value)

        else:
            node.right=self._add(node.right,key,value)
        return node

    def _get_node(self,node,key):
        if not node:
            return

        if node.key==key:
            return node
        elif node.key>key:
            return self._get_node(node.left,key)
        else:
            return self._get_node(node.right,key)

    def contains(self,key):
        node=self._get_node(self._root,key)
        if node:
            return True
        else:
            return

    def getter(self,key):
        node=self._get_node(self._root,key)
        if node:
            return node
        else:
            return

    def setter(self,key,value):
        node=self._get_node(self._root,key)
        if node:
            node.value=value
        else:
            raise('key doesnt exist')

    def minimum(self):
        return self._minimum(self._root)

    def _minimum(self,node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def _remove_min(self,node):
        if not node.left:
            right_node=node.right
            node.right=None
            self._size-=1
            return right_node
        node.left=self._remove_min(node.left)
        return node

    def remove(self,key):
        node=self._get_node(self._root,key)
        if node:
            self._root=self._remove(self._root,key)
            return node.value
        return

    def _remove(self,node,key):
        if not node:
            return

        if node.key>key:
            node.left=self._remove(node.left,key)
            return node
        elif node.key<key:
            node.right=self._remove(node.right,key)
            return node
        else:
            if not node.left:
                right_node=node.right
                node.right=None
                self._size-=1
                return right_node

            elif not node.right:
                left_node=node.left
                node.left=None
                self._size-=1
                return left_node

            else:
                successor=self._minimum(node.right)
                successor.right=self._remove_min(node.right)
                successor.left=node.left
                node.left=node.right=None
                return successor

