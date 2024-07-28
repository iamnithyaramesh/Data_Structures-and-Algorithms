from Node import Node

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isempty(self):
        return self.size == 0

    def push(self, item):
        temp = Node(item)
        temp.next = self.top
        self.top = temp
        self.size += 1

    def pop(self):
        if self.isempty():
            raise Exception("Stack is empty.")
        del_item = self.top.item
        self.top = self.top.next
        self.size -= 1
        return del_item

    def peek(self):
        if self.isempty():
            raise Exception("Stack is empty.")
        return self.top.item

    def display(self):
        if self.isempty():
            print("Stack is empty.")
            return

        temp = self.top
        while temp is not None:
            print(temp.item, end=",")
            temp = temp.next
        print()



S1=LinkedStack()
print(S1.isempty())
S1.push(10)
S1.display()
S1.push(20)
S1.display()
S1.push(30)
S1.display()
print(S1.pop())
print(S1.peek())
    

                