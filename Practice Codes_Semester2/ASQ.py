import ctypes
class ListADT:

    def __init__(self,val):
        if isinstance(val,int):
            self.n=0
            self.capacity=1
            self.A=[]
        else:
            self.n=len(val)-1
            self.capacity=len(val)
            self.A=val
    
    def make_array(self,cap):
        self.capacity=cap
        dy_list=(cap*(ctypes.py_object))()
        return dy_list
    
    def resize(self,cap):
        B=self.make_array(cap)
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B
        self.capacity=cap

    def append(self,ele):
        if self.n<self.capacity:
            self.A[self.n]=ele
            self.n=self.n+1
        else:
            self.resize(2*self.capacity)
            self.arr[self.n] = ele
            self.n += 1

    
    def insert(self, index, ele):
        if 0 <= index < self.n:
            if self.n < self.capacity:
                for i in range(self.n, index, -1):
                    self.arr[i] = self.arr[i - 1]
                self.arr[index] = ele
                self.n += 1
            else:
                self.resize(2 * self.capacity)
                self.insert(index, ele)

    def remove(self, ele):
        for i in range(self.n):
            if self.arr[i] == ele:
                for j in range(i, self.n - 1):
                    self.arr[j] = self.arr[j + 1]
                self.n -= 1
                break

        if self.n < self.capacity // 2:
            self.resize(self.capacity // 2)


