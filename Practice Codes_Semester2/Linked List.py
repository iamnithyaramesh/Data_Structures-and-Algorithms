from Node import Node
class LinkedList:

    def __init__(self):
        self.head=self.tail=Node()
    
    def __isempty__(self):
        return (self.head==self.tail)
    
    def append(self,val):
        new=Node(val)
        new.next=self.tail.next
        self.tail.next=new
    
    def insert(self,val,index):
        new=Node(val)
        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        new.next=pos.next
        pos.next=new
    
    def remove(self,val):
        pos=self.head.next
        while pos is not None:
            if pos.item==val:
                return pos
            
    def popitem(self,index):
        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        pos.next=pos.next.next
    
    def pop(self):
        pos=self.head.next
        while pos.next is not None:
            if pos.next==self.tail:
                pos.next=None
    
    def __str__(self):
        pos=self.head.next
        s=''
        while pos is not None:
            s+=str(pos.item)
        return s

L1=LinkedList()
print(L1)
L1.append(10)
print(L1)
L1.append(20)
print(L1)
L1.append(30)
print(L1)
L1.append(40)
print(L1)
L1.remove(30)
L1.insert(50,2)
L1.pop()
L1.popitem(3)
print(L1)

        
        

