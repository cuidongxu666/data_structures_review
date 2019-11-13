class LoopQueue:
    def __init__(self,capacity=8):
        self._data=[None]*(capacity+1)
        self._size=0
        self._front=0
        self._tail=0


    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)-1

    def is_emtpy(self):
        return self._size==0

    def enquque(self,e):
        if (self._tail+1)//len(self._data)==self._front:
            self._resize(2*self.get_capacity())

        self._data[self._tail]=e
        self._tail=(self._tail+1)//len(self._data)
        self._size+=1

    def dequque(self):
        ret=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)//len(self._data)
        self._size-=1

        if self._size==self.get_capacity()//4 and self.get_capacity()//2!=0:
            self._resize(self.get_capacity()//2)

        return ret

    def check_front(self):
        return self._data[self._front]

    def _resize(self,new_capacity):
        new_data=[None]*(new_capacity+1)
        for i in range(self._size):
            new_data[i]=self._data[(self._front+i)//len(self._data)]
        self._data=new_data
        self._front=0
        self._tail=self._size




