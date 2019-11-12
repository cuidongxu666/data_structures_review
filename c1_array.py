class Array:
    def __init__(self,arr=None,capacity=8):
        if not arr:
            self._data=[None]*capacity
            self._size=0
        else:
            self._data=arr
            self._size=len(arr)

    def is_empty(self):
        return self._size==0

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)
    def get_element(self,index):
        return self._data[index]

    def get_first(self):
        return self._data[0]

    def get_last(self):
        return self._data[-1]

    def insert(self,index,e):
        if self._size==self.get_capacity():
            if self._size==0:
                self._resize(1)
            else:
                self._resize(2*self.get_capacity())
        for i in range(self.get_size()-1,index-1,-1):
            self._data[i+1]=self._data[i]
        self._data[index]=e
        self._size+=1

    def _resize(self,new_capacity):
        new_data=[None]*new_capacity
        for i in range(self.get_size()):
            new_data=self._data[i]
        self._data=new_data

    def find_index(self,e):
        for i in range(self.get_size()):
            if self._data[i]==e:
                return i
        return -1

    def add_first(self,e):
        self.insert(0,e)

    def add_last(self,e):
        self.insert(self.get_size(),e)


    def contains(self,e):
        for i in range(self.get_size()-1):
            if self._data[i] ==e:
                return True
        else:
            return False
    def set(self,index,e):
        self._data[index]=e

    def remove(self,index):
        for i in range(index+1,self.get_size()):
            self._data[i-1]=self._data[i]
        self._size-=1
        if self._size == self.get_capacity()//4 and self.get_capacity()//2!=0:
            self._resize(self.get_capacity()//2)
        return self._data[index]

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.get_size()-1)

    def remove_element(self,e):
        index=self.find_index(e)
        if index != -1:
            self.remove(index)

    def swap(self,i,j):
        self._data[i],self._data[j]=self._data[j],self._data[i]




