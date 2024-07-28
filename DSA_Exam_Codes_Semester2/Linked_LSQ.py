from Linked_Implementation import Single_Node

'''class Linked_List:

    def __init__(self, item=None, next=None):
        self.head = self.tail = Single_Node()
        self.size = 0
    
    def isempty(self):
        return self.head == self.tail

    def append(self, item):
        temp = Single_Node(item)
        self.tail.next = temp
        self.tail = temp
        self.size += 1
    
    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        temp = Single_Node(item)
        pos = self.head.next
        for i in range(index - 1):
            pos = pos.next
        temp.next = pos.next
        pos.next = temp
        self.size += 1
    
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        pos = self.head.next
        for i in range(index - 1):
            pos = pos.next
        s = pos.next.item
        pos.next = pos.next.next
        self.size -= 1
        return s
    
    def display(self):
        res = " "
        pos = self.head.next
        while pos is not None:
            res += str(pos.item) + "--->"
            pos = pos.next
        print(res)



if __name__ == "__main__":
    L = Linked_List()

    print("Is the list empty?", L.isempty())  # Output: Is the list empty? True

    L.append(1)
    L.append(2)
    L.append(3)

    print("List after appending elements:")
    L.display()  # Output:  1--->2--->3--->

    L.insert(1, 10)
    L.insert(2, 20)

    print("List after inserting elements:")
    L.display()  # Output:  1--->10--->2--->20--->3--->

    removed_item = L.remove(1)
    print("Removed item:", removed_item)  # Output: Removed item: 2

    print("List after removing an element:")
    L.display()  # Output:  1--->10--->20--->3--->

    print("Is the list empty?", L.isempty()) ''' # Output: Is the list empty? False


'''class Linked_Stack:

    def __init__(self,item=None,next=None):

        self.top=Single_Node()
        self.size=0
    
    def push(self,item):
        temp=Single_Node(item)
        temp.next=self.top.next
        self.top.next=temp
        self.size+=1
    
    def pop(self):
        x=self.top.next.item
        self.top.next=self.top.next.next
        self.size-=1
    
    def peek(self):
        return self.top.next.item

    def display(self):
        res="["
        pos=self.top.next
        while pos is not None:
            res+=str(pos.item)+"--->"
            pos=pos.next
        print(res)


Link_Stack=Linked_Stack()
Link_Stack.push(10)
Link_Stack.display()
Link_Stack.push(20)
Link_Stack.display()
Link_Stack.pop()
Link_Stack.display()'''

class Linked_Queue:

    def __init__(self,item=None,next=None):

        self.front=self.rear=Single_Node()
        self.size=0
    
    def isempty(self):
        if self.front==self.rear:
            return True
    
    def enqueue(self,item):
        temp=Single_Node(item)
        self.rear.next=temp
        self.rear=temp
        self.size+=1
    
    def dequeue(self):
        del_item=self.front.next.item
        self.front.next=self.front.next.next
        self.size-=1
        return del_item
    
    def display(self):
        res="["
        pos=self.front.next
        while pos is not None:
            res+=str(pos.item)+","
            pos=pos.next   
        print(res)

LQ=Linked_Queue()
LQ.enqueue(10)
LQ.enqueue(20)
LQ.display()
LQ.dequeue()
LQ.display()     

class Circular_Queue:

    def __init__(self,item=None,next=None):

        self.rear=None
        self.size=0
    
    def isempty(self):
        return self.rear==None

    def enqueue(self,item):
     if self.size==0:
        temp=Single_Node(item)
        self.rear.next=temp
        self.rear=temp
        self.size+=1
     else:
         self.rear.next=temp
         temp.next=self.rear
         self.size+=1
    
    def dequeue(self):
        self.rear.next=self.rear.next.next






        