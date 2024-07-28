

class DNode:
    __slots__ = ['item', 'next', 'prev']

    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = None
        self.prev = None


class CircularLL(DNode):
    def __init__(self, item=None, next=None):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __getitem__(self,index):
        pos=self.head
        for i in range(index-1):
            pos=pos.next
        return str(pos.item)

    def append(self, ele):
        x = DNode(ele)
        if self.head is None:
            self.head = self.tail = x
            x.next = x
            x.prev = x
        else:
            x.next = self.head
            x.prev = self.tail
            self.tail.next = x
            self.head.prev = x
            self.tail = x
        self.size += 1

    def insert(self, index, item):
        x = DNode(item)
        if index <= 0:
            x.next = self.head
            x.prev = self.tail
            self.tail.next = x
            self.head.prev = x
            self.head = x
        elif index >= self.size:
            self.append(item)
        else:
            pos = self.head
            for i in range(index - 1):
                pos = pos.next
            x.next = pos.next
            x.prev = pos
            pos.next.prev = x
            pos.next = x
        self.size += 1

    def delete(self, key):
        if self.head is None:
            return
        pos = self.head
        while True:
            if isinstance(pos.item, dict) and key in pos.item:
                if pos == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
                elif pos == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    pos.prev.next = pos.next
                    pos.next.prev = pos.prev
                self.size -= 1
                break
            pos = pos.next
            if pos == self.head:
                break

    def display(self):
        if self.head is None:
            return
        s = ""
        pos = self.head
        while True:
            s += str(pos.item)
            pos = pos.next
            if pos == self.head:
                break
        print(s)

    def reversedisplay(self):
        if self.head is None:
            return
        s = ""
        pos = self.tail
        while True:
            s += str(pos.item)
            pos = pos.prev
            if pos == self.tail:
                break
        print(s)
    
    def display_specific(self, key):
        if self.head is None:
            return
        pos = self.head
        while pos is not None:
            if pos.item[0]==key:
                print(pos.item[1])


Complaints=CircularLL()
complaint_no=0
print("User Menu")
print("Enter 1 to Enter Complaint")
print("Enter 2 to Delete Complaint")
print("Enter 3 to Display Complaints List(Oldest to Newest)")
print("Enter 4 to Display Complaints List(Newest to Oldest)")
print("Enter 5 to Display Specific Complaint")
print("Press any other number to Exit")
while True:
 user_menu=int(input("Enter Choice"))

 if user_menu==1:
    complaint_no+=1
    com=input("Enter your Complaint")
    d={complaint_no:com}
    Complaints.append(d)
    print("You complaints has been successfully recorded!")

 elif user_menu==2:
    Complaints.display()
    com_del=int(input("Enter Complaint No to delete"))
    Complaints.delete(com_del)
    Complaints.display()
    print("Your Complaint has been successfully removed!")
    
 elif user_menu==3:
     print("Complaints List")
     Complaints.display()

 elif user_menu==4:
    print("Complaints List")
    Complaints.reversedisplay()
 elif user_menu==5:
     index=int(input("Enter Complaint No"))
     Complaints.display_specific(index)


 else:
     break
x=len(Complaints)
print(x)







    


