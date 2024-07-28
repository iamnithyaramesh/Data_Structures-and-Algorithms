from lnode import LNode
class LinkedList(LNode):

    def __init__(self):
        self.head=self.tail=LNode()

    def append(self,item):
        x=LNode(item)
        self.tail.next=x
        self.tail=x
    
    def isempty(self):
        if self.head==self.tail:
            return True
    
    def display(self):
        s="["
        pos=self.head.next
        while pos is not None:
            s+=str(pos.item)+','
            pos=pos.next
        s+="]"
        print(s)

    def find(self,ele):
        pos=self.head.next
        while pos is not None:
            if pos.item==ele:
                return True
            else:
                pos=pos.next
    
    def insert(self,index,item):
        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        temp=LNode(item)
        temp.next=pos.next.next
        pos.next=temp
    
    def delete(self,index):
        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        del_item=pos.next.item
        pos.next=pos.next.next
        return del_item

    def insert_by_prev_value(self,prev,insert_item):
        pos=self.head.next
        while pos is not None:
            if pos.item==prev:
                x=LNode(insert_item)
                x.next=pos.next.next
                pos.next=x
            else:
                pos=pos.next
    
    def delete_by_prev_value(self,ele):
        pos=self.head.next
        while pos is not None:
            if pos.item==ele:
                del_item=pos.next.item
                pos.next=pos.next.next
            else:
                pos=pos.next
    
    def reverse(self):
        l1=self
        new_dh=LNode()
        pos=self.head.next
        while pos is not None:
            pos=pos.next
    
    def swap(self,node1,node2):
        pos=self.head.next
        while pos.item!=node1.item:
            pos=pos.next
        temp1=node1
        temp2=node2
        pos.next=temp2
        temp1.next=pos.next.next
        temp2.next=temp1

  
    
        

    
L1=LinkedList()
print(L1.isempty())

L1.append(10)
print('\n')
L1.display()

L1.append(20)
print('\n')
L1.display()

L1.append(30)
print('\n')
L1.display()

L1.append(40)
print('\n')
L1.display()

print('\n')
L1.find(40)

L1.insert(2,45)
print('\n')
L1.display()

L1.delete(2)
print('\n')
L1.display()

L1.insert_by_prev_value(10,35)
print('\n')
L1.display()

L1.delete_by_prev_value(10)
print('\n')
L1.display()


    





        
