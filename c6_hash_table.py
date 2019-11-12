from c5_avltree import AVLMap
_UPPER_TOL = 10
_LOWER_TOL = 2
_INIT_CAPACITY = 7
class HashTable:
    def __init__(self,M=_INIT_CAPACITY):
        self._M=M
        self._hashtable=[AVLMap() for _ in range(self._M)]
        self._size=0

    def _hash(self,key):
        return hash(key)%0x7fffffff %self._M

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def add(self,key,value):
        treemap=self._hashtable[self._hash(key)]
        treemap.add(key,value)
        self._size+=1

        if self._size>=_UPPER_TOL*self._M:
            self._resize(2*self._M)

    def contains(self,key):
        treemap = self._hashtable[self._hash(key)]
        if treemap.contains(key):return True
        return False

    def getter(self,key):
        treemap = self._hashtable[self._hash(key)]
        return treemap.get(key)

    def setter(self,key,value):
        treemap = self._hashtable[self._hash(key)]
        treemap.setter(key,value)

    def remove(self,key):
        treemap = self._hashtable[self._hash(key)]
        ret=treemap.remove(key)
        self._size-=1

        if self._size<_LOWER_TOL*self._M and self._M//2>=_INIT_CAPACITY:
            self._resize(self._M//2)

        return ret

    def _resize(self,new_M):
        new_hashtable=[AVLMap() for _ in range(new_M)]
        old_M=self._M
        for i in range(old_M):
            treemap=self._hashtable[i]
            all_nodes=treemap.get_all_nodes()
            for node in all_nodes:
                key=node.key
                value=node.value
                new_hashtable[self._hash(key)].add(key,value)
                
        self._hashtable=new_hashtable
