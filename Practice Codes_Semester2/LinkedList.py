'''class LinkedList:

    class LNode:

        __slots__=['item','next']

        def __init__(self,item=None,next=None):

            self.item=item
            self.next=next
    
    def __init__(self,item=None,next=None):

        self.head=self.tail=LinkedList.LNode()
        self.size=0
    
    def append(self,ele):
        x=LinkedList.LNode(ele)
        self.tail.next=x
        self.tail=x
        self.size+=1
    
    def __str__(self):
        s=""
        pos=self.head.next
        while pos is not None:
            s+=str(pos.item)+" "
            pos=pos.next
        return s
    
    def find(self,ele):
        pos=self.head.next
        while pos is not None:
            if pos.item==ele:
                return pos

    def swap(self,item_1,item_2):
        add_1=self.find(item_1)
        add_2=self.find(item_2)

        pos=self.head.next
        while pos is not None:
            if pos.next==add_1:
                prev=pos
                next=pos.next.next
            if pos.next==add_2:
                prev_2=pos
                next_2=pos.next.next
        add_2.next=next
        prev.next=add_2
        add_1.next=next_2
        prev_2.next=add_1

L=LinkedList()
L.append(10)
L.append(20)
L.append(30)
L.append(40)
print(L)
L.swap(20,30)
print(L)
L.swap(10,40)
print(L)
'''

'''class DoublyLinkedList:

    class DNode:

        def __init__(self,item=None,next=None,prev=None):

            self.item=item
            self.next=next
            self.prev=prev
    
    def __init__(self,item=None,next=None,prev=None):

        self.head=self.tail=DoublyLinkedList.DNode()
        self.size=0
    
    def append(self,item):

        x=DoublyLinkedList.DNode(item)
        self.tail.next=x
        x.prev=self.tail
        self.tail=x
        self.size+=1
    
    def __str__(self):
        s=""
        pos=self.head.next
        while pos is not None:
            s+=str(pos.item)+" "
            pos=pos.next
        return s
    
    def reversedisplay(self):
        s=""
        pos=self.tail
        while pos is not None:
            s+str(pos.item)+" "
            pos=pos.prev
        print(s)

D=DoublyLinkedList()
D.append(10)
D.append(20)
D.append(30)
print(D)
D.reversedisplay()
'''

class CircularList:

    



        

