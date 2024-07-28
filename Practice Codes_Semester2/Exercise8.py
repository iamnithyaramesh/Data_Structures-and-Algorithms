import ctypes
import sys
class ListADT:
    def __init__(self,val):
        if isinstance(val,int):        #For a single element list
            self.n=0
            self.capacity=1
            self.A=self.make_array(self.capacity) #Allocation of memory
        else:
            self.n=len(val)-1            #For a multiple element list
            self.A=val
            self.capacity=len(val)

    def make_array(self,cap):
        self.capacity=cap
        dy_list=(cap*ctypes.py_object)()
        return dy_list
    
    def resize(self,cap):
        B=self.make_array(cap)
        for index in range(self.n):
            B[index]=self.A[index]
        self.A=B
        self.capacity=cap
    
    def append(self,val):
        if self.n<self.capacity:
            self.A[self.n]=val
            self.n=self.n+1
        else:
            self.resize(2*self.capacity)
        def __str__(self):
            return str(self.A)
        return self.A.__str__()


    def __str__(self):
         return str(self.A)

    def __len__(self):
        return len(self.A)
    
    def __getitem__(self,index):
        return self.A[index]
    
    def __setitem__(self,index,value):
        self.A[index]=value
    
    
# Allocation of memory spaces based on capcaity 


L1=ListADT([1,2,3])
print(L1)
for i in range(5):
    value=int(input())
    L1.append(value)
print(L1)





