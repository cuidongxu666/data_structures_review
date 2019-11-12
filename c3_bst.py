from c1_loop_queue import LoopQueue
class BST:
    class _Node:
        def __init__(self,e=None):
            self.e=e
            self.left=None
            self.right=None
    def __init__(self):
        self._size=0
        self._root=None


    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def add(self,e):
        self._root=self._add(self._root,e)
    def _add(self,node,e):
        if not node:
            self._size+=1
            return self._Node(e)
        if node.e>e:
            node.left=self._add(node.left,e)
        elif node.e<e:
            node.right=self._add(node.right,e)
        return node

    def contain(self,e):
        return self._contain(self._root,e)
    def _contain(self,node,e):
        if not node:
            return False

        if node.e==e:
            return True

        elif node.e>e:
            return self._contain(node.left,e)
        else:
            return self._contain(node.right,e)

    def pre(self):
        self._pre(self._root)
    def _pre(self,node):
        if not node:
            return
        print(node.e)
        self._pre(node.left)
        self._pre(node.right)

    def pre_nr(self):
        stack=[]
        stack.append(self._root)
        while stack:
            curr=stack.pop()
            print(curr)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    def level_order(self):
        queue=LoopQueue()
        queue.enquque(self._root)
        while queue:
            curr=queue.dequque()
            print(curr)
            if curr.left:
                queue.enquque(curr.left)
            if curr.right:
                queue.enquque(curr.right)

    def minimun(self):
        return self._minimum(self._root)

    def _minimum(self,node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self.is_empty():
            raise ValueError('BST is empty!')
        return self._maximum(self._root)

    def _maximum(self, node):
        if not node.right:
            return node
        return self._maximum(node.right)

    def remove_min(self):
        ret=self.minimun()
        self._root=self._remove_min(self._root)
        return ret

    def _remove_min(self,node):
        if not node.left:
            right_node=node.right
            node.right=None
            self._size-=1
            return right_node
        node.left= self._remove_min(node.left)
        return node

    def remove_max(self):
        ret = self.maximum()
        # 用单链表来验证
        self._root = self._remove_max(self._root)
        return ret

        # 删除掉以node为根的BST中的最大节点
        # 返回删除节点后新的BST的根

    def _remove_max(self, node):
        # 递归终止
        if not node.right:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node
        node.right = self._remove_max(node.right)
        return node

    def remove(self,e):
        self._root=self._remove(self._root,e)

    def _remove(self,node,e):
        if not node:
            return
        if node.e>e:
            node.left=self._remove(node.left,e)
            return node
        elif node.e<e:
            node.right=self._remove(node.right,e)
            return node
        else:
            #这边需要在看看，是否互斥条件
            if not node.right:
                left_node=node.left
                node.left=None
                self._size-=1
                return left_node

            if not node.left:
                right_node=node.right
                node.right=None
                self._size-=1
                return right_node

            successor=self._minimum(node.right)
            successor.right=self._remove_min(node.right)
            successor.left=node.left
            node.left=node.right=None
            return successor



