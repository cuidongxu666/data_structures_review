class AVLMap:
    class _Node:
        def __init__(self,key=None,value=None):
            self.key=key
            self.value=value
            self.left=None
            self.right=None
            self.height=1

    def __init__(self):
        self._root=None
        self._size=0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    # --------------------------------------------------
    #获得当前节点高度
    def get_height(self,node):
        if not node:
            return 0
        return node.height

    #计算当前节点的平衡因子
    def get_balance_factor(self,node):
        if not node:
            return 0
        return self.get_height(node.left)-self.get_height(node.right)

    def is_bst(self):
        keys=[]
        self._in_order(self._root,keys)
        for i in range(1,len(keys)):
            if keys[i-1]>keys[i]:
                return False
        return True
    def get_all_nodes(self):
        keys=[]
        self._in_order(self._root, keys)

    def _in_order(self,node,keys):
        if not node:
            return
        self._in_order(node.left,keys)
        keys.append(node)
        self._in_order(node.right,keys)
    # ---------------------------------------------------------------

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
        #每层维护node高度
        node.height=1+max(self.get_height(node.left),self.get_height((node.right)))

        balance_factor=self.get_balance_factor(node)
        if balance_factor>1 and self.get_balance_factor(node.left)>=0:
            return self._right_rotate(node)
        if balance_factor<-1 and self.get_balance_factor(node.right)<=0:
            return self._left_rotate(node)
        if balance_factor>1 and self.get_balance_factor(node.left)<0:
            self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance_factor<-1 and self.get_balance_factor(node.right)>0:
            self._right_rotate(node.right)
            return self._left_rotate(node)
        return node


    def _right_rotate(self,y):
        x=y.left
        t=x.right
        x.right=y
        y.left=t
        #旋转后维护高度
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))
        return x

    def _left_rotate(self,y):
        x=y.right
        t=x.left
        x.left=y
        y.right=t
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

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

    def get(self,key):
        node=self._get_node(self._root,key)
        if node:
            return node
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

    # def _remove_min(self,node):
    #     if not node.left:
    #         right_node=node.right
    #         node.right=None
    #         self._size-=1
    #         return right_node
    #     node.left=self._remove_min(node.left)
    #     return node

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
            ret= node
        elif node.key<key:
            node.right=self._remove(node.right,key)
            ret= node
        else:
            if not node.left:
                right_node=node.right
                node.right=None
                self._size-=1
                ret= right_node

            elif not node.right:
                left_node=node.left
                node.left=None
                self._size-=1
                ret= left_node

            else:
                successor=self._minimum(node.right)
                successor.right=self._remove(node.right,successor.key)
                successor.left=node.left
                node.left=node.right=None
                ret= successor
        if not ret:
            return

        ret.height=1+max(self.get_height(ret.left),self.get_height(ret.right))
        balance_factor=self.get_balance_factor(ret)
        if balance_factor>1 and self.get_balance_factor(node.left)>=0:
            return self._right_rotate(node)
        if balance_factor<-1 and self.get_balance_factor(node.right)<=0:
            return self._left_rotate(node)
        if balance_factor>1 and self.get_balance_factor(node.left)<0:
            self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance_factor<-1 and self.get_balance_factor(node.right)>0:
            self._right_rotate(node.right)
            return self._left_rotate(node)

        return ret