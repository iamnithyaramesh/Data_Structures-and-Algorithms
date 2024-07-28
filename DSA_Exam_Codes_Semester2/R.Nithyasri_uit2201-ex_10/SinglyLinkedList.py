from Node import Node

class SinglyLinkedList:
    
    def __init__(self):
        self.head=self.tail=Node()
    
    def isempty(self):
        return self.head==self.tail
    
    def display(self):
        print("List:")
        pos=self.head.next
        while pos is not None:
            print(pos.item,end=',')
            pos=pos.next
    
    def find(self,ele):
        pos=self.head.next
        while pos.next is not None:
            if pos.next.item==ele:
                print("Found")
                break
            else:
                pos=pos.next
        else:
         
         print("Not Found")

    def append(self,ele):
        temp=Node(ele)
        self.tail.next=temp
        self.tail=temp
    
    def insert(self,index,ele):
        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        temp=Node(ele,pos.next)
        pos.next=temp
    
    def delete(self,index):
        pos=self.head
        for i in range(index-1):
             pos=pos.next
        pos.next=pos.next.next
    
    def insert_by_prev_value(self,prev,ele):
        pos=self.head
        while pos is not None:
                if pos.item!=prev:
                    pos=pos.next
                else:
                    break
                temp=Node(ele)
                temp.next=pos.next
                pos.next=temp

    def delete_by_prev_value(self,prev):
        pos=self.head.next
        while pos.item!=prev:
                pos=pos.next
        temp=pos.next.item
        pos.next=pos.next.next
        print(temp)
    

L1=SinglyLinkedList()
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
    
