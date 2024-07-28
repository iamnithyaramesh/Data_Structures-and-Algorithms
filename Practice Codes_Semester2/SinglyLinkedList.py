from Node import Node

class SinglyLinkedList:
    def __init_(self,tail=None,head=None):
        self.head=self.tail=Node()
        self.size=0
    
    def isempty(self):
        if self.head==self.tail:
            return True
    
    def append(self,val):
        temp=Node(val)
        self.tail.next=temp
        self.tail=temp
        self.size+=1
    
    def insert(self,index,val):
        temp=Node(val)
        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        temp.next=pos.next.next
        pos.next=temp
    
    def remove(self,index):
        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        x=pos.next.item
        pos.next=pos.next.next
        return x
    
    def display(self):
        pos=self.head.next
        while pos is not None:
            return str(pos.item)
    
L1=SinglyLinkedList()
L1.append(1)
L1.append(2)
L1.append(3)
L1.insert(5,1)
L1.remove(2)
L1.display()
