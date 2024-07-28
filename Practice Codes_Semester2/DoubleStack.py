import ctypes
class DoubleStack:

    def __init__(self,capacity):
        self.capacity=capacity
        self.arr=self.makearray(capacity)
        self.top1=0
        self.top2=capacity-1
    
    def makearray(self,capacity):
        temp=(capacity*(ctypes.py_object))()
        return temp
    
    def isempty(self):
        if self.top1==0 and self.top2==self.capacity:
            return True
    
    def isfull(self):
        if not(self.isempty):
           return True
    
    def push(self,pos,val):
        if self.isfull():
            raise Exception
        else:
         if pos==0:
            self.arr[self.top1]=str(val)
            self.top1+=1
         elif pos==1:
            self.arr[self.top2]=str(val)
            self.top2-=1

    def pop(self,pos):
        if self.isempty():
            raise Exception
        else:
         if pos==0:
            x=self.arr.pop(0)
            return x
         elif pos==1:
            x=self.arr.pop()
            return x
    
    
S1=DoubleStack(10)
S1.push(0,10)
print(S1)
S1.push(0,20)
print(S1)
S1.push(0,30)
print(S1)
S1.push(1,40)
print(S1)
S1.push(1,50)
print(S1)
S1.push(1,60)
print(S1)
    
