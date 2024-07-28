
import ctypes
class FoodDelivery:

    def __init__(self,M):
        self.cap=M
        self.queue=self.makearray(self.cap)
        self.rear=self.front=0

    def makearray(self,cap):
        temp= (cap*(ctypes.py_object))()
        return temp
    
    def next(self,pos):
        return (pos+1)%self.cap
    
    def isempty(self):
        if self.rear==self.front==0:
            return True
    
    def isfull(self):
        return (self.rear+1)%self.cap==self.front
    
    def enqueue(self,item):
        if (self.isfull()):
            raise Exception
        else:
           self.queue[self.rear]=item
           self.rear=FoodDelivery.next(self,self.rear)

    def dequeue(self,item):
        if self.queue.isempty():
            raise Exception
        else:
            x=self.queue[self.rear]
            self.front=FoodDelivery.next(self,self.front)
            return x

    def __len__(self):
        return len(self.queue)
    
    def __getitem__(self,index):
        return self.queue[index]
    
    def __setitem__(self,index,value):
        self.queue[index]=value

    def __str__(self):
        return str(self.queue)
        
    
M=int(input("Enter NO"))
Order_Stack=FoodDelivery(M)
for i in range(M):
    item=input("Enter food item")
    Order_Stack.enqueue(item)
print(Order_Stack)
    

