import ctypes

'''class Dynamic_Array:

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.arr = self.makearray(self.capacity)
    
    def makearray(self, cap):
        temp = (cap * ctypes.py_object)()
        return temp
    
    def resize(self, capacity):
        B = self.makearray(capacity)
        for i in range(self.n):
            B[i] = self.arr[i]
        self.arr = B
        self.capacity = capacity
        return self.arr

    def append(self, item):
        if self.n < self.capacity:
            self.arr[self.n] = item
            self.n += 1
        else:
            self.resize(2 * self.capacity)
            self.arr[self.n] = item
            self.n += 1
        
    def delete(self, index):
        if not (0 <= index < self.n):
            raise IndexError("Index out of range")
        del_item = self.arr[index]
        if self.n < self.capacity // 4:
            self.resize(self.capacity // 2)
        for i in range(index, self.n -1):
            self.arr[i] = self.arr[i + 1]
        self.n -= 1
        print(del_item)
    
    def insert(self,index,item):
        if not(0<=index<=self.n):
            raise IndexError
        else:
            if self.n==self.capacity:
                self.resize(2*self.capacity)
            for i in range(self.n,index,-1):
                self.arr[i]=self.arr[i-1]
            self.arr[index]=item
            self.n+=1

    def display(self):
        res = "["
        for i in range(self.n):
            res += str(self.arr[i]) + ","
        res += "]"
        print(res)

# Test the Dynamic_Array class
D = Dynamic_Array()
D.append(1)
D.display()
D.append(2)
D.display()
D.insert(1,3)
D.display()
D.insert(0,4)
D.display()


import ctypes

class Compact_Stack:

    def __init__(self, capacity):
        self.n = 0
        self.capacity = capacity
        self.arr = self.makearray(self.capacity)
    
    def makearray(self, cap):
        temp = (cap * ctypes.py_object)()
        return temp
    
    def push(self, item):
        if self.n < self.capacity:
            self.arr[self.n] = item
            self.n += 1
        else:
            raise IndexError("Stack is full")

    def pop(self):
        if self.n != 0:
            print(self.arr[self.n-1])
            self.n-=1

    def peek(self):
        if self.n != 0:
            return self.arr[self.n - 1]

    def isempty(self):
        return self.n == 0

    def isfull(self):
        return self.n == self.capacity

    def display(self):
        res = "["
        for i in range(self.n):
            res += str(self.arr[i]) + ","
        res += "]"
        print(res)

S = Compact_Stack(10)
S.push(10)
S.display()
S.push(20)
S.display()
S.push(30)
S.display()
S.pop()
S.display()
print(S.peek())'''

'''class Compact_Queue:

    def __init__(self,capacity):
        self.n=0
        self.capacity=capacity
        self.arr=self.makearray(self.capacity)
    
    def makearray(self, cap):
        temp = (cap * ctypes.py_object)()
        return temp
    
    def isfull(self):
        return(self.n==self.capacity)

    def isempty(self):
        return self.n==0
    
    def enqueue(self,item):
        if not(self.isfull()):
            self.arr[self.n]=item
            self.n+=1
        else:
            raise IndexError
    
    def dequeue(self):
        if not self.isempty():
            for i in range(self.n - 1):
                self.arr[i] = self.arr[i + 1]
            self.n -= 1




    def display(self):
        res = "["
        for i in range(self.n):
            res += str(self.arr[i]) + ","
        res += "]"
        print(res)

Q=Compact_Queue(8)
Q.enqueue(10)
Q.display()
Q.enqueue(20)
Q.display()
Q.enqueue(30)
Q.display()
Q.dequeue()
Q.display()'''

class Circular_Queue:

    def __init__(self,capacity):
        self.capacity=capacity
        self.arr=self.makearray(self.capacity)
        self.front=self.rear=0
    
    def next(self,pos):
        return ((pos+1)%self.capacity)
    
    def isempty(self):
        return (self.front==self.rear)
    
    def isfull(self):
        return(self.next(self.rear)==self.front)

    def enqueue(self,item):
        if not(self.isfull()):
            self.arr[self.rear]=item
            self.rear=self.next(self.rear)
    
    def dequeue(self):
        if not(self.isempty()):
            x=self.arr[self.front]
            self.front=self.next(self.front)
        return x

      
CQ=Circular_Queue(5)
CQ.enqueue(10)

    
        


    


