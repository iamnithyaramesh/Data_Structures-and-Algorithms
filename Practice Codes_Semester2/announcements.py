

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

Announcements=CircularLL()
announcement_no=0
print("User Menu")
print("Enter 1 to Enter Announcement")
print("Enter 2 to Delete Announcement")
print("Enter 3 to Display Announcement List(Oldest to Newest)")
print("Enter 4 to Display Announcement List(Newest to Oldest)")
print("Press any other number to Exit")
while True:
 user_menu=int(input("Enter Choice"))

 if user_menu==1:
    announcement_no+=1
    com=input("Enter your Announcement")
    d={announcement_no:com}
    Announcements.append(d)
    print("You Announcement has been successfully recorded!")

 elif user_menu==2:
    Announcements.display()
    com_del=int(input("Enter Announcement No to delete"))
    Announcements.delete(com_del)
    Announcements.display()
    print("Your Announcement has been successfully removed!")
    
 elif user_menu==3:
     print("Announcement List")
     Announcements.display()

 elif user_menu==4:
    print("Announcements List")
    Announcements.reversedisplay()

 else:
     break