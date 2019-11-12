from c1_array import Array
class MaxHeap:
    def __init__(self,arr=None,capacity=0):
        if isinstance(arr,Array):
            self._heap=arr
            for i in range(self._parent(self._heap.get_size()-1),-1,-1):
                self._sift_down(i)
            return
        self._heap=Array(capacity=capacity)

    def get_size(self):
        return self._heap.get_size()

    def is_empty(self):
        return self._heap.is_empty()


    def _parent(self,index):
        return (index-1)//2
    def _left_child(self,index):
        return index*2+1
    def _right_child(self,index):
        return index*2+2

    def add(self,e):
        self._heap.add_last(e)
        self._sift_up(self._heap.get_size()-1)

    def _sift_up(self,k):
        while k>0 and self._heap.get_element(k)>self._heap.get_element(self._parent(k)):
            self._heap.swap(k,self._parent(k))
            k=self._parent(k)

    def find_max(self):
        return self._heap.get_element(0)

    def extract_max(self):
        ret=self.find_max()
        self._heap.swap(0,self._heap.get_size()-1)
        self._heap.remove_last()
        self._sift_down(0)
        return ret
    def _sift_down(self,k):
        while self._left_child(k)<self._heap.get_size():
            j=self._left_child(k)
            if j+1<self._heap.get_size() and self._heap.get_element(j+1) >self._heap.get_element(j):
                j=self._right_child(k)

            if self._heap.get_element(k)>self._heap.get_element(j):
                break
            self._heap.swap(j,k)
            k=j

    def replace(self,e):
        ret=self.find_max()
        self._heap.set(0,e)
        self._sift_down(0)
        return ret
