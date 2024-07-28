from Linked_Implementation import Double_Node

'''class Doubly_Linked_List:

    def __init__(self,item=None,next=None,prev=None):

        self.head=self.tail=Double_Node()
    
    def isempty(self):
        return self.head==self.tail
    
    def append(self,item):
        temp=Double_Node(item)
        self.tail.next=temp
        temp.prev=self.tail
        self.tail=temp

    def insert(self,index,item):
        pos=self.head.next
        temp=Double_Node(item)
        for i in range(index-1):
            pos=pos.next
        temp.next=pos.next
        pos.next.prev=temp
        pos.next=temp
        temp.prev=pos
    
    def remove(self,index):

        pos=self.head.next
        for i in range(index-1):
            pos=pos.next
        pos.next=pos.next.next
        pos.next.prev=pos
    
    def display(self):
        res="["
        pos=self.head.next
        while pos is not None:
            res+=str(pos.item)+","
            pos=pos.next
        res+="]"
        print(res)

dll = Doubly_Linked_List()
dll.append(10)
dll.display()
dll.append(20)
dll.display()
dll.append(30)
dll.display()
dll.insert(1, 15)  
dll.display()  
dll.remove(2)
dll.display()'''


class Double_Linked_Stack:
    def __init__(self, item=None):
        self.top = Double_Node(item)
        self.size = 0
    
    def push(self, item):
        temp = Double_Node(item)
        if self.top.next is None:  # Stack is empty
            self.top.next = temp
            temp.prev = self.top
        else:
            self.top.next.prev = temp
            temp.next = self.top.next
            self.top.next = temp
            temp.prev = self.top
        self.size += 1
    
    def pop(self):
        if self.top.next is None:  # Stack is empty
            print("Stack is empty. Cannot pop.")
        else:
            del_item = self.top.next.item
            self.top.next = self.top.next.next
            if self.top.next is not None:
                self.top.next.prev = self.top
            print(del_item)
            self.size -= 1
    
    def display(self):
        if self.top.next is None:  # Stack is empty
            print("[]")
        else:
            res = "["
            pos = self.top.next
            while pos is not None:
                res += str(pos.item) + "<"
                pos = pos.next
            print(res)


stack = Double_Linked_Stack()
stack.push(10)
stack.display() 
stack.push(20)
stack.display() 
stack.push(30)
stack.display() 
print("Double Linked Stack:")
stack.display()  
stack.pop()  
stack.display()









        
    
        