from Node import Node
class Linked_Stack:

    def __init__(self):
        self.top=Node()
    
    def __isempty__(self):
        if self.top.next is None:
            return True
        else:
            return False
    
    def peek(self):
        if self.__isempty__()==False:
            return self.top.next.item
    
    def push(self,element):
        x=Node(element)
        x.next=self.top.next.next
        self.top.next=x
    
    def pop(self):
        x=self.top.next.item
        self.top.next=self.top.next.next
        return x

    def __str__(self):
        pos=self.top.next
        s=''
        while pos is not None:
            s+=str(pos.item)
            pos=pos.next
        return s
            

S=Linked_Stack()
S.__isempty__()
S.push(10)
S.peek()
S.push(20)
S.pop()
print(S)


