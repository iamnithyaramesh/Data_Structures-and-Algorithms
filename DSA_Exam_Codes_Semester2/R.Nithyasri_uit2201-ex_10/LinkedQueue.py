from Node import Node

class LinkedQueue:

    def __init__(self):
        self.front=self.rear=Node()
        self.size=0
    
    def isempty(self):
        if self.front==self.rear:
            return True
    
    def peek(self):
        return self.rear.item
    
    def enqueue(self,val):
        x=Node(val)
        self.rear.next=x
        self.rear=self.rear.next
    
    def dequeue(self):
        x=self.front.next
        self.front.next=self.front.next.next
        return x
    
    def display(self):
        s=''
        pos=self.front.next
        while pos is not None:
            s+=str(pos.item)
            s+=','
            pos=pos.next
        print(s)
        
Q1=LinkedQueue()
Q1.isempty()
Q1.enqueue(10)
Q1.display()
Q1.enqueue(20)
Q1.display()
Q1.enqueue(30)
Q1.display()
Q1.dequeue()
Q1.display()